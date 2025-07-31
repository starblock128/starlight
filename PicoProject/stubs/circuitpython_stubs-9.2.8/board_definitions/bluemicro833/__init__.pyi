# SPDX-FileCopyrightText: 2024 Justin Myers
#
# SPDX-License-Identifier: MIT
"""
Board stub for BlueMicro833
 - port: nordic
 - board_id: bluemicro833
 - NVM size: 8192
 - Included modules: _bleio, adafruit_pixelbuf, alarm, analogio, array, audiocore, board, builtins, busio, busio.SPI, busio.UART, collections, digitalio, keypad, keypad.KeyMatrix, keypad.Keys, keypad.ShiftRegisterKeys, math, microcontroller, neopixel_write, os, pulseio, pwmio, rainbowio, random, rotaryio, rtc, storage, struct, supervisor, sys, time, usb_cdc, usb_hid, usb_midi
 - Frozen libraries: 
"""

# Imports
import busio
import microcontroller


# Board Info:
board_id: str


# Pins:
P0_02: microcontroller.Pin  # P0_02
P0_03: microcontroller.Pin  # P0_03
P0_04: microcontroller.Pin  # P0_04
P0_05: microcontroller.Pin  # P0_05
P0_06: microcontroller.Pin  # P0_06
P0_07: microcontroller.Pin  # P0_07
P0_08: microcontroller.Pin  # P0_08
P0_09: microcontroller.Pin  # P0_09
P0_10: microcontroller.Pin  # P0_10
P0_11: microcontroller.Pin  # P0_11
P0_12: microcontroller.Pin  # P0_12
P0_13: microcontroller.Pin  # P0_13
P0_14: microcontroller.Pin  # P0_14
P0_15: microcontroller.Pin  # P0_15
P0_16: microcontroller.Pin  # P0_16
P0_17: microcontroller.Pin  # P0_17
P0_19: microcontroller.Pin  # P0_19
P0_20: microcontroller.Pin  # P0_20
P0_21: microcontroller.Pin  # P0_21
P0_22: microcontroller.Pin  # P0_22
P0_23: microcontroller.Pin  # P0_23
P0_24: microcontroller.Pin  # P0_24
P0_25: microcontroller.Pin  # P0_25
P0_26: microcontroller.Pin  # P0_26
P0_27: microcontroller.Pin  # P0_27
P0_28: microcontroller.Pin  # P0_28
P0_29: microcontroller.Pin  # P0_29
P0_30: microcontroller.Pin  # P0_30
P0_31: microcontroller.Pin  # P0_31
P1_00: microcontroller.Pin  # P1_00
P1_01: microcontroller.Pin  # P1_01
P1_02: microcontroller.Pin  # P1_02
P1_03: microcontroller.Pin  # P1_03
P1_04: microcontroller.Pin  # P1_04
P1_05: microcontroller.Pin  # P1_05
P1_06: microcontroller.Pin  # P1_06
P1_07: microcontroller.Pin  # P1_07
P1_08: microcontroller.Pin  # P1_08
P1_09: microcontroller.Pin  # P1_09
A0: microcontroller.Pin  # P0_02
A1: microcontroller.Pin  # P0_03
A2: microcontroller.Pin  # P0_04
A3: microcontroller.Pin  # P0_05
A4: microcontroller.Pin  # P0_28
A5: microcontroller.Pin  # P0_29
A6: microcontroller.Pin  # P0_30
A7: microcontroller.Pin  # P0_31
SDA: microcontroller.Pin  # P0_15
SCL: microcontroller.Pin  # P0_17
RX: microcontroller.Pin  # P0_08
TX: microcontroller.Pin  # P0_06
MISO: microcontroller.Pin  # P0_03
MOSI: microcontroller.Pin  # P0_28
SCK: microcontroller.Pin  # P1_05
LED1: microcontroller.Pin  # P1_04
LED2: microcontroller.Pin  # P0_25
RED_LED: microcontroller.Pin  # P1_04
BLUE_LED: microcontroller.Pin  # P0_25
VCC_ON: microcontroller.Pin  # P0_12
NEOPIXEL: microcontroller.Pin  # P0_07


# Members:
def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """

def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """

def SPI() -> busio.SPI:
    """Returns the `busio.SPI` object for the board's designated SPI bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.SPI`.
    """


# Unmapped:
#   none
