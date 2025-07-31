# SPDX-FileCopyrightText: Copyright (c) 2025 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_fruitjam.peripherals`
================================================================================

Hardware peripherals for Adafruit Fruit Jam


* Author(s): Tim Cocks

Implementation Notes
--------------------

**Hardware:**

* `Adafruit Fruit Jam <https://www.adafruit.com/product/6200>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice

"""

import adafruit_tlv320
import audiobusio
import board
import displayio
import framebufferio
import picodvi
import supervisor
from digitalio import DigitalInOut, Direction, Pull
from neopixel import NeoPixel

__version__ = "0.4.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FruitJam.git"

VALID_DISPLAY_SIZES = {(360, 200), (720, 400), (320, 240), (640, 480)}
COLOR_DEPTH_LUT = {
    360: 16,
    320: 16,
    720: 8,
    640: 8,
}


def request_display_config(width, height, color_depth=None):
    """
    Request a display size configuration. If the display is un-initialized,
    or is currently using a different configuration it will be initialized
    to the requested width and height.

    This function will set the initialized display to ``supervisor.runtime.display``

    :param width: The width of the display in pixels.
    :param height: The height of the display in pixels.
    :param color_depth: The color depth of the display in bits.
      Valid values are 1, 2, 4, 8, 16, 32. Larger resolutions must use
      smaller color_depths due to RAM limitations. Default color_depth for
      720 and 640 width is 8, and default color_depth for 320 and 360 width
      is 16.
    :return: None
    """
    if (width, height) not in VALID_DISPLAY_SIZES:
        raise ValueError(f"Invalid display size. Must be one of: {VALID_DISPLAY_SIZES}")

    # if user does not specify a requested color_depth
    if color_depth is None:
        # use the maximum color depth for given width
        color_depth = COLOR_DEPTH_LUT[width]

    requested_config = (width, height, color_depth)

    if requested_config != get_display_config():
        displayio.release_displays()
        fb = picodvi.Framebuffer(
            width,
            height,
            clk_dp=board.CKP,
            clk_dn=board.CKN,
            red_dp=board.D0P,
            red_dn=board.D0N,
            green_dp=board.D1P,
            green_dn=board.D1N,
            blue_dp=board.D2P,
            blue_dn=board.D2N,
            color_depth=color_depth,
        )
        supervisor.runtime.display = framebufferio.FramebufferDisplay(fb)


def get_display_config():
    """
    Get the current display size configuration.

    :return: display_config: Tuple containing the width, height, and color_depth of the display
      in pixels and bits respectively.
    """

    display = supervisor.runtime.display
    if display is not None:
        display_config = (display.width, display.height, display.framebuffer.color_depth)
        return display_config
    else:
        return (None, None, None)


class Peripherals:
    """Peripherals Helper Class for the FruitJam Library


    Attributes:
        neopixels (NeoPxiels): The NeoPixels on the Fruit Jam board.
            See https://circuitpython.readthedocs.io/projects/neopixel/en/latest/api.html
    """

    def __init__(self):
        self.neopixels = NeoPixel(board.NEOPIXEL, 5)

        self._buttons = []
        for pin in (board.BUTTON1, board.BUTTON2, board.BUTTON3):
            switch = DigitalInOut(pin)
            switch.direction = Direction.INPUT
            switch.pull = Pull.UP
            self._buttons.append(switch)

        i2c = board.I2C()
        self._dac = adafruit_tlv320.TLV320DAC3100(i2c)

        # set sample rate & bit depth
        self._dac.configure_clocks(sample_rate=11030, bit_depth=16)

        # use headphones
        self._dac.headphone_output = True
        self._dac.headphone_volume = -15  # dB

        self._audio = audiobusio.I2SOut(board.I2S_BCLK, board.I2S_WS, board.I2S_DIN)

    @property
    def button1(self) -> bool:
        """
        Return whether Button 1 is pressed
        """
        return not self._buttons[0].value

    @property
    def button2(self) -> bool:
        """
        Return whether Button 2 is pressed
        """
        return not self._buttons[1].value

    @property
    def button3(self) -> bool:
        """
        Return whether Button 3 is pressed
        """
        return not self._buttons[2].value

    @property
    def any_button_pressed(self) -> bool:
        """
        Return whether any button is pressed
        """
        return True in [button.value for (i, button) in enumerate(self._buttons)]

    @property
    def dac(self):
        return self._dac

    @property
    def audio(self):
        return self._audio
