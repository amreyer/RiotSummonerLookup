import operator
from RiotAPI import RiotAPI
import RiotConsts as Consts


def main():
    champDict = map_champs_to_id()

    region_menu()

    while (True):
        try:
            choice = int(input('Enter the number of your region (1-5): '))
        except NameError:
            print 'Enter a anumber (1-5)'
            continue

        if (1 <= choice <= 5):
            break
        else:
            print 'ERROR: Invalid Region Choice'

    region = Consts.REGIONS['north_america']

    if (choice == 1):
        region = Consts.REGIONS['north_america']
    elif (choice == 2):
        region = Consts.REGIONS['europe_west']
    elif (choice == 3):
        region = Consts.REGIONS['europe_nordic_and_east']
    elif (choice == 4):
        region = Consts.REGIONS['korea']
    elif (choice == 5):
        region = Consts.REGIONS['brazil']

    api = RiotAPI(Consts.KEY, False, region)  # Creates an API to access regional
    staticAPI = RiotAPI(Consts.KEY, True, region)  # Creates an API to access static data

    summoner = raw_input("Enter your summoner name: ")
    summoner = summoner.replace(" ", "")
    print

    r = api.get_summoner_by_name(summoner)

    try:
        sumID = r[summoner.lower()]['id']
    except KeyError:
        print 'Summoner does not exist'
        quit()
    # print sumID

    if(r[summoner.lower()]['summonerLevel']==30):
        league = api.get_league_by_id(sumID)
    else:
        name = r[summoner.lower()]['name']
        level = r[summoner.lower()]['summonerLevel']

        print 'Name: {name} \n' \
              'Level: {level} \n'.format(name=name, level=level)
        quit()

    # print league[str(sumID)][0]['entries'][0]
    wins = league[str(sumID)][0]['entries'][0]['wins']
    losses = league[str(sumID)][0]['entries'][0]['losses']
    games = wins + losses

    winRate = float(wins) / games
    winRate = round(winRate, 2) * 100

    name = league[str(sumID)][0]['entries'][0]['playerOrTeamName']
    leaguePoints = league[str(sumID)][0]['entries'][0]['leaguePoints']
    division = league[str(sumID)][0]['entries'][0]['division']
    tier = league[str(sumID)][0]['tier']

    print "Name: {name} \n" \
          "Rank: {tier} {division} {leaguePoints} LP\n" \
          "Win Rate: %{winRate}\n".format(name=name, tier=tier, division=division,
                                          winRate=winRate, leaguePoints=leaguePoints)

    champStats = api.get_stats_by_id(sumID)['champions']

    gamesPlayed = []

    for champs in champStats:
        gamesPlayed.append([champs['id'], champs['stats']['totalSessionsPlayed'],
                            (float(champs['stats']['totalSessionsWon'])/float(champs['stats']['totalSessionsPlayed']))])

    sortedGamesPlayed = sorted(gamesPlayed, key=lambda champ: champ[1], reverse=True)

    idx = 1
    for champ in sortedGamesPlayed:
        if(champ[0]!=0):
            champ[0] = champDict[str(champ[0])]

    sortedWinPercent = sorted(gamesPlayed, key=lambda champ: champ[2], reverse=True)



    #update_champs(staticAPI)  # Only needs to be called if ids change


    print 'Top 3 Most Played Champions:'

    idx = 1
    while idx < 4:
        print '{idx}. {champ}  {games} played'.format(idx=idx, champ=sortedGamesPlayed[idx][0],
                                                  games=sortedGamesPlayed[idx][1])
        idx += 1

    print
    print 'Top 3 Highest Win Rate: '
    idx = 1
    rank = 1
    while(idx < 50 and rank < 4):
        if(sortedWinPercent[idx][1]>=10):
            print '{idx}. {champ}  %{rate} '.format(idx=rank, champ=sortedWinPercent[idx][0],
                                                  rate=(round(100* sortedWinPercent[idx][2])))
            idx += 1
            rank += 1
        else:
            idx += 1

def region_menu():
    print '1. North America \n' \
          '2. European West \n' \
          '3. European and Nordic East \n' \
          '4. Korea \n' \
          '5. Brazil \n'

def update_champs(staticAPI):
    champFile = open("Champions.txt", 'w')
    idx = 1
    while (idx < 500):
        try:
            champFile.write(str(idx) + ',' + staticAPI.get_champ_by_id(idx)['name'] + '\n')
            idx += 1
        except KeyError:
            idx += 1
    # Above lines are used to get an update up the champions and their ids
    champFile.close()

def map_champs_to_id():
    champDict = {}
    champFile = open("Champions.txt", 'r')
    for line in champFile:
        line = line.replace('\n','')
        line = line.split(',')
        champDict[line[0]] = line[1]

    return champDict

    champFile.close()



if __name__ == "__main__":
    main()
