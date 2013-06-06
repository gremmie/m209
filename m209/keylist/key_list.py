# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""key_list.py - This module defines the KeyList class."""

import collections

KeyList = collections.namedtuple('KeyList',
                ['indicator', 'lugs', 'pin_list', 'letter_check'])
