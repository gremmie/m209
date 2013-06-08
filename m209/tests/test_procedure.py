# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""Unit tests for the M209 encrypt & decrypt procedures."""

import unittest

from ..keylist import KeyList
from ..procedure import StdEncryptProcedure


PLAINTEXT = 'ATTACK AT DAWN'
CIPHERTEXT = 'GGABC DEFFM NQHNL CAARZ OLTVX GGABC DEFFM'


class ProcedureTestCase(unittest.TestCase):

    def setUp(self):
        self.fm = KeyList(indicator="FM",
                    lugs='1-0 2-0*8 0-3*7 0-4*5 0-5*2 1-5 1-6 3-4 4-5',
                    pin_list=[
                        'BCEJOPSTUVXY',
                        'ACDHJLMNOQRUYZ',
                        'AEHJLOQRUV',
                        'DFGILMNPQS',
                        'CEHIJLNPS',
                        'ACDFHIMN'
                    ],
                    letter_check='TNMYS CRMKK UHLKW LDQHM RQOLW R')
        self.proc = StdEncryptProcedure(key_list=self.fm)

    def test_encrypt(self):
        result = self.proc.encrypt(PLAINTEXT, ext_msg_ind='ABCDEF', sys_ind='G')
        self.assertEqual(result, CIPHERTEXT)
