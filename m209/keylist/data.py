# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""This module contains data used in the generation of key lists."""

# This data was obtained from:
#   TM-11-380, War Department, Technical Manual, Converter M-209, M-209-A,
#   M-209-B (cipher) 17 March, 1944.
#   Appendix II (pages 76-79):
#   http://www.ilord.com/m209manual.html
#   http://www.ilord.com/1944manual/page-76.JPG
#   http://www.ilord.com/1944manual/page-78.JPG
#
# The overlap values from the tables were omitted to save memory since they can
# be computed from the set of 6 numbers: overlap = sum(first 6 values) - 27.
#
# It should be noted that I think I found a typo in the Group B data. The
# overlap value does jive with the 6 numbers in one case. See the comment marked
# TYPO?, below. Should I tell the War Department? :P
# I changed it to a sequence where the overlap matched the lines above and below
# it. I suppose it could have been intentional.

GROUP_A = [
    [1, 2, 3, 4, 8, 10],
    [1, 2, 3, 4, 7, 11],
    [1, 2, 3, 4, 6, 12],
    [1, 2, 3, 4, 5, 13],
    [1, 2, 3, 5, 8, 9],
    [1, 2, 3, 5, 7, 10],
    [1, 2, 3, 5, 6, 11],
    [1, 2, 3, 6, 7, 9],
    [1, 2, 4, 5, 7, 9],
    [1, 2, 4, 5, 6, 10],
    [1, 2, 3, 4, 9, 10],
    [1, 2, 3, 4, 8, 11],
    [1, 2, 3, 4, 7, 12],
    [1, 2, 3, 4, 6, 13],
    [1, 2, 3, 5, 8, 10],
    [1, 2, 3, 5, 7, 11],
    [1, 2, 3, 5, 6, 12],
    [1, 2, 3, 6, 8, 9],
    [1, 2, 3, 6, 7, 10],
    [1, 2, 4, 5, 8, 9],
    [1, 2, 4, 5, 7, 10],
    [1, 2, 4, 5, 6, 11],
    [1, 2, 4, 6, 7, 9],
    [1, 2, 3, 4, 9, 11],
    [1, 2, 3, 4, 8, 12],
    [1, 2, 3, 4, 7, 13],
    [1, 2, 3, 5, 9, 10],
    [1, 2, 3, 5, 8, 11],
    [1, 2, 3, 5, 7, 12],
    [1, 2, 3, 5, 6, 13],
    [1, 2, 3, 6, 8, 10],
    [1, 2, 3, 6, 7, 11],
    [1, 2, 3, 7, 8, 9],
    [1, 2, 4, 5, 8, 10],
    [1, 2, 4, 5, 7, 11],
    [1, 2, 4, 5, 6, 12],
    [1, 2, 4, 6, 8, 9],
    [1, 2, 4, 6, 7, 10],
    [1, 2, 3, 4, 10, 11],
    [1, 2, 3, 4, 9, 12],
    [1, 2, 3, 4, 8, 13],
    [1, 2, 3, 5, 9, 11],
    [1, 2, 3, 5, 8, 12],
    [1, 2, 3, 5, 7, 13],
    [1, 2, 3, 6, 9, 10],
    [1, 2, 3, 6, 8, 11],
    [1, 2, 3, 6, 7, 12],
    [1, 2, 3, 7, 8, 10],
    [1, 2, 4, 5, 9, 10],
    [1, 2, 4, 5, 8, 11],
    [1, 2, 4, 5, 7, 12],
    [1, 2, 4, 5, 6, 13],
    [1, 2, 4, 6, 7, 11],
    [1, 2, 4, 6, 8, 10],
    [1, 2, 4, 7, 8, 9],
    [1, 2, 3, 4, 10, 12],
    [1, 2, 3, 4, 9, 13],
    [1, 2, 3, 5, 10, 11],
    [1, 2, 3, 5, 9, 12],
    [1, 2, 3, 5, 8, 13],
    [1, 2, 3, 6, 9, 11],
    [1, 2, 3, 6, 8, 12],
    [1, 2, 3, 6, 7, 13],
    [1, 2, 3, 7, 9, 10],
    [1, 2, 3, 7, 8, 11],
    [1, 2, 4, 5, 9, 11],
    [1, 2, 4, 5, 8, 12],
    [1, 2, 4, 5, 7, 13],
    [1, 2, 4, 6, 9, 10],
    [1, 2, 4, 6, 8, 11],
    [1, 2, 4, 6, 7, 12],
    [1, 2, 4, 7, 8, 10],
    [1, 2, 3, 4, 11, 12],
    [1, 2, 3, 4, 10, 13],
    [1, 2, 3, 5, 10, 12],
    [1, 2, 3, 5, 9, 13],
    [1, 2, 3, 6, 10, 11],
    [1, 2, 3, 6, 9, 12],
    [1, 2, 3, 6, 8, 13],
    [1, 2, 3, 7, 9, 11],
    [1, 2, 3, 7, 8, 12],
    [1, 2, 4, 5, 10, 11],
    [1, 2, 4, 5, 9, 12],
    [1, 2, 4, 5, 8, 13],
    [1, 2, 4, 6, 8, 12],
    [1, 2, 4, 6, 9, 11],
    [1, 2, 4, 6, 7, 13],
    [1, 2, 4, 7, 9, 10],
    [1, 2, 4, 7, 8, 11],
    [1, 2, 3, 4, 11, 13],
    [1, 2, 3, 5, 11, 12],
    [1, 2, 3, 5, 10, 13],
    [1, 2, 3, 6, 10, 12],
    [1, 2, 3, 6, 9, 13],
    [1, 2, 3, 7, 10, 11],
    [1, 2, 3, 7, 9, 12],
    [1, 2, 3, 7, 8, 13],
    [1, 2, 4, 5, 10, 12],
    [1, 2, 4, 5, 9, 13],
    [1, 2, 4, 6, 8, 13],
    [1, 2, 4, 6, 9, 12],
    [1, 2, 4, 6, 10, 11],
    [1, 2, 4, 7, 9, 11],
    [1, 2, 4, 7, 8, 12],
    [1, 2, 4, 8, 9, 10],
    [1, 2, 3, 5, 11, 13],
    [1, 2, 3, 6, 11, 12],
    [1, 2, 3, 6, 10, 13],
    [1, 2, 3, 7, 10, 12],
    [1, 2, 3, 7, 9, 13],
    [1, 2, 4, 5, 11, 12],
    [1, 2, 4, 5, 10, 13],
    [1, 2, 4, 6, 9, 13],
    [1, 2, 4, 6, 10, 12],
    [1, 2, 4, 7, 10, 11],
    [1, 2, 4, 7, 9, 12],
    [1, 2, 4, 7, 8, 13],
    [1, 2, 4, 8, 9, 11],
    [1, 2, 3, 5, 12, 13],
    [1, 2, 3, 6, 11, 13],
    [1, 2, 3, 7, 11, 12],
    [1, 2, 3, 7, 10, 13],
    [1, 2, 4, 5, 11, 13],
    [1, 2, 4, 6, 10, 13],
    [1, 2, 4, 6, 11, 12],
    [1, 2, 4, 7, 10, 12],
    [1, 2, 4, 7, 9, 13],
    [1, 2, 4, 8, 10, 11],
    [1, 2, 4, 8, 9, 12],
    [1, 2, 3, 6, 12, 13],
    [1, 2, 3, 7, 11, 13],
    [1, 2, 4, 5, 12, 13],
    [1, 2, 4, 6, 11, 13],
    [1, 2, 4, 7, 11, 12],
    [1, 2, 4, 7, 10, 13],
    [1, 2, 4, 8, 9, 13],
    [1, 2, 4, 8, 10, 12],
    [1, 2, 3, 7, 12, 13],
    [1, 2, 4, 6, 12, 13],
    [1, 2, 4, 7, 11, 13],
    [1, 2, 4, 8, 11, 12],
    [1, 2, 4, 8, 10, 13],
    [1, 2, 4, 7, 12, 13],
    [1, 2, 4, 8, 11, 13],
]

