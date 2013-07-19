Library Reference
=================

This section of the documentation is aimed at developers who wish to use the
``m209`` library as part of their own application. This documentation covers
the major classes and functions.

Key lists
---------

Key lists are represented as a named tuple called ``KeyList``.

.. class:: m209.keylist.KeyList(indicator, lugs, pin_list, letter_check)

   As a named tuple, ``KeyList`` has the following attributes:

   * ``indicator`` - the string name for the ``KeyList``; must be 2 letters in
     the range ``AA`` - ``ZZ``
   * ``lugs`` - a string representing the drum lug settings; see below
   * ``pin_list`` - a list of six strings which represent key wheel pin
     settings; see below
   * ``letter_check`` - a string representing the letter check used to verify
     operator settings; if unknown this can be ``None`` or an empty string
   
Lug settings string format
~~~~~~~~~~~~~~~~~~~~~~~~~~

Drum lug settings are often conveniently represented as strings consisting of
at most 27 whitespace-separated pairs of integers separated by dashes. For
example::

   lugs = '1-0 2-0 2-0 0-3 0-5 0-5 0-5 0-6 2-4 3-6'

Each integer pair must be in the form ``m-n`` where m & n are integers
between 0 and 6, inclusive. Each integer represents a lug position where
0 is a neutral position, and 1-6 correspond to key wheel positions. If
m & n are both non-zero, they cannot be equal.

If a string has less than 27 pairs, it is assumed all remaining bars have both
lugs in the neutral (0) positions.

Order of the pairs within the string does not matter.

To reduce typing and to aid in readability, an alternate shortcut notation is
supported::

   lugs = '1-0 2-0*2 0-3 0-5*3 0-6 2-4 3-6'

Any pair that is suffixed by ``*k``, where k is a positive integer, means there
are ``k`` copies of the preceeding lug pair combination. For example, these two
strings describe identical drum configurations::

   lugs1 = '2-4 2-4 2-4 0-1 0-1'
   lugs2 = '2-4*3 0-1*2'

Key wheel pin settings
~~~~~~~~~~~~~~~~~~~~~~

Key wheel pin settings are represented as iterables of letters whose pins are
slid to the "effective" position (to the right). Letters not appearing in this
sequence are considered to be in the "ineffective" position (to the left). If
None or empty, all pins are set to be ineffective.

Examples::

   all_ineffective = ''
   wheel1 = 'ABDEFHIJMQSUXZ'
   wheel2 = 'EINPQRTVXZ'
   wheel3 = 'DEFGIKNOSUX'
   wheel4 = 'BFGJKRS'
   wheel5 = 'ABCDFGHIJMPS'
   wheel6 = 'ADEFHIJKN'

Key List Example
~~~~~~~~~~~~~~~~

An example of using the :py:class:`m209.keylist.KeyList` is:

.. code-block:: python

   from m209.keylist import KeyList

   key_list1 = KeyList(
          indicator='AA',
          lugs='0-4 0-5*4 0-6*6 1-0*5 1-2 1-5*4 3-0*3 3-4 3-6 5-6',
          pin_list=[
              'FGIKOPRSUVWYZ',
              'DFGKLMOTUY',
              'ADEFGIORTUVX',
              'ACFGHILMRSU',
              'BCDEFJKLPS',
              'EFGHIJLMNP'
          ],
          letter_check='QLRRN TPTFU TRPTN MWQTV JLIJE J')
