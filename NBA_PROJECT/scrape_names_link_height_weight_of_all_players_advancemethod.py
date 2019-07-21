#importing the required libs
import requests
import datetime
bio = []
common_tag="/players/#!/"

if __name__ == '__main__':
    page_url = 'https://in.global.nba.com/playerindex/'
    s = requests.Session()
    s.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

    # visit the homepage to populate session with necessary cookies
    res = s.get(page_url)
    res.raise_for_status()

    json_url = 'https://in.global.nba.com/stats2/league/playerlist.json?locale=en'
    res = s.get(json_url)
    res.raise_for_status()
    data = res.json()
    
    for p in data['payload']['players']:
        name = p['playerProfile']['displayName']
        code = p['playerProfile']['code']
        href = common_tag+code
        weight = p['playerProfile']['weight']
        height = p['playerProfile']['height']
        dob = p['playerProfile']['dob']
        dob = datetime.datetime.fromtimestamp(int(dob)/1000.0).date()
        names = {
                "name" : name,
                "link" : href,
                "weight":weight,
                "height":height,
                "dob":dob
                }
        bio.append(names)
    
    
        
