# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""This module contains the encrypt & decrypt procedures as described in "War
Department, Official Training Film, T.F. 11 - 1400, Army, Service Forces."
A YouTube playlist of this film can be found here:

http://www.youtube.com/playlist?list=PLCPgncK_sTnEny2-uoTV-1_GC72zo-vKq

This procedure is also described on Mark J. Blair's pages:

http://www.nf6x.net/2013/04/practical-use-of-the-m-209-cipher-machine-chapter-4/
http://www.nf6x.net/2013/04/practical-use-of-the-m-209-cipher-machine-chapter-5/

If other procedures are discovered, this module can be expanded to a package and
the new procedures can be added as different modules. For now, this is the only
procedure known to the author.

"""
import random

from . import M209Error
from .converter import M209, M209_ALPHABET_SET, M209_ALPHABET_LIST
from .key_wheel import KeyWheelError


class ProcedureError(M209Error):
    pass


class StdEncryptProcedure:
    """This class encapsulates the "standard" encrypt procedure for the M-209 as
    found in the training film T.F. 11 - 1400.

    The procedure can be configured with an optional M-209, and optional key
    list to be used for the day. If the M-209 is not supplied, one will be
    created internally. Before an encrypt() operation can be performed, a key
    list must be supplied. This can be done at construction time or via the
    set_key_list() method.

    """
    def __init__(self, m_209=None, key_list=None):
        self.m_209 = m_209 if m_209 else M209()

        if key_list:
            self.set_key_list(key_list)

    def set_key_list(self, key_list):
        """Use the supplied key list for all future encrypt operations.

        Configure the M209 with the key list parameters.

        """
        if len(key_list.indicator) != 2:
            raise ProcedureError("invalid key list indicator")

        self.key_list = key_list
        self.m_209.set_drum_lugs(key_list.lugs)
        self.m_209.set_all_pins(key_list.pin_list)

    def encrypt(self, plaintext, group=True, spaces=True, ext_msg_ind=None, sys_ind=None):
        """Encrypts a plaintext message using standard procedure. The encrypted text
        with the required message indicators are returned as one string.

        The encrypt function accepts these parameters:

        plaintext - Input string of text to be encrypted
        group - If True, the resulting encrypted text will be grouped into 5-letter
            groups with a space between each group. If False, no spaces will be
            present in the output.
        spaces - If True, space characters in the input plaintext will automatically
            be replaced with 'Z' characters before encrypting.
        ext_msg_ind - This is the external message indicator, which, if supplied,
            must be a valid 6 letter string of key wheel settings. If not supplied,
            one will be generated randomly.
        sys_ind - This is the system indicator, which must be a string of length
            1 in the range 'A'-'Z', inclusive. If None, one is chosen at random.

        A ProcedureError will be raised if the procedure does not have a key
        list to work with.

        """
        # Ensure we have a key list indicator and there is no ambiguity:

        if not self.key_list:
            raise ProcedureError("encrypt requires a key list")

        self.m_209.letter_counter = 0

        # Set key wheels to external message indicator
        if ext_msg_ind:
            try:
                self.m_209.set_key_wheels(ext_msg_ind)
            except M209Error as ex:
                raise M209Error("invalid external message indicator {} - {}".format(
                    ext_msg_ind, ex))
        else:
            ext_msg_ind = self.m_209.set_random_key_wheels()

        # Ensure we have a valid system indicator
        if sys_ind:
            if sys_ind not in M209_ALPHABET_SET:
                raise ProcedureError("invalid system indicator {}".format(sys_ind))
        else:
            sys_ind = random.choice(M209_ALPHABET_LIST)

        # Generate internal message indicator

        int_msg_ind = self.m_209.encrypt(sys_ind * 12, group=False)

        # Set wheels to internal message indicator from left to right. We must skip
        # letters that aren't valid for a given key wheel.
        it = iter(int_msg_ind)
        n = 0
        while n != 6:
            try:
                self.m_209.set_key_wheel(n, next(it))
            except KeyWheelError:
                pass
            except StopIteration:
                assert False, "Ran out of letters building internal message indicator"
            else:
                n += 1

        # Now encipher the message on the M209
        ciphertext = self.m_209.encrypt(plaintext, group=group, spaces=spaces)

        # If we are grouping, and the final group in the ciphertext has less than
        # 5 letters, pad with X's to make a complete group:
        if group:
            total_len = len(ciphertext)
            num_groups = total_len // 5
            num_spaces = num_groups - 1 if num_groups >= 2 else 0
            x_count = 5 - (total_len - num_spaces) % 5
            if 0 < x_count < 5:
                ciphertext = ciphertext + 'X' * x_count

        # Add the message indicators to pad each end of the message

        pad1 = sys_ind * 2 + ext_msg_ind[:3]
        pad2 = ext_msg_ind[3:] + self.key_list.indicator

        msg_parts = [pad1, pad2, ciphertext, pad1, pad2]

        # Assemble the final message; group if requested
        sep = ' ' if group else ''
        return sep.join(msg_parts)
