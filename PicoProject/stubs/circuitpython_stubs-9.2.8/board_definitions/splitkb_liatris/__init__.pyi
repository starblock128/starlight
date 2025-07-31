# SPDX-FileCopyrightText: 2024 Justin Myers
#
# SPDX-License-Identifier: MIT
"""
Board stub for splitkb.com Liatris
 - port: raspberrypi
 - board_id: splitkb_liatris
 - NVM size: 4096
 - Included modules: _asyncio, _bleio, _pixelmap, adafruit_bus_device, adafruit_pixelbuf, aesio, alarm, analogbufio, analogio, array, atexit, audiobusio, audiocore, audiomixer, audiomp3, audiopwmio, binascii, bitbangio, bitmapfilter, bitmaptools, bitops, board, builtins, builtins.pow3, busdisplay, busio, busio.SPI, busio.UART, codeop, collections, countio, digitalio, displayio, epaperdisplay, errno, floppyio, fontio, fourwire, framebufferio, getpass, gifio, hashlib, i2cdisplaybus, i2ctarget, imagecapture, io, jpegio, json, keypad, keypad.KeyMatrix, keypad.Keys, keypad.ShiftRegisterKeys, keypad_demux, keypad_demux.DemuxKeyMatrix, locale, math, memorymap, microcontroller, msgpack, neopixel_write, nvm, onewireio, os, os.getenv, paralleldisplaybus, pulseio, pwmio, qrio, rainbowio, random, re, rgbmatrix, rotaryio, rp2pio, rtc, sdcardio, select, sharpdisplay, storage, struct, supervisor, synthio, sys, terminalio, tilepalettemapper, time, touchio, traceback, ulab, usb, usb_cdc, usb_hid, usb_host, usb_midi, usb_video, vectorio, warnings, watchdog, zlib
 - Frozen libraries: 
"""

# Imports
import busio
import microcontroller


# Board Info:
board_id: str


# Pins:
D0: microcontroller.Pin  # GPIO0
TX: microcontroller.Pin  # GPIO0
D1: microcontroller.Pin  # GPIO1
RX: microcontroller.Pin  # GPIO1
D2: microcontroller.Pin  # GPIO2
SDA: microcontroller.Pin  # GPIO2
D3: microcontroller.Pin  # GPIO3
SCL: microcontroller.Pin  # GPIO3
D4: microcontroller.Pin  # GPIO4
D5: microcontroller.Pin  # GPIO5
D6: microcontroller.Pin  # GPIO6
D7: microcontroller.Pin  # GPIO7
D8: microcontroller.Pin  # GPIO8
D9: microcontroller.Pin  # GPIO9
D29: microcontroller.Pin  # GPIO29
A3: microcontroller.Pin  # GPIO29
D28: microcontroller.Pin  # GPIO28
A2: microcontroller.Pin  # GPIO28
D27: microcontroller.Pin  # GPIO27
A1: microcontroller.Pin  # GPIO27
D26: microcontroller.Pin  # GPIO26
A0: microcontroller.Pin  # GPIO26
D22: microcontroller.Pin  # GPIO22
SCK: microcontroller.Pin  # GPIO22
D20: microcontroller.Pin  # GPIO20
MISO: microcontroller.Pin  # GPIO20
D23: microcontroller.Pin  # GPIO23
MOSI: microcontroller.Pin  # GPIO23
D21: microcontroller.Pin  # GPIO21
D12: microcontroller.Pin  # GPIO12
D13: microcontroller.Pin  # GPIO13
D14: microcontroller.Pin  # GPIO14
D15: microcontroller.Pin  # GPIO15
D16: microcontroller.Pin  # GPIO16
NEOPIXEL: microcontroller.Pin  # GPIO25
VBUS_SENSE: microcontroller.Pin  # GPIO19
POWER_LED: microcontroller.Pin  # GPIO24


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
