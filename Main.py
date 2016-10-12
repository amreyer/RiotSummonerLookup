from RiotAPI import RiotAPI
import RiotConsts as Consts

def main():

    regionMenu()

    while(True):
        choice = input('Enter the number of your region (1-5): ')
        if(1<=choice<=5):
            break
        else:
            print 'ERROR: Invalid Region Choice'

    region = Consts.REGIONS['north_america']

    if(choice==1):
        region = Consts.REGIONS['north_america']
    elif(choice==2):
        region = Consts.REGIONS['europe_west']
    elif(choice==3):
        region = Consts.REGIONS['europe_nordic_and_east']
    elif(choice==4):
        region = Consts.REGIONS['korea']
    elif(choice==5):
        region = Consts.REGIONS['brazil']

    api = RiotAPI(Consts.KEY, region)


    r = api.get_summoner_by_name('Anguriel')
    sumID = r['anguriel']['id']

    league = api.get_league_by_id(sumID)

    #print league[str(sumID)][0]['entries'][0]
    wins = league[str(sumID)][0]['entries'][0]['wins']
    losses = league[str(sumID)][0]['entries'][0]['losses']
    games = wins + losses

    winRate = float(wins)/games
    winRate = round(winRate,2)*100

    name = league[str(sumID)][0]['entries'][0]['playerOrTeamName']
    leaguePoints = league[str(sumID)][0]['entries'][0]['leaguePoints']
    division = league[str(sumID)][0]['entries'][0]['division']
    tier = league[str(sumID)][0]['tier']

    print "Name: {name} \n" \
          "Rank: {tier} {division}\n" \
          "Win Rate: %{winRate}\n".format(name=name, tier=tier, division=division, winRate=winRate)


    #print league[str(sumID)][0]

def regionMenu():
    print '1. North America \n' \
          '2. European West \n' \
          '3. European and Nordic East \n' \
          '4. Korea \n' \
          '5. Brazil \n'



if __name__ == "__main__":
    main()

