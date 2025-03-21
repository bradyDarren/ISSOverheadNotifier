import requests
from datetime import datetime
import smtplib

# setting coordinates
MY_LAT = 38.545502
MY_LONG = -106.926903
MY_EMAIL = 'bradydarren056@gmail.com'
DAILY_HOURS = 24

# 1. Fetch data from API's

def fetch_data():

    data_obj = []

    parameters = {
        'lat':MY_LAT,
        'lng':MY_LONG,
        'formatted':0
    }

    iss_response = requests.get(url = 'http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()

    ss_response = requests.get(url = 'https://api.sunrise-sunset.org/json',params=parameters)
    ss_response.raise_for_status()

    iss_data = iss_response.json()
    ss_data = ss_response.json()

    data_obj.append(iss_data)
    data_obj.append(ss_data)

    return data_obj

# 2. Convert time from UTC to CST in a 24hr format
# Find a simpler way to acheive the below function.
def time_conv(*utc_times):
    our_time = [] 
    
    # converting sunrise/sunset to CST from UTC
    for time in utc_times:
        total_time = time.split("T")[1].split(':')
        hours = int(total_time[0])
        hours = (hours - 6) % 24
        total_time[0] = str(hours)

    # MUST MOVE TO THE MAIN() FUNC
    # obtaining sunrise & sunset from fetch data function
    # sunrise = fetch_data()[1]['results']['sunrise']
    # sunset = fetch_data()[1]['results']['sunset']

time_conv('2025-03-21T13:07:16+00:00','2025-03-22T01:22:08+00:00')
# 2. Check and see if it is currently dark.
def is_dark(time):
    pass

# 3. If dark send email to email address telling notifiying us to look up. 
sunrise = fetch_data()[1]['results']['sunrise']
sunset = fetch_data()[1]['results']['sunset']
# print(sunrise)
# print(sunset)