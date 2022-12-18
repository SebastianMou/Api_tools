import requests
import colorama
from colorama import Fore
from isodate import parse_duration


colorama.init(autoreset=True)


youtube_api_key = 'AIzaSyBAzvCjkFGn5mI1l8WnXc27Nw7xUVEhucM'

def menu():
    print('1) Youtube API (retorno básico)')
    print('2) Youtube API (todas las option)')
    print('3) Youtube API (optiones espesificas)')
    option = int(input('enter option:'))

    if option == 1:
        q = str(input(Fore.RED + 'va regresar lo basico y/n: '))
        if q == 'y' or 'Y':
            search_url = 'https://www.googleapis.com/youtube/v3/search'
            params = {
                'part': 'snippet',
                'q': 'learn python',
                'key': youtube_api_key,
                'maxResults': 1,
            }
            r = requests.get(search_url, params=params)
            print(Fore.WHITE+''+r.text)
            menu()
        else:
            menu()
    elif option == 2:
        q = str(input(Fore.RED + 'Youtube API (todas las option) y/n: '))
        if q == 'y':
            search_url = 'https://www.googleapis.com/youtube/v3/search'
            video_url = 'https://www.googleapis.com/youtube/v3/videos'
            search_params = {
                'part': 'snippet',
                'q': 'learn python',
                'key': youtube_api_key,
                'maxResults': 9,
                'type': 'video',
            }
            videos_ids = []

            r = requests.get(search_url, params=search_params)

            results = r.json()['items']
            for result in results:
                videos_ids.append(result['id']['videoId'])

            video_params = {
                'key': youtube_api_key,
                'part': 'snippet, contentDetails',
                'id': ','.join(videos_ids),
            }
            r = requests.get(video_url, params=video_params)
            print(Fore.WHITE+''+r.text)
            menu()
        else:
            menu()
    elif option == 3:
        q = str(input(Fore.RED + 'Youtube API (optiones espesificas) y/n: '))
        if q == 'y':
            search_url = 'https://www.googleapis.com/youtube/v3/search'
            video_url = 'https://www.googleapis.com/youtube/v3/videos'

            search_params = {
                'part': 'snippet',
                'q': 'learn python now',
                'key': youtube_api_key,
                'maxResults': 9,
                'type': 'video',
            }

            videos_ids = []
            r = requests.get(search_url, params=search_params)

            results = r.json()['items']

            for result in results:
                videos_ids.append(result['id']['videoId'])

            video_params = {
                'key': youtube_api_key,
                'part': 'snippet, contentDetails',
                'id': ','.join(videos_ids),
                'maxResults': 9,
            }
            r = requests.get(video_url, params=video_params)
            results = r.json()['items']


            for result in results:
                print('\n')
                print(Fore.WHITE+ 'title: ' +Fore.GREEN+ result['snippet']['title'])
                print(Fore.WHITE+ 'channal: ' +Fore.GREEN+ result['snippet']['channelTitle'])
                default_language = result['snippet'].get('defaultLanguage', 'N/A')
                print(Fore.WHITE+ 'defaultLanguage: ' +Fore.GREEN+ default_language)
                print(Fore.WHITE+ 'id: ' +Fore.GREEN+ result['id'])
                print(Fore.WHITE+ 'definition: ' +Fore.GREEN+ result['contentDetails']['definition'])
                print(Fore.WHITE+ 'time: ' +Fore.GREEN+ str(parse_duration(result['contentDetails']['duration']).total_seconds() // 60))
                print(Fore.WHITE+ 'thumbnails: ' +Fore.GREEN+ result['snippet']['thumbnails']['high']['url'])
                print(Fore.WHITE+ 'description: ' +Fore.GREEN+ result['snippet']['description'])
                tags = result['snippet']['tags']
                formatted_tags = ', '.join(tags)
                print(Fore.WHITE + 'tags: ' + Fore.GREEN + formatted_tags)
                print('\n')
            menu()
        else:
            menu()
    elif option == 0:
        print('good bye')
        exit()
    
menu()
