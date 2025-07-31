"""Board specific pin names

Common container for board base pin names. These will vary from board to
board so don't expect portability when using this module.

Another common use of this module is to use serial communication buses with
the default pins and settings.  For more information about serial communcication
in CircuitPython, see the :mod:`busio`.

For more information regarding the typical usage of :py:mod:`board`, refer to the `CircuitPython
Essentials Learn guide
<https://learn.adafruit.com/circuitpython-essentials/circuitpython-pins-and-modules>`_

.. warning:: The board module varies by board. The APIs documented here may or may not be
             available on a specific board."""

from __future__ import annotations

import busio

board_id: str
"""Board ID string. The unique identifier for the board model in
circuitpython, as well as on circuitpython.org.
Example: "hallowing_m0_express"."""

def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...

def SPI() -> busio.SPI:
    """Returns the `busio.SPI` object for the board's designated SPI bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.SPI`.
    """
    ...

def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """
    ...
# Raspberry Pi Pico Pin Definitions
from microcontroller import Pin  # 引用 Pin 類型

GP0: Pin
GP1: Pin
GP2: Pin
GP3: Pin
GP4: Pin
GP5: Pin
GP6: Pin
GP7: Pin
GP8: Pin
GP9: Pin
GP10: Pin
GP11: Pin
GP12: Pin
GP13: Pin
GP14: Pin
GP15: Pin
GP16: Pin
GP17: Pin
GP18: Pin
GP19: Pin
GP20: Pin
GP21: Pin
GP22: Pin
GP23: Pin
GP24: Pin
GP25: Pin
GP26: Pin
GP27: Pin
GP28: Pin

LED: Pin
