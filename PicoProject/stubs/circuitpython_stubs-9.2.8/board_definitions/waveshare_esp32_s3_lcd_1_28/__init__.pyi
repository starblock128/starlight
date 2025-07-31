# SPDX-FileCopyrightText: 2024 Justin Myers
#
# SPDX-License-Identifier: MIT
"""
Board stub for Waveshare ESP32S3 LCD 1.28
 - port: espressif
 - board_id: waveshare_esp32_s3_lcd_1_28
 - NVM size: 8192
 - Included modules: _asyncio, _bleio, _eve, _pixelmap, adafruit_bus_device, adafruit_pixelbuf, aesio, alarm, analogbufio, analogio, array, atexit, audiobusio, audiocore, audiomixer, audiomp3, binascii, bitbangio, bitmapfilter, bitmaptools, board, builtins, builtins.pow3, busdisplay, busio, busio.SPI, busio.UART, canio, codeop, collections, countio, digitalio, displayio, dualbank, epaperdisplay, errno, espidf, espnow, espulp, fontio, fourwire, framebufferio, frequencyio, getpass, gifio, hashlib, i2cdisplaybus, io, ipaddress, jpegio, json, keypad, keypad.KeyMatrix, keypad.Keys, keypad.ShiftRegisterKeys, keypad_demux, keypad_demux.DemuxKeyMatrix, locale, math, max3421e, mdns, memorymap, microcontroller, msgpack, neopixel_write, nvm, onewireio, os, os.getenv, paralleldisplaybus, ps2io, pulseio, pwmio, rainbowio, random, re, rgbmatrix, rotaryio, rtc, sdcardio, sdioio, select, sharpdisplay, socketpool, socketpool.socketpool.AF_INET6, ssl, storage, struct, supervisor, synthio, sys, terminalio, tilepalettemapper, time, touchio, traceback, ulab, usb, vectorio, warnings, watchdog, wifi, zlib
 - Frozen libraries: 
"""

# Imports
import busio
import displayio
import microcontroller


# Board Info:
board_id: str


# Pins:
IO36: microcontroller.Pin  # GPIO36
IO35: microcontroller.Pin  # GPIO35
IO34: microcontroller.Pin  # GPIO34
IO33: microcontroller.Pin  # GPIO33
IO21: microcontroller.Pin  # GPIO21
IO18: microcontroller.Pin  # GPIO18
IO17: microcontroller.Pin  # GPIO17
IO16: microcontroller.Pin  # GPIO16
IO15: microcontroller.Pin  # GPIO15
IO14: microcontroller.Pin  # GPIO14
IO46: microcontroller.Pin  # GPIO46
IO45: microcontroller.Pin  # GPIO45
IO42: microcontroller.Pin  # GPIO42
IO41: microcontroller.Pin  # GPIO41
IO39: microcontroller.Pin  # GPIO39
IO38: microcontroller.Pin  # GPIO38
IO37: microcontroller.Pin  # GPIO37
IO13: microcontroller.Pin  # GPIO13
IO0: microcontroller.Pin  # GPIO0
IO2: microcontroller.Pin  # GPIO2
IO3: microcontroller.Pin  # GPIO3
IO4: microcontroller.Pin  # GPIO4
IO5: microcontroller.Pin  # GPIO5
BOOT: microcontroller.Pin  # GPIO0
BUTTON0: microcontroller.Pin  # GPIO0
BAT_ADC: microcontroller.Pin  # GPIO1
SCL: microcontroller.Pin  # GPIO7
SDA: microcontroller.Pin  # GPIO6
SCK: microcontroller.Pin  # GPIO10
MOSI: microcontroller.Pin  # GPIO11
MISO: microcontroller.Pin  # GPIO13
LCD_DC: microcontroller.Pin  # GPIO8
LCD_CS: microcontroller.Pin  # GPIO9
LCD_RST: microcontroller.Pin  # GPIO12
LCD_BACKLIGHT: microcontroller.Pin  # GPIO40
IMU_INT1: microcontroller.Pin  # GPIO47
IMU_INT2: microcontroller.Pin  # GPIO48
RX: microcontroller.Pin  # GPIO44
TX: microcontroller.Pin  # GPIO43


# Members:
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """

def SPI() -> busio.SPI:
    """Returns the `busio.SPI` object for the board's designated SPI bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.SPI`.
    """

def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """

"""Returns the `displayio.Display` object for the board's built in display.
The object created is a singleton, and uses the default parameter values for `displayio.Display`.
"""
DISPLAY: displayio.Display


# Unmapped:
#   none
