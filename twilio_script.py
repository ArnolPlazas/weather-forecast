"""
************************************************************************
* Author = @ArnolPlazas                                               *
* Date = '21/06/2023'                                                  *
* Description = weather forecast with cell phone daily                   *
************************************************************************
"""
from tqdm import tqdm

from utils import request_wapi,get_forecast,create_df,send_message,get_date
from twilio_config import *



query = 'Bogotá'
api_key = API_KEY_WAPI

input_date= get_date()
response = request_wapi(api_key,query)

data = []

for i in tqdm(range(24),colour = 'blue'):

    data.append(get_forecast(response,i))


df_rain = create_df(data)
msj = "\nHi! \n\n\n Today's forecast is: "+ input_date +' in ' + query +' is : \n\n\n ' + str(df_rain)

message_id = send_message(msj, TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN, PHONE_NUMBER, MY_PHONE_NUMBER)