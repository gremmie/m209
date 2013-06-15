# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""This module contains routines to generate key lists."""

import collections
import random

from .key_list import KeyList
from ..converter import M209
from .. import M209Error
from ..data import KEY_WHEEL_DATA


# Maximum number of attempts to generate valid settings before giving up and
# raising a M209Error:
MAX_ATTEMPTS = 128

# Total number of pins on all 6 wheels:
TOTAL_PINS = sum(len(letters) for letters, _ in KEY_WHEEL_DATA)


def generate_key_list(indicator):
    """Create a key list at random with the given indicator.

    The procedure used is based upon manuals for the M-209 as found online:

    [1]: TM-11-380, War Department, Technical Manual, Converter M-209, April 27,
         1942.
         http://maritime.org/tech/csp1500inst.htm

    [2]: TM-11-380, War Department, Technical Manual, Converter M-209, M-209-A,
         M-209-B (cipher) 17 March, 1944.
         http://www.ilord.com/m209manual.html

    Page 1 of reference [2] says: "This manual supercedes TM-11-380, 27 April
    1942, and TM-11-380B, 20 September 1943."

    """
    lugs = generate_lugs()
    pin_list = generate_pin_list()
    letter_check = generate_letter_check(lugs=lugs, pin_list=pin_list)

    return KeyList(indicator=indicator, lugs=lugs, pin_list=pin_list,
            letter_check=letter_check)


def generate_lugs():
    """Return random lug settings based on Army procedure."""
    return ''


def generate_pin_list():
    """Return a random pin list based on Army procedure."""

    cards = ['R'] * 78
    cards.extend(['L'] * (156 - len(cards)))

    for n in range(MAX_ATTEMPTS):
        random.shuffle(cards)
        deck = collections.deque(cards)
        pin_list = []
        for letters, _ in KEY_WHEEL_DATA:
            pins = [c for c in letters if 'R' == deck.pop()]
            pin_list.append(''.join(pins))

        if pin_list_check(pin_list):
            break
    else:
        raise M209Error("generate_pin_list: too many attempts")

    return pin_list


def generate_letter_check(lugs, pin_list):
    """Return a letter check string for the given pin list and lug settings."""

    m_209 = M209(lugs, pin_list)
    m_209.set_key_wheels('A' * 6)
    return m_209.encrypt('A' * 26, group=True)


def pin_list_check(pin_list):
    """Returns True if the supplied pin list meets Army procedure criteria.

    To pass the check, the number of effective pins must be between 40-60%.
    Furthermore, there cannot be more than 6 consecutive effective or
    non-effective pins on any wheel.

    """
    num_eff = sum(len(s) for s in pin_list)
    ratio = num_eff / TOTAL_PINS

    if not (0.4 <= ratio <= 0.6):
        return False

    # Check for more than 6 consecutive effective pins on a wheel
    # TODO: not all letters are on every wheel

    for pins in pin_list:
        run = 0
        for i in range(len(pins) - 1):
            if ord(pins[i]) + 1 == ord(pins[i + 1]):
                run = 2 if run == 0 else run + 1
            else:
                run = 0
            if run >= 7:
                return False

    # Check for more than 6 consecutive ineffective pins on a wheel
    # TODO: not all letters are on every wheel

    for pins in pin_list:
        x = 'A'
        for y in pins:
            if ord(y) - ord(x) >= 8:
                return False
            x = y

    return True
