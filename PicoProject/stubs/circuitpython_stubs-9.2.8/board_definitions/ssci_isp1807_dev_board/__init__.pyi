# SPDX-FileCopyrightText: 2024 Justin Myers
#
# SPDX-License-Identifier: MIT
"""
Board stub for SSCI ISP1807 Dev Board
 - port: nordic
 - board_id: ssci_isp1807_dev_board
 - NVM size: 8192
 - Included modules: _asyncio, _bleio, _pixelmap, adafruit_bus_device, adafruit_pixelbuf, aesio, alarm, analogio, array, atexit, audiobusio, audiocore, audiomixer, audiomp3, audiopwmio, binascii, bitbangio, bitmapfilter, bitmaptools, board, builtins, builtins.pow3, busdisplay, busio, busio.SPI, busio.UART, codeop, collections, countio, digitalio, displayio, epaperdisplay, errno, fontio, fourwire, framebufferio, getpass, gifio, i2cdisplaybus, io, jpegio, json, keypad, keypad.KeyMatrix, keypad.Keys, keypad.ShiftRegisterKeys, keypad_demux, keypad_demux.DemuxKeyMatrix, locale, math, memorymap, microcontroller, msgpack, neopixel_write, nvm, onewireio, os, os.getenv, paralleldisplaybus, pulseio, pwmio, rainbowio, random, re, rgbmatrix, rotaryio, rtc, sdcardio, select, sharpdisplay, storage, struct, supervisor, synthio, sys, terminalio, tilepalettemapper, time, touchio, traceback, ulab, usb_cdc, usb_hid, usb_midi, vectorio, warnings, watchdog, zlib
 - Frozen libraries: 
"""

# Imports
import busio
import microcontroller


# Board Info:
board_id: str


# Pins:
P0_02: microcontroller.Pin  # P0_02
P0_27: microcontroller.Pin  # P0_27
P0_03: microcontroller.Pin  # P0_03
P0_15: microcontroller.Pin  # P0_15
P0_05: microcontroller.Pin  # P0_05
P0_04: microcontroller.Pin  # P0_04
P0_06: microcontroller.Pin  # P0_06
P0_07: microcontroller.Pin  # P0_07
P0_08: microcontroller.Pin  # P0_08
P0_13: microcontroller.Pin  # P0_13
P0_17: microcontroller.Pin  # P0_17
P0_25: microcontroller.Pin  # P0_25
P0_31: microcontroller.Pin  # P0_31
P0_11: microcontroller.Pin  # P0_11
P0_30: microcontroller.Pin  # P0_30
P0_19: microcontroller.Pin  # P0_19
P0_29: microcontroller.Pin  # P0_29
P0_23: microcontroller.Pin  # P0_23
P0_28: microcontroller.Pin  # P0_28
P0_09: microcontroller.Pin  # P0_09
P0_12: microcontroller.Pin  # P0_12
P0_10: microcontroller.Pin  # P0_10
P0_14: microcontroller.Pin  # P0_14
P0_26: microcontroller.Pin  # P0_26
A0: microcontroller.Pin  # P0_02
A1: microcontroller.Pin  # P0_03
A2: microcontroller.Pin  # P0_04
A3: microcontroller.Pin  # P0_05
A5: microcontroller.Pin  # P0_29
A6: microcontroller.Pin  # P0_30
A7: microcontroller.Pin  # P0_31
LED: microcontroller.Pin  # P0_06
BUTTON: microcontroller.Pin  # P1_06
SDA: microcontroller.Pin  # P0_19
SCL: microcontroller.Pin  # P0_23
MOSI: microcontroller.Pin  # P0_10
MISO: microcontroller.Pin  # P0_12
SCK: microcontroller.Pin  # P0_14
TX: microcontroller.Pin  # P0_11
RX: microcontroller.Pin  # P0_25


# Members:
def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """

def SPI() -> busio.SPI:
    """Returns the `busio.SPI` object for the board's designated SPI bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.SPI`.
    """

def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """


# Unmapped:
#   none
