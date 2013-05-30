# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""This module contains the Drum class for the M-209 simulation."""

from . import M209Error

class DrumError(M209Error):
    """Exception class for all drum errors"""
    pass


class Drum:
    """The Drum class represents the drum cage inside the M-209.

    The drum cage consists of 27 bars where each bar has 2 movable lugs. The
    lugs can be slid into positions numbered 1-6 and/or 2 neutral positions
    numbered 0.  As the drum rotates all 27 bars have a chance for their lugs to
    interact with the effective pins on the 6 key wheels. As each bar rotates
    past the effective pins on the 6 key wheels, if one or both lugs come into
    contact with any wheel's effective pins, the bar will quickly shift left.
    This causes the indicator disk to rotate once, thus causing the substitution
    cipher for the selected letter to change. Thus the drum, along with the key
    wheels, acts as a pseudo-random number generator, generating a number
    between 0 and 27, inclusive. Thus number is used to select which
    substitution cipher will be used for the current operator selected letter.

    Internally the bars are represented as a list of 1 or 2 tuples, with one
    entry for each bar that has 1 or more lugs not in neutral positions.  Bars
    that have both lugs in neutral positions do not have entries in the list.
    A bar that has 1 lug in a neutral position, and the other lug in position
    3 will have an entry in the list consisting of the 1-tuple (2, ). A bar that
    has one lug in position 2 and one in position 6 will have an entry in the
    list consisting of the 2-tuple (1, 5). We subtract one from the position for
    0-based indexing reasons.

    The order of the bars list is not relevant as we only need to simulate
    complete revolutions of the drum cage.

    """
    NUM_BARS = 27

    def __init__(self, lug_list=None):
        """Creates a Drum instance with the given lug list.

        If lug_list is None or empty, all lugs will be placed in neutral
        positions.

        If lug_list is present, it must be a list of 1 or 2-tuple integers,
        where each integer is between 0-5, inclusive, and represents a 0-based
        key wheel position. The list can not be longer than NUM_BARS items.

        """
        self.bars = []
        if lug_list:
            self.bars = lug_list
            self._validate_bars()

    @classmethod
    def from_key_list(cls, lug_list):
        """Creates a Drum instance from a string that might be found on a key
        list. The must consist of at most 27 whitespace separated pairs of
        integers separated by dashes. For example:
                '1-0 2-0 2-0 0-3 0-5 0-5 0-6 2-4 3-6'

        Each integer pair must be in the form 'm-n' where m & n are integers
        between 0 and 6, inclusive. Each integer represents a lug position where
        0 is a neutral position, and 1-6 correspond to key wheel positions. If
        m & n are both non-zero, they cannot be equal.

        If a string has less than 27 pairs of integers, it is assumed all
        remaining bars have both lugs in the neutral (0) positions.

        """
        bars = []
        lug_list = lug_list.split()
        for lug_pair in lug_list:
            try:
                m, n = [int(x) for x in lug_pair.split('-')]
            except ValueError:
                raise DrumError("Invalid lug pair {}".format(lug_pair))

            if m and n:
                bars.append((m - 1, n - 1))
            elif m and not n:
                bars.append((m - 1, ))
            elif not m and n:
                bars.append((n - 1, ))

        return cls(lug_list=bars)

    def rotate(self, pins):
        """Rotate the drum cage a complete revolution and return the number of
        times a bar was shifted to the left. The pins parameter must be a
        6-element list of Bools representing the current effective states of
        the 6 key wheels.

        """
        count = 0
        for lug_pair in self.bars:
            for index in lug_pair:
                if pins[index]:
                    count += 1
                    break

        return count

    def _validate_bars(self):
        """Internal function to validate the bars list. Raises DrumError if the
        list is invalid.

        A list is valid if all of these conditions are true:
            * it has NUM_BARS or less entries
            * each entry must be a 1 or 2 tuple of integers in the range 0-5,
              inclusive
            * if an entry is a 2-tuple, the two elements must not be equal to
              each other

        """
        if not isinstance(self.bars, list):
            raise DrumError("Type of lug_list must be list")
        if len(self.bars) > self.NUM_BARS:
            raise DrumError("Too many bars in lug list")

        for lug_pair in self.bars:
            error = False
            try:
                if len(lug_pair) == 1:
                    error = not (0 <= lug_pair[0] <= 5)
                elif len(lug_pair) == 2:
                    error = not (0 <= lug_pair[0] <= 5) or not (
                            0 <= lug_pair[1] <= 5) or (
                                    lug_pair[0] == lug_pair[1])
                else:
                    error = True
            except (ValueError, TypeError):
                error = True

            if error:
                raise DrumError("Invalid lug pair {}".format(lug_pair))
