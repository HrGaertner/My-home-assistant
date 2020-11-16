# My-home-assistant
Configuration and Introduction to my own devices in my home assistant installation

If you're intressting in using parts of this but don't get it because my documentation is not helpful just open an issue

##Tools I use
Node MCU ESP8266
[Home Assistant](https://hass.io)
[esphome](https://esphome.io) (as plugin in my home assistant)
Raspberry Pi (For my HA installation and later hopefully [rhasspy](https://github.com/rhasspy))

## Devices

###Garden
This devices is connected to two relais and controls two Gardena 24V Magnetic valve.
For configuring i use [esphome](https://esphome.io) the relais are connected to the GPIOs D1 and D2 on the Node MCU ESP8266  
Just take my configuration file for esphome and insert wifi Password and SSID as well as the Fallback password (If the esp can not connect to the wifi)

### My room
This is also just a configuration file for esphome. Change Password, Wifi and Fallback wifi.
Configured is a light stripe on D1-3 connect those pins to three transistors and connect them on the one side to you're voltage and on the other site to one of the stripes colors.
It also configures the status light on the Esp.
It expects to have a DHT11 on D4 (and GND, 3V)

### [Presence Detection](https://www.home-assistant.io/integrations/ubus/)