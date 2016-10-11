from RiotAPI import RiotAPI

def main():
    api = RiotAPI('RGAPI-42ee3ede-f853-4412-95fd-ec912ab55c0d')
    r = api.get_summoner_by_name('Anguriel')
    print r

if __name__ == "__main__":
    main()
