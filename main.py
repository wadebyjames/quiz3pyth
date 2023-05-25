import requests
import json
key = '50cdee0c828715407939f518ce86df7b'
city = str(input('შეიტანეთ სასურველი ქალაქი: '))
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
result = requests.get(url)
json_r = result.text
res = json.loads(json_r)
shedegi = json.dumps(res, indent=4)
print(result)
print(shedegi)
print(result.text)
print(result.status_code)
print(result.headers)
k = res['main']
temp = k['temp']
temp -= 273.15
temp_min = k['temp_min']
temp_min -= 273.15
temp_max = k['temp_max']
temp_max -= 273.15
L = res['wind']
wind_speed = L['speed']
dict = {'ამჟამინდელი ტემპერატურა': temp, 'ქარის სიჩქარე': wind_speed, 'მაქსიმალური ტემპერატურა': temp_max,'მინიმალური ტემპერატურა': temp_min}
print(dict)



