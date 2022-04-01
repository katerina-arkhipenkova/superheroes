import requests

hero_dict = {}


def get_request(*hero_names):
    for hero_name in hero_names:
        url = f'https://www.superheroapi.com/api.php/2619421814940190/search/{hero_name}'
        resp = requests.get(url)
        hero_dict[hero_name] = resp.json()['results'][0]['powerstats']['intelligence']


if __name__ == '__main__':
    get_request('Hulk', 'Captain America', 'Thanos')
    print(f'{max(hero_dict)} - самый умный супергерой')


