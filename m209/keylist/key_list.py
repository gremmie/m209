# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""This module defines the KeyList class and related functions"""

import collections
import re


VALID_IND_RE = re.compile('^[A-Z]{2}$')


KeyList = collections.namedtuple('KeyList',
                ['indicator', 'lugs', 'pin_list', 'letter_check'])


def valid_indicator(indicator):
    """Returns True if the given indicator is valid and False otherwise."""
    return True if VALID_IND_RE.match(indicator) else False
