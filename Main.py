from RiotAPI import RiotAPI
import RiotConsts as Consts

def main():
    #summoner = raw_input()

    api = RiotAPI(Consts.KEY)

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


if __name__ == "__main__":
    main()
