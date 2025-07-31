# SPDX-FileCopyrightText: 2024 Justin Myers
#
# SPDX-License-Identifier: MIT
"""
Board stub for BDMICRO VINA-D51
 - port: atmel-samd
 - board_id: bdmicro_vina_d51
 - NVM size: 256
 - Included modules: _asyncio, _bleio, _pixelmap, adafruit_bus_device, adafruit_pixelbuf, aesio, alarm, analogio, array, atexit, audiobusio, audiocore, audioio, audiomixer, audiomp3, binascii, bitbangio, bitmaptools, board, builtins, builtins.pow3, busdisplay, busio, busio.SPI, busio.UART, codeop, collections, countio, digitalio, displayio, epaperdisplay, errno, floppyio, fontio, fourwire, framebufferio, frequencyio, getpass, gifio, i2cdisplaybus, i2ctarget, io, jpegio, json, keypad, keypad.KeyMatrix, keypad.Keys, keypad.ShiftRegisterKeys, locale, math, max3421e, microcontroller, msgpack, neopixel_write, nvm, onewireio, os, os.getenv, paralleldisplaybus, ps2io, pulseio, pwmio, rainbowio, random, re, rgbmatrix, rotaryio, rtc, samd, sdcardio, select, sharpdisplay, spitarget, storage, struct, supervisor, synthio, sys, terminalio, tilepalettemapper, time, touchio, traceback, ulab, usb, usb_cdc, usb_hid, usb_midi, vectorio, warnings, watchdog, zlib
 - Frozen libraries: 
"""

# Imports
import busio
import microcontroller


# Board Info:
board_id: str


# Pins:
A0: microcontroller.Pin  # PA04
A1: microcontroller.Pin  # PA06
A10: microcontroller.Pin  # PB07
A11: microcontroller.Pin  # PC00
A2: microcontroller.Pin  # PA07
A3: microcontroller.Pin  # PB08
A4: microcontroller.Pin  # PB09
A5: microcontroller.Pin  # PC02
A6: microcontroller.Pin  # PC03
A7: microcontroller.Pin  # PB04
A8: microcontroller.Pin  # PB05
A9: microcontroller.Pin  # PB06
AUX_1: microcontroller.Pin  # PA17
AUX_UART_TX: microcontroller.Pin  # PA17
AUX_SPI_MOSI: microcontroller.Pin  # PA17
AUX_I2C_SDA: microcontroller.Pin  # PA17
ATW01_MOSI: microcontroller.Pin  # PA17
ESP01_TX: microcontroller.Pin  # PA17
AUX_10: microcontroller.Pin  # PC01
ATW01_IRQ: microcontroller.Pin  # PC01
AUX_11: microcontroller.Pin  # PC10
ATW01_GPIO_3: microcontroller.Pin  # PC10
AUX_12: microcontroller.Pin  # PC11
ATW01_GPIO_1: microcontroller.Pin  # PC11
AUX_3: microcontroller.Pin  # PA18
AUX_UART_RTS: microcontroller.Pin  # PA18
AUX_SPI_SS: microcontroller.Pin  # PA18
ATW01_SS: microcontroller.Pin  # PA18
ESP01_GPIO0: microcontroller.Pin  # PA18
AUX_4: microcontroller.Pin  # PC14
ATW01_RESET: microcontroller.Pin  # PC14
ESP01_RESET: microcontroller.Pin  # PC14
AUX_5: microcontroller.Pin  # PA19
AUX_UART_CTS: microcontroller.Pin  # PA19
AUX_SPI_MISO: microcontroller.Pin  # PA19
ATW01_MISO: microcontroller.Pin  # PA19
ESP01_GPIO2: microcontroller.Pin  # PA19
AUX_6: microcontroller.Pin  # PC15
ATW01_EN: microcontroller.Pin  # PC15
ESP01_CH_PD: microcontroller.Pin  # PC15
AUX_8: microcontroller.Pin  # PA16
AUX_UART_RX: microcontroller.Pin  # PA16
AUX_SPI_SCK: microcontroller.Pin  # PA16
AUX_I2C_SCL: microcontroller.Pin  # PA16
ATW01_SCK: microcontroller.Pin  # PA16
ESP01_RX: microcontroller.Pin  # PA16
AUX_9: microcontroller.Pin  # PA27
ATW01_WAKE: microcontroller.Pin  # PA27
D0: microcontroller.Pin  # PB31
D1: microcontroller.Pin  # PC16
D10: microcontroller.Pin  # PC13
D11: microcontroller.Pin  # PA14
D12: microcontroller.Pin  # PA15
D13: microcontroller.Pin  # PB12
D14: microcontroller.Pin  # PB13
D15: microcontroller.Pin  # PA21
I2S_SDO: microcontroller.Pin  # PA21
D16: microcontroller.Pin  # PA22
I2S_SDI: microcontroller.Pin  # PA22
D17: microcontroller.Pin  # PA20
I2S_FS_0: microcontroller.Pin  # PA20
D18: microcontroller.Pin  # PB16
I2S_SCK_0: microcontroller.Pin  # PB16
D19: microcontroller.Pin  # PB17
I2S_MCK_0: microcontroller.Pin  # PB17
D2: microcontroller.Pin  # PC17
D3: microcontroller.Pin  # PC18
D4: microcontroller.Pin  # PC19
D5: microcontroller.Pin  # PC20
D6: microcontroller.Pin  # PC21
D7: microcontroller.Pin  # PB18
D8: microcontroller.Pin  # PB19
D9: microcontroller.Pin  # PC12
DAC0: microcontroller.Pin  # PA02
DAC1: microcontroller.Pin  # PA05
I2C1_SCL: microcontroller.Pin  # PA12
SCL: microcontroller.Pin  # PA12
I2C1_SDA: microcontroller.Pin  # PA13
SDA: microcontroller.Pin  # PA13
LED_AUX: microcontroller.Pin  # PC26
LED_B: microcontroller.Pin  # PA23
LED_STATUS: microcontroller.Pin  # PA23
LED_G: microcontroller.Pin  # PB15
LED_QSPI: microcontroller.Pin  # PC07
LED_R: microcontroller.Pin  # PB14
LED_RX: microcontroller.Pin  # PC05
LED_TX: microcontroller.Pin  # PC06
RS485_RE: microcontroller.Pin  # PB01
RS485_RX: microcontroller.Pin  # PB03
RS485_TE: microcontroller.Pin  # PB00
RS485_TX: microcontroller.Pin  # PB02
SPI1_MISO: microcontroller.Pin  # PB23
MISO: microcontroller.Pin  # PB23
SPI1_MOSI: microcontroller.Pin  # PC27
MOSI: microcontroller.Pin  # PC27
SPI1_SCK: microcontroller.Pin  # PC28
SCK: microcontroller.Pin  # PC28
SPI1_SS: microcontroller.Pin  # PB22
SS: microcontroller.Pin  # PB22
UART1_CTS: microcontroller.Pin  # PC25
UART1_RTS: microcontroller.Pin  # PC24
UART1_RX: microcontroller.Pin  # PB24
UART1_TX: microcontroller.Pin  # PB25
UART2_RX: microcontroller.Pin  # PB20
RX: microcontroller.Pin  # PB20
I2C2_SCL: microcontroller.Pin  # PB20
UART2_TX: microcontroller.Pin  # PB21
TX: microcontroller.Pin  # PB21
I2C2_SDA: microcontroller.Pin  # PB21


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
