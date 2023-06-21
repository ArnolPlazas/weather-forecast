import pandas as pd
from twilio.rest import Client
from datetime import datetime
import requests

def get_date():

    input_date = datetime.now()
    input_date = input_date.strftime("%Y-%m-%d")

    return input_date

def request_wapi(api_key,query):

    weather_url = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+query+'&days=1&aqi=no&alerts=no'

    try :
        response = requests.get(weather_url).json()
    except Exception as e:
        print(e)

    return response

def get_forecast(response, i):
    date = response['forecast']['forecastday'][0]['hour'][i]['time'].split()[0]
    hour = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0])
    condition = response['forecast']['forecastday'][0]['hour'][i]['condition']['text']
    temperature = response['forecast']['forecastday'][0]['hour'][i]['temp_c']
    rain = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain']
    prob_rain = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain']

    return date, hour, condition, temperature, rain, prob_rain

def create_df(data):
    columns = ['date', 'hour', 'condition', 'temperature', 'rain', 'prob_rain']
    df_forecast = pd.DataFrame(data=data, columns=columns)
    df_rain = df_forecast[(df_forecast['rain'] == 1) & (df_forecast['hour']>6) & (df_forecast['hour']< 22)] 
    df_rain = df_rain[['hour', 'condition']]
    df_rain.set_index('hour', inplace=True)

    return df_rain

def send_message(msj, TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN, PHONE_NUMBER, MY_PHONE_NUMBER):

    account_sid = TWILIO_ACCOUNT_SID 
    auth_token = TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=msj,
                        from_=PHONE_NUMBER,
                        to=MY_PHONE_NUMBER
                    )

    return message.sid