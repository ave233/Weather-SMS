from twilio.rest import TwilioRestClient
import requests, json

# Set up the twilio rest client based off your account details (account SID, auth token)
client = TwilioRestClient('account SID', 'auth token')

# Make API call to openweathermap.org
r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=5119235&APPID=60a661c2450f5f33408f1b04017938aa')
data = r.json()

# Pull whatever data you want from the api call to open weather map.
# I've decided to take the description and temperature.
description = data['weather'][0]['description']

# Convert Kelvin to Farenheit
kelvin = data['main']['temp']
celsius = kelvin - 273.15
farenheit = (celsius * 1.8) + 32

# Declare message body
message_body = "The weather in Great Neck Estates is currently " + str(farenheit) + " degrees Farenheit."
message_body = message_body + " The description is: " + str(description)

# Create message body and send sms based on the number you would like to send to
# and your given Twilio phone number.
client.messages.create(to="+123456789", from_="+15162532484", body=message_body)
