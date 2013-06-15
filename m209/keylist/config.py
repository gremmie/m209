# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""This module contains routines to read & write key lists in config (aka INI)
file format.

In the config file format, multiple key lists are stored in one file. Each key
list is stored in a section named for its indicator. In this example, the file
contains settings for 2 key lists, one with indicator AA and one with indicator
YL.

[AA]
lugs = 0-4 0-5*4 0-6*6 1-0*5 1-2 1-5*4 3-0*3 3-4 3-6 5-6
wheel1 = FGIKOPRSUVWYZ
wheel2 = DFGKLMOTUY
wheel3 = ADEFGIORTUVX
wheel4 = ACFGHILMRSU
wheel5 = BCDEFJKLPS
wheel6 = EFGHIJLMNP
check = QLRRN TPTFU TRPTN MWQTV JLIJE J

[YL]
lugs = 1-0 2-0*4 0-3 0-4*3 0-5*2 0-6*11 2-5 2-6 3-4 4-5
wheel1 = BFJKLOSTUWXZ
wheel2 = ABDJKLMORTUV
wheel3 = EHJKNPQRSX
wheel4 = ABCHIJLMPQR
wheel5 = BCDGJLNOPQS
wheel6 = AEFHIJP
check = OZGPK AFVAJ JYRZW LRJEG MOVLU M

"""

import configparser
from .key_list import KeyList

WHEELS = ['wheel{}'.format(n) for n in range(1, 7)]


def read_key_list(fname, indicator):
    """Reads key list information from the file given by fname.

    Searches the config file for the key list with the given indicator. If
    found, returns a KeyList object. Returns None if not found.

    """
    config = configparser.ConfigParser(interpolation=None)
    config.read(fname)

    if indicator not in config.sections():
        return None

    section = config[indicator]
    return KeyList(
            indicator=indicator,
            lugs=section['lugs'],
            pin_list=[section[w] for w in WHEELS],
            letter_check=section['check'])


def write_key_list(fname, key_list):
    """Updates the file named by fname with the given key_list.

    If the file doesn't exist, it is created and the key_list is written to it.

    If the file already exists, it is read and searched for a section that
    matches the key_list indicator name. If found, this section is updated and
    the file is written back out. If the section is not found, one for the
    key_list is added and the file is written out.

    """
    config = configparser.ConfigParser(interpolation=None)
    config.read(fname)

    # If the section for this key list doesn't exist, add one
    if not config.has_section(key_list.indicator):
        config.add_section(key_list.indicator)

    # Now update it
    section = config[key_list.indicator]
    section['lugs'] = key_list.lugs
    for n, wheel in enumerate(WHEELS):
        section[wheel] = key_list.pin_list[n]
    section['check'] = key_list.letter_check

    # Write the file
    with open(fname, 'w') as fp:
        config.write(fp)
