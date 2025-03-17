import requests
from datetime import datetime

MY_LAT = 29.785786
MY_LONG = -95.824394

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# data = response.json()
# print(data)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]['latitude']

# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    'lat':MY_LAT,
    'lng':MY_LONG,
    'formatted':0,
    'tzid':'CST'
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
print(data)
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now)