GROUP_B = [
    [1, 1, 2, 3, 8, 13],
    [1, 1, 2, 4, 9, 11],
    [1, 1, 2, 4, 8, 12],
    [1, 1, 2, 4, 7, 13],
    [1, 1, 2, 5, 9, 10],
    [1, 1, 2, 5, 8, 11],
    [1, 1, 2, 5, 7, 12],
    [1, 1, 2, 5, 6, 13],
    [1, 1, 3, 4, 9, 10],
    [1, 1, 3, 4, 8, 11],
    [1, 1, 3, 4, 7, 12],
    [1, 1, 3, 4, 6, 13],
    [1, 1, 3, 5, 8, 10],
    [1, 1, 3, 5, 7, 11],
    [1, 1, 3, 5, 6, 12],
    [1, 1, 3, 6, 8, 9],
    [1, 1, 3, 6, 7, 10],
    [1, 2, 2, 3, 9, 11],
    [1, 2, 2, 3, 8, 12],
    [1, 2, 2, 3, 7, 13],
    [1, 2, 2, 4, 8, 11],
    [1, 2, 2, 4, 7, 12],
    [1, 2, 2, 4, 6, 13],
    [1, 2, 2, 5, 8, 10],
    [1, 2, 2, 5, 7, 11],
    [1, 2, 2, 5, 6, 12],
    [1, 2, 2, 6, 8, 9],
    [1, 2, 2, 6, 7, 10],
    [1, 2, 3, 3, 9, 10],
    [1, 2, 3, 3, 8, 11],
    [1, 2, 3, 3, 7, 12],
    [1, 2, 3, 4, 9, 9],
    [1, 2, 3, 5, 5, 12],
    [1, 2, 3, 6, 6, 10],
    [1, 2, 4, 4, 8, 9],
    [1, 2, 4, 5, 5, 11],
    [1, 2, 4, 6, 6, 9],
    [1, 1, 2, 4, 9, 12],
    [1, 1, 2, 4, 8, 13],
    [1, 1, 2, 5, 9, 11],
    [1, 1, 2, 5, 8, 12],
    [1, 1, 2, 5, 7, 13],
    [1, 1, 3, 4, 9, 11],
    [1, 1, 3, 4, 8, 12],
    [1, 1, 3, 4, 7, 13],
    [1, 1, 3, 5, 9, 10],
    [1, 1, 3, 5, 8, 11],
    [1, 1, 3, 5, 7, 12],
    [1, 1, 3, 5, 6, 13],
    [1, 1, 3, 6, 8, 10],
    [1, 1, 3, 6, 7, 11],
    [1, 2, 2, 3, 9, 12],
    [1, 2, 2, 3, 8, 13],
    [1, 2, 2, 4, 9, 11],
    [1, 2, 2, 4, 7, 13],
    [1, 2, 2, 5, 9, 10],
    [1, 2, 2, 5, 8, 11],
    [1, 2, 2, 5, 7, 12],
    [1, 2, 2, 5, 6, 13],
    [1, 2, 2, 6, 8, 10], # TYPO? Manual has 1 2 2 6 10 11 (with overlap = 2)
    [1, 2, 2, 6, 7, 11],
    [1, 2, 3, 3, 9, 11],
    [1, 2, 3, 3, 8, 12],
    [1, 2, 3, 3, 7, 13],
    [1, 2, 3, 5, 5, 13],
    [1, 2, 3, 5, 9, 9],
    [1, 2, 3, 6, 6, 11],
    [1, 2, 3, 7, 7, 9],
    [1, 2, 4, 4, 7, 11],
    [1, 2, 4, 4, 5, 13],
    [1, 2, 4, 5, 5, 12],
    [1, 1, 2, 4, 9, 13],
    [1, 1, 2, 5, 10, 11],
    [1, 1, 2, 5, 9, 12],
    [1, 1, 2, 5, 8, 13],
    [1, 1, 3, 4, 10, 11],
    [1, 1, 3, 4, 9, 12],
    [1, 1, 3, 4, 8, 13],
    [1, 1, 3, 5, 9, 11],
    [1, 1, 3, 5, 8, 12],
    [1, 1, 3, 5, 7, 13],
    [1, 1, 3, 6, 9, 10],
    [1, 1, 3, 6, 8, 11],
    [1, 1, 3, 6, 7, 12],
    [1, 2, 2, 3, 9, 13],
    [1, 2, 2, 4, 10, 11],
    [1, 2, 2, 4, 9, 12],
    [1, 2, 2, 4, 8, 13],
    [1, 2, 2, 5, 9, 11],
    [1, 2, 2, 5, 8, 12],
    [1, 2, 2, 5, 7, 13],
    [1, 2, 2, 6, 9, 10],
    [1, 2, 2, 6, 8, 11],
    [1, 2, 2, 6, 7, 12],
    [1, 2, 3, 3, 10, 11],
    [1, 2, 3, 3, 9, 12],
    [1, 2, 3, 3, 8, 13],
    [1, 2, 3, 4, 10, 10],
    [1, 2, 3, 6, 6, 12],
    [1, 2, 3, 6, 9, 9],
    [1, 2, 3, 7, 7, 10],
    [1, 2, 4, 4, 9, 10],
    [1, 2, 4, 4, 8, 11],
    [1, 2, 4, 4, 7, 12],
    [1, 2, 4, 4, 6, 13],
    [1, 2, 4, 5, 5, 13],
    [1, 2, 4, 5, 9, 9],
    [1, 2, 4, 6, 6, 11],
    [1, 2, 4, 7, 7, 9],
    [1, 1, 2, 5, 10, 12],
    [1, 1, 2, 5, 9, 13],
    [1, 1, 3, 4, 10, 12],
    [1, 1, 3, 4, 9, 13],
    [1, 1, 3, 5, 10, 11],
    [1, 1, 3, 5, 9, 12],
    [1, 1, 3, 5, 8, 13],
    [1, 1, 3, 6, 9, 11],
    [1, 1, 3, 6, 8, 12],
    [1, 1, 3, 6, 7, 13],
    [1, 2, 2, 4, 9, 13],
    [1, 2, 2, 5, 10, 11],
    [1, 2, 2, 5, 9, 12],
    [1, 2, 2, 5, 8, 13],
    [1, 2, 2, 6, 9, 11],
    [1, 2, 2, 6, 7, 13],
    [1, 2, 3, 3, 10, 12],
    [1, 2, 3, 3, 9, 13],
    [1, 2, 3, 5, 10, 10],
    [1, 2, 3, 6, 6, 13],
    [1, 2, 3, 7, 7, 11],
    [1, 2, 3, 7, 9, 9],
    [1, 2, 4, 4, 9, 11],
    [1, 2, 4, 4, 7, 13],
    [1, 2, 4, 6, 9, 9],
    [1, 2, 4, 7, 7, 10],
    [1, 1, 2, 5, 10, 13],
    [1, 1, 3, 4, 10, 13],
    [1, 1, 3, 5, 10, 12],
    [1, 1, 3, 5, 9, 13],
    [1, 1, 3, 6, 10, 11],
    [1, 1, 3, 6, 9, 12],
    [1, 1, 3, 6, 8, 13],
    [1, 2, 2, 4, 10, 13],
    [1, 2, 2, 5, 10, 12],
    [1, 2, 2, 5, 9, 13],
    [1, 2, 2, 6, 9, 12],
    [1, 2, 2, 6, 8, 13],
    [1, 2, 3, 3, 10, 13],
    [1, 2, 3, 4, 11, 11],
    [1, 2, 3, 6, 10, 10],
    [1, 2, 3, 7, 7, 12],
    [1, 2, 4, 4, 10, 11],
    [1, 2, 4, 4, 9, 12],
    [1, 2, 4, 4, 8, 13],
    [1, 2, 4, 6, 6, 13],
    [1, 2, 4, 7, 7, 11],
    [1, 2, 4, 7, 9, 9],
    [1, 2, 4, 8, 8, 9],
    [1, 1, 3, 5, 11, 12],
    [1, 1, 3, 5, 10, 13],
    [1, 1, 3, 6, 10, 12],
    [1, 1, 3, 6, 9, 13],
    [1, 2, 2, 4, 11, 13],
    [1, 2, 2, 5, 11, 12],
    [1, 2, 2, 5, 10, 13],
    [1, 2, 2, 6, 9, 13],
    [1, 2, 3, 3, 11, 13],
    [1, 2, 3, 5, 11, 11],
    [1, 2, 3, 7, 7, 13],
    [1, 2, 3, 7, 10, 10],
    [1, 2, 4, 7, 7, 12],
    [1, 2, 4, 8, 9, 9],
    [1, 1, 3, 5, 11, 13],
    [1, 1, 3, 6, 11, 12],
    [1, 1, 3, 6, 10, 13],
    [1, 2, 2, 4, 12, 13],
    [1, 2, 2, 5, 11, 13],
    [1, 2, 2, 6, 11, 12],
    [1, 2, 2, 6, 10, 13],
    [1, 2, 3, 6, 11, 11],
    [1, 2, 4, 4, 11, 12],
    [1, 2, 4, 4, 10, 13],
    [1, 2, 4, 5, 11, 11],
    [1, 2, 4, 7, 7, 13],
    [1, 2, 4, 7, 10, 10],
    [1, 2, 4, 8, 8, 11],
    [1, 1, 3, 6, 11, 13],
    [1, 2, 2, 6, 11, 13],
    [1, 2, 3, 5, 12, 12],
    [1, 2, 4, 4, 11, 13],
    [1, 2, 4, 6, 11, 11],
    [1, 1, 3, 6, 12, 13],
    [1, 2, 2, 6, 12, 13],
    [1, 2, 3, 6, 12, 12],
    [1, 2, 4, 4, 12, 13],
    [1, 2, 4, 5, 12, 12],
    [1, 2, 4, 7, 11, 11],
    [1, 2, 4, 8, 8, 13],
    [1, 2, 2, 6, 13, 13],
    [1, 2, 3, 5, 13, 13],
    [1, 2, 4, 8, 11, 11],
    [1, 2, 3, 6, 13, 13],
    [1, 2, 4, 7, 12, 12],
    [1, 2, 3, 7, 13, 13],
]


