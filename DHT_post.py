import time
import Adafruit_DHT
import requests

url = "http://172.20.10.2:8080/save/temp"
sensor = Adafruit_DHT.DHT11
pin = 14

def postDATA() :
    h, t = Adafruit_DHT.read_retry(sensor,pin)
    if h is not None and t is not None :
        DHT = {
            "temperature" : float(t),
            "humidity" : float(h)
            }
        post = requests.post(url, json = DHT, timeout = 5)
        print(post.text)
        
    else :
        print('Read Error')
    

try:
    while True:
        postDATA()

except Exception as e:
    print(e)
