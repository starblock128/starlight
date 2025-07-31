# SPDX-FileCopyrightText: 2024 Justin Myers
#
# SPDX-License-Identifier: MIT
"""
Board stub for LoC BeR M4 base board
 - port: atmel-samd
 - board_id: loc_ber_m4_base_board
 - NVM size: 256
 - Included modules: alarm, analogio, array, board, builtins, busio, busio.SPI, busio.UART, collections, digitalio, math, microcontroller, neopixel_write, nvm, onewireio, os, ps2io, pwmio, rainbowio, random, rotaryio, rtc, samd, spitarget, storage, struct, supervisor, sys, time, touchio, usb_cdc, usb_hid, usb_midi, watchdog
 - Frozen libraries: 
"""

# Imports
import busio
import microcontroller


# Board Info:
board_id: str


# Pins:
A0: microcontroller.Pin  # PA02
A1: microcontroller.Pin  # PA05
A2: microcontroller.Pin  # PB08
A3: microcontroller.Pin  # PB09
A4: microcontroller.Pin  # PA04
A5: microcontroller.Pin  # PA06
D0: microcontroller.Pin  # PA16
RX: microcontroller.Pin  # PA16
D1: microcontroller.Pin  # PA17
TX: microcontroller.Pin  # PA17
D2: microcontroller.Pin  # PA07
D3: microcontroller.Pin  # PB22
D4: microcontroller.Pin  # PA14
D5: microcontroller.Pin  # PA15
D7: microcontroller.Pin  # PA18
D9: microcontroller.Pin  # PA19
D10: microcontroller.Pin  # PA20
D11: microcontroller.Pin  # PA21
D12: microcontroller.Pin  # PA23
D13: microcontroller.Pin  # PA22
SDA: microcontroller.Pin  # PA12
SCL: microcontroller.Pin  # PA13
SCK: microcontroller.Pin  # PA01
MOSI: microcontroller.Pin  # PA00
MISO: microcontroller.Pin  # PB23
APA102_MOSI: microcontroller.Pin  # PB03
APA102_SCK: microcontroller.Pin  # PB02
SCK_2: microcontroller.Pin  # PB10
MOSI_2: microcontroller.Pin  # PA08
MISO_2: microcontroller.Pin  # PA09
CS_2: microcontroller.Pin  # PB11
WP_2: microcontroller.Pin  # PA10
HOLD_2: microcontroller.Pin  # PA11


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