# All possible inputs to the Drum.rotate() function. This is used to ensure lug
# settings can create all values between 1 - 27, inclusive.
#
# This list was generated as follows:
# >>> from itertools import permutations
# >>> cases = [
# ...     [True, True, True, True, True, True],
# ...     [True, True, True, True, True, False],
# ...     [True, True, True, True, False, False],
# ...     [True, True, True, False, False, False],
# ...     [True, True, False, False, False, False],
# ...     [True, False, False, False, False, False],
# ... ]
# >>>
# >>> result = []
# >>> for case in cases:
# ...     result.extend(sorted(list(set(permutations(case)))))
#
# The code above could have been included directly but it seems wasteful to
# compute it every time the program is run. We'll trade some memory for CPU
# here.

ALL_DRUM_ROTATE_INPUTS = [
    (True, True, True, True, True, True),
    (False, True, True, True, True, True),
    (True, False, True, True, True, True),
    (True, True, False, True, True, True),
    (True, True, True, False, True, True),
    (True, True, True, True, False, True),
    (True, True, True, True, True, False),
    (False, False, True, True, True, True),
    (False, True, False, True, True, True),
    (False, True, True, False, True, True),
    (False, True, True, True, False, True),
    (False, True, True, True, True, False),
    (True, False, False, True, True, True),
    (True, False, True, False, True, True),
    (True, False, True, True, False, True),
    (True, False, True, True, True, False),
    (True, True, False, False, True, True),
    (True, True, False, True, False, True),
    (True, True, False, True, True, False),
    (True, True, True, False, False, True),
    (True, True, True, False, True, False),
    (True, True, True, True, False, False),
    (False, False, False, True, True, True),
    (False, False, True, False, True, True),
    (False, False, True, True, False, True),
    (False, False, True, True, True, False),
    (False, True, False, False, True, True),
    (False, True, False, True, False, True),
    (False, True, False, True, True, False),
    (False, True, True, False, False, True),
    (False, True, True, False, True, False),
    (False, True, True, True, False, False),
    (True, False, False, False, True, True),
    (True, False, False, True, False, True),
    (True, False, False, True, True, False),
    (True, False, True, False, False, True),
    (True, False, True, False, True, False),
    (True, False, True, True, False, False),
    (True, True, False, False, False, True),
    (True, True, False, False, True, False),
    (True, True, False, True, False, False),
    (True, True, True, False, False, False),
    (False, False, False, False, True, True),
    (False, False, False, True, False, True),
    (False, False, False, True, True, False),
    (False, False, True, False, False, True),
    (False, False, True, False, True, False),
    (False, False, True, True, False, False),
    (False, True, False, False, False, True),
    (False, True, False, False, True, False),
    (False, True, False, True, False, False),
    (False, True, True, False, False, False),
    (True, False, False, False, False, True),
    (True, False, False, False, True, False),
    (True, False, False, True, False, False),
    (True, False, True, False, False, False),
    (True, True, False, False, False, False),
    (False, False, False, False, False, True),
    (False, False, False, False, True, False),
    (False, False, False, True, False, False),
    (False, False, True, False, False, False),
    (False, True, False, False, False, False),
    (True, False, False, False, False, False),
]
