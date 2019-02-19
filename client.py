#!/usr/bin/env python3
# author : René Bolf xbolf@stud.fit.vutbr.cz
# IPK projekt http client openweathermap api
import socket
import sys
import json

if len(sys.argv) != 3:
    print("ERR: bad params", file = sys.stderr)
    sys.exit()

api_key = sys.argv[1]
location = sys.argv[2]

hostname = "api.openweathermap.org"
port = 80 #http
url_string = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key + "&units=metric"
request_command = "GET " + url_string + " HTTP/1.1\n" + "Host: " + hostname + "\n\n"
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is IPv4,  sock_stream is  TCP/IP
    s.connect((hostname,port)) #connect to server
    s.send(request_command.encode("utf-8"))#send request to server
    data = s.recv(4096) #size of buffer
    s.close() #close connection
except socket.error:
    print("ERROR: problem with socket", file = sys.stderr)
    sys.exit()

data_string = data.decode("utf-8") #decode from bytes to string
win_deg = data_string.find("deg") # we find deg in our string when deg is not found result is -1 when is found result is 0
if(data_string.find("HTTP/1.1 200 OK") == -1):
    print("ERROR: bad response ", file = sys.stderr)
    if(data_string.find("HTTP/1.1 401 Unauthorized") == 0):
        print("Code : 401 Unauthorized, non existing API_KEY", file = sys.stderr)
    if(data_string.find("HTTP/1.1 404 Not Found") == 0):
        print("Code : 404 Not Found, non existing city", file = sys.stderr)
    sys.exit()

data_split = data_string.split("POST\r\n\r\n")[1] #split http info because we want just json data
jsondata = json.loads(data_split)
print ("\ncity:",jsondata["name"],",",jsondata["sys"]["country"])
for weather in jsondata["weather"]:
    print("weather:",weather["description"])
print ("temperature:",jsondata["main"]["temp"],"°C")
print ("humidity:",jsondata["main"]["humidity"],"%")
print ("pressure:",jsondata["main"]["pressure"],"hPa")
print ("wind-speed:",jsondata["wind"]["speed"],"m/s")
if(win_deg == -1): #when result is -1 deg is not found , we set wind-deg to -
    print ("wind-deg: -")
else:
    print ("wind-deg:",jsondata["wind"]["deg"])
