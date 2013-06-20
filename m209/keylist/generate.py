# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""This module contains routines to generate key lists."""

import collections
import itertools
import random

from .key_list import KeyList
from ..converter import M209
from .. import M209Error
from ..data import KEY_WHEEL_DATA
from .data import GROUP_A, GROUP_B


# Maximum number of attempts to generate valid settings before giving up and
# raising a M209Error:
MAX_ATTEMPTS = 128

# Total number of pins on all 6 wheels:
TOTAL_PINS = sum(len(letters) for letters, _ in KEY_WHEEL_DATA)

# CONSEC_MAPS is a list of dicts, one for each key wheel. Each dict key is
# a letter. The value is the string of 7 consecutive letters that would make the
# key setting invalid according to Army procedure. The consecutive string
# accounts for the letters on the key wheel and wrap-around.

def build_consec_map(letters):
    """Builds a "consecutive map" for the list of letters on a key wheel. This
    is used to validate a pin list to make sure there are not too many effective
    or ineffective pins in a consecutive sequence.

    """
    deque = collections.deque(letters)
    consec = {}
    for c in letters:
        consec[c] = ''.join(itertools.islice(deque, 0, 7))
        deque.rotate(-1)
    return consec

CONSEC_MAPS = [build_consec_map(letters) for letters, _ in KEY_WHEEL_DATA]


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

    # From the manual:
    # "2a: Select a set of numbers from either group A or group B in appenix II.
    # Sets of numbers selected from group B must not exceed 10% of the total
    # sets selected."

    # For our purposes, we'll just pick from group B 10% of the time. We also
    # (currently) have no history of prior key list generations, so we don't
    # worry about reusing sets or how often we've picked from group B.
    rn = random.randint(0, 100)
    group = GROUP_A if rn > 10 else GROUP_B
    selection = random.choice(group)

    # 2b: Rearrange the numbers so they appear in a random order
    random.shuffle(selection)

    # 2c: Distribution of Overlaps
    overlap = sum(selection) - 27

    # TODO:
    # (1) Most of the six number should be involved
    # (2) Overlaps should include numbers which are separated, and numbers which
    # are side by side.
    # (3) Several small overlaps should be used in preference to one large
    # overlap
    # (4) There must not be more than four overlaps between any two numbers.

    # 2d: Checking placement of overlaps
    # TODO

    # Build lug string
    # TODO

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

    for n, pins in enumerate(pin_list):
        if check_consecutive(n, pins):
            return False

    # Check for more than 6 consecutive ineffective pins on a wheel

    for n, pins in enumerate(pin_list):
        if check_consecutive(n, invert_pins(n, pins)):
            return False

    return True


def check_consecutive(n, pins):
    """Check for consecutive pins on key wheel n. The pins parameter must be
    a string of the pins that are effective. Returns True if there are more than
    6 consecutive effective pins and False otherwise.

    """
    consec = CONSEC_MAPS[n]
    deque = collections.deque(pins)
    for c in pins:
        if consec[c] == ''.join(itertools.islice(deque, 0, 7)):
            return True
        deque.rotate(-1)
    return False


def invert_pins(n, pins):
    """Given a string of effective pins on key wheel n, return a string where
    all the effective pins are pushed to the left and all the ineffective pins
    are pushed to the right, thus flipping which pins are effective
    / ineffective.

    """
    all_letters = set(KEY_WHEEL_DATA[n][0])
    effective = set(pins)
    inverse = sorted(all_letters - effective)
    return ''.join(inverse)
