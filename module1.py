# Author: Ruaaaaast
# 2018/3/10
import requests
import datetime

def print_json(data):
    for object in data:
        print("{")
        for key in object:
            print(key, ":", object[key])
        print("}")

# Hero Info
# JSON Array [{dict}...]
def getHeroInfo():
    r = requests.get('https://api.opendota.com/api/heroes')
    data = r.json()
    #print_json(data)
    hero_table = {}
    for object in data:
        hero_table[object['id']] = object['localized_name']
    return hero_table

hero_table = getHeroInfo()

# extract useful information in a match
def getMatchInfo():
    r = requests.get('https://api.opendota.com/api/matches/3774178327')
    data = r.json()

    # Ban-pick data
    # TODO: hero_id to hero_name
    print_json(data['picks_bans'])

    # Players
    player_list = data['players']
    for player in player_list:
        print("----------------")
        print("account_id", player['account_id'])
        print("hero_name", hero_table[player['hero_id']])
        print("name", player['name'])
        print("isRadiant", player['isRadiant'])
        print("actions_per_min", player['actions_per_min'])
        print("kills", player['kills'])
        print("deaths", player['deaths'])
        print("assists", player['assists'])

    # Teams 
    print(data['radiant_team'])
    print(data['dire_team'])

    # Result
    print(data['radiant_win'])

#getMatchInfo()


def getHeroStats():
    r = requests.get('https://api.opendota.com/api/heroStats')
    data = r.json()
    print_json(data)

#getHeroStats()

# TODO: Get Team (Liquid) recent matches
# team_id for liquid is : 2163

def getTeamMatches():
    r = requests.get('https://api.opendota.com/api/teams/2163')
    data = r.json()
    print(data)
    r = requests.get('https://api.opendota.com/api/teams/2163/matches')
    data = r.json()
    for object in data:
        object['start_time'] = datetime.datetime.fromtimestamp(object['start_time']).strftime('%Y-%m-%d %H:%M:%S')
    print(data)

getTeamMatches()