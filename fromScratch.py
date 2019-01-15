import praw
import requests, json
import configparser
config = configparser.ConfigParser()
config.read('weatherApi.ini')
my_config = config['weather']

base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = 'Columbus'
complete_url = base_url + "appid=" + my_config['api_key'] + "&zip=14602"

columbus_weather = requests.get(complete_url)
columbus_weather_json = columbus_weather.json()


reddit = praw.Reddit('rit', user_agent='rit_site')
print(reddit.user.me())
stylesheet = reddit.subreddit('MyTestPostSub').stylesheet()
new_sheet = stylesheet.stylesheet + '*{background-color: red;}'
# reddit.subreddit('MyTestPostSub').stylesheet.update(new_sheet)