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
        'formatted':1
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

def time_conv(*utc_times):
    our_time = [] 

    for time in utc_times: 
        result = time.split(":")
        for section in result:
            num_time = int(section)
            our_time.append(num_time)

    if our_time[0] - 6 < 0:
        abs_time = abs(our_time[0] - 6)
        our_time[0] = DAILY_HOURS - abs_time

    print(our_time)
    
    for t in our_time:
        print(t) 
    #     string_time = str(t)
    #     our_time.append(string_time)

    
    # MUST MOVE TO THE MAIN() FUNC
    # obtaining sunrise & sunset from fetch data function
    # sunrise = fetch_data()[1]['results']['sunrise']
    # sunset = fetch_data()[1]['results']['sunset']

    # return(utc_times)   
     
    # converting sunrise/sunset to CST from UTC

time_conv('1:00:00')
    

# 2. Check and see if it is currently dark.

# 3. If dark send email to email address telling notifiying us to look up. 
