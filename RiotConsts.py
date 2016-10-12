KEY = 'RGAPI-42ee3ede-f853-4412-95fd-ec912ab55c0d'

URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'summoner_by_name': 'v{version}/summoner/by-name/{names}',
    'league_by_summoner': 'v{version}/league/by-summoner/{ids}/entry'

}

API_VERSIONS = {
    'summoner': '1.4',
    'league': '2.5'
}


REGIONS = {
    'north_america': 'na',
    'brazil': 'br',
    'korea': 'kr',
    'europe_west': 'euw',
    'europe_nordic_and_east': 'eune'
}
