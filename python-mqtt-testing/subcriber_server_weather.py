from machine import Pin
from time import localtime, sleep
from weatherbit.api import Api
import threading

api_key = "key"
lat = 49.44684
lon = 8.357229999999959
api = Api(api_key)
api.set_granularity('daily')

class MQTT_subcriber(): #Class for controlling the ESP
    pass
def auto_water(): #This function looks what the forecast says and let flow enough water for everything
    pass
def manuell(): #function for manuell control e.g. if it is not enough water
    pass
threading.Thread(target = auto_water).start()
threading.Thread(target = manuell).start()