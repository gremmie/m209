# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""This module contains the M209 class, which puts together all the parts to
assemble a complete M-209 converter.

"""
import string

from . import M209Error
from .data import KEY_WHEEL_DATA
from .key_wheel import KeyWheel
from .drum import Drum

ALLOWED_PLAINTEXT = set(string.ascii_uppercase)
CIPHER = list(reversed(string.ascii_uppercase))


class M209:
    """The M209 class is the top-level class in the M-209 simulation. It
    aggregates key wheels and a drum and orchestrates their movements to provide
    encrypt and decrypt functions for the operator.

    """
    def __init__(self):
        """Build a M209 instance with all pins in the ineffective state and all
        drum lugs in neutral positions.

        """
        self.key_wheels = [KeyWheel(*args) for args in KEY_WHEEL_DATA]
        self.drum = Drum()
        self.letter_counter = 0

    def set_pins(self, n, effective_pins):
        """Sets the pin settings on the key wheel specified by n, where n is
        between 0-5, inclusive. Key wheel 0 is the left-most wheel and wheel
        5 is the right-most.

        effective_pins - must be an iterable of letters whose pins are slid to
        the "effective" position (to the right). Letters not appearing in this
        sequence are considered to be in the "ineffective" position (to the
        left). If None or empty, all pins are set to be ineffective.

        """
        if not (0 <= n < len(self.key_wheels)):
            raise M209Error("set_pins(): invalid key wheel index {}".format(n))
        self.key_wheels[n].set_pins(effective_pins)

    def set_drum_lugs(self, lug_list):
        """Sets the drum lugs according to the given lug_list parameter.

        If lug_list is None or empty, all lugs will be placed in neutral
        positions.

        Otherwise, the lug_list can either be a list or a string.

        If lug_list is passed a list, it must be a list of 1 or 2-tuple integers,
        where each integer is between 0-5, inclusive, and represents a 0-based
        key wheel position. The list can not be longer than 27 items.

        If lug_list is passed as a string, it is assumed to be in key list
        format. That is, it must consist of at most 27 whitespace separated pairs
        of integers separated by dashes. For example:
                '1-0 2-0 2-0 0-3 0-5 0-5 0-5 0-6 2-4 3-6'

        Each integer pair must be in the form 'm-n' where m & n are integers
        between 0 and 6, inclusive. Each integer represents a lug position where
        0 is a neutral position, and 1-6 correspond to key wheel positions. If
        m & n are both non-zero, they cannot be equal.

        If a string or list has less than 27 items, it is assumed all remaining
        bars have both lugs in the neutral (0) positions.

        Order in a list or string doesn't matter.

        An alternate shortcut notation is also supported:
                '1-0 2-0*2 0-3 0-5*3 0-6 2-4 3-6'

        Any pair that is suffixed by '*k', where k is a positive integer, means
        there are k copies of the preceeding lug pair combination. In other
        words, these two strings describe identical drum configurations:
                '2-4 2-4 2-4 0-1 0-1'
                '2-4*3 0-1*2'

        """
        if isinstance(lug_list, str):
            drum = Drum.from_key_list(lug_list)
        else:
            drum = Drum(lug_list)
        self.drum = drum

    def encrypt(self, plaintext, group=True):

        ciphertext = []
        for p in plaintext:
            if p not in ALLOWED_PLAINTEXT:
                raise M209Error("Illegal input to encrypt(): {}".format(p))

            pins = [kw.is_effective() for kw in self.key_wheels]
            count = self.drum.rotate(pins)
            c = CIPHER[(ord(p) - ord('A') - count) % 26]
            ciphertext.append(c)

            for kw in self.key_wheels:
                kw.rotate()

            self.letter_counter += 1

        if group:
            s = ' '.join(''.join(ciphertext[i:i+5]) for i in range(0,
                len(ciphertext), 5))
        else:
            s = ''.join(ciphertext)

        return s


if __name__ == '__main__':

    m209 = M209()
    m209.set_drum_lugs('1-0 2-0*4 0-3 0-4*3 0-5*3 0-6*11 2-5 2-6 3-4 4-5')
    m209.set_pins(0, 'BFJKLOSTUWXZ')
    m209.set_pins(1, 'ABDJKLMORTUV')
    m209.set_pins(2, 'EHJKNPQRSX')
    m209.set_pins(3, 'ABCHIJLMPQR')
    m209.set_pins(4, 'BCDGJLNOPQS')
    m209.set_pins(5, 'AEFHIJP')
    pt = 'A' * 26
    print(m209.encrypt(pt))



