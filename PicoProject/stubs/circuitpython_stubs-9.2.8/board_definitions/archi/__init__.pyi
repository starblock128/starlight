# SPDX-FileCopyrightText: 2024 Justin Myers
#
# SPDX-License-Identifier: MIT
"""
Board stub for Archi RP2040
 - port: raspberrypi
 - board_id: archi
 - NVM size: 4096
 - Included modules: _asyncio, _bleio, _eve, _pixelmap, adafruit_bus_device, adafruit_pixelbuf, aesio, alarm, analogbufio, analogio, array, atexit, audiobusio, audiocore, audiomixer, audiomp3, audiopwmio, binascii, bitbangio, bitmapfilter, bitmaptools, bitops, board, builtins, builtins.pow3, busdisplay, busio, busio.SPI, busio.UART, codeop, collections, countio, digitalio, displayio, epaperdisplay, errno, floppyio, fontio, fourwire, framebufferio, getpass, gifio, hashlib, i2cdisplaybus, i2ctarget, imagecapture, io, jpegio, json, keypad, keypad.KeyMatrix, keypad.Keys, keypad.ShiftRegisterKeys, keypad_demux, keypad_demux.DemuxKeyMatrix, locale, math, memorymap, microcontroller, msgpack, neopixel_write, nvm, onewireio, os, os.getenv, paralleldisplaybus, picodvi, pulseio, pwmio, qrio, rainbowio, random, re, rgbmatrix, rotaryio, rp2pio, rtc, sdcardio, select, sharpdisplay, storage, struct, supervisor, synthio, sys, terminalio, tilepalettemapper, time, touchio, traceback, ulab, usb, usb_cdc, usb_hid, usb_host, usb_midi, usb_video, vectorio, warnings, watchdog, zlib
 - Frozen libraries: adafruit_framebuf, adafruit_led_animation, adafruit_motor, adafruit_mpu6050, adafruit_pixel_framebuf, adafruit_register, adafruit_seesaw, neopixel, simpleio
"""

# Imports
import busio
import microcontroller


# Board Info:
board_id: str


# Pins:
GP0: microcontroller.Pin  # GPIO0
MPU_SDA: microcontroller.Pin  # GPIO0
GP1: microcontroller.Pin  # GPIO1
MPU_SCL: microcontroller.Pin  # GPIO1
GP2: microcontroller.Pin  # GPIO2
SDA: microcontroller.Pin  # GPIO2
GP3: microcontroller.Pin  # GPIO3
SCL: microcontroller.Pin  # GPIO3
GP4: microcontroller.Pin  # GPIO4
MISO: microcontroller.Pin  # GPIO4
GP5: microcontroller.Pin  # GPIO5
GP6: microcontroller.Pin  # GPIO6
SCK: microcontroller.Pin  # GPIO6
GP7: microcontroller.Pin  # GPIO7
MOSI: microcontroller.Pin  # GPIO7
GP8: microcontroller.Pin  # GPIO8
TX: microcontroller.Pin  # GPIO8
GP9: microcontroller.Pin  # GPIO9
RX: microcontroller.Pin  # GPIO9
B: microcontroller.Pin  # GPIO10
GP10: microcontroller.Pin  # GPIO10
GP11: microcontroller.Pin  # GPIO11
GP12: microcontroller.Pin  # GPIO12
GP13: microcontroller.Pin  # GPIO13
GP14: microcontroller.Pin  # GPIO14
GP15: microcontroller.Pin  # GPIO15
GP16: microcontroller.Pin  # GPIO16
GP17: microcontroller.Pin  # GPIO17
GP18: microcontroller.Pin  # GPIO18
D: microcontroller.Pin  # GPIO19
GP19: microcontroller.Pin  # GPIO19
MIC_DATA: microcontroller.Pin  # GPIO20
GP20: microcontroller.Pin  # GPIO20
MIC_CLOCK: microcontroller.Pin  # GPIO21
GP21: microcontroller.Pin  # GPIO21
BUZZER: microcontroller.Pin  # GPIO22
GP22: microcontroller.Pin  # GPIO22
A: microcontroller.Pin  # GPIO23
GP23: microcontroller.Pin  # GPIO23
NEOPIXEL: microcontroller.Pin  # GPIO24
GP24: microcontroller.Pin  # GPIO24
C: microcontroller.Pin  # GPIO25
GP25: microcontroller.Pin  # GPIO25
GP26: microcontroller.Pin  # GPIO26
A0: microcontroller.Pin  # GPIO26
GP27: microcontroller.Pin  # GPIO27
A1: microcontroller.Pin  # GPIO27
GP28: microcontroller.Pin  # GPIO28
A2: microcontroller.Pin  # GPIO28
GP29: microcontroller.Pin  # GPIO29
A3: microcontroller.Pin  # GPIO29


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


# Unmapped:
#   none
