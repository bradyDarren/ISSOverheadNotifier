import requests
from datetime import datetime
import smtplib

# setting coordinates
MY_LAT = 38.545502
MY_LONG = -106.926903
MY_EMAIL = 'bradydarren056@gmail.com'
PASSWORD = "ayae lpxi ubzt vhfh"
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
    our_time = {}
    
    # converting sunrise/sunset to CST from UTC
    for time in utc_times:
        total_time = time.split("T")[1].split(':')
        hours = (int(total_time[0])- 6) % 24
        if hours < 8:
            our_time['sunrise'] = {'hr':hours,'min':int(total_time[1])}
        else: 
            our_time['sunset'] = {'hr':hours,'min':int(total_time[1])}

        # total_time[0] = str(hours)
        # total_time = total_time[:-2]
    return our_time 

# 2. Check and see if it is currently dark.
def is_dark(rise, set, time):
    if rise > time or time > set: 
        dark = True
    else:
        dark = False
    return dark

# 3. If dark send email to email address telling notifiying us to look up. 
def notify(night): 
    if night: 
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection: 
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            subject = 'THE ISS IS VISIBLE IN THE NIGHT SKY!!!!'
            body = 'Look Up!!'
            message = f'Subject:{subject}\n\n{body}'
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=message.encode('utf-8'))
# main function
def main():
    pass
 
