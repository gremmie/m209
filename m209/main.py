# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""This module contains the main() entry point for the command-line m209
utility.

"""
import argparse
import logging
import sys

from .keylist.generate import generate_key_list
from .keylist.key_list import valid_indicator


DESC = "M-209 simulator and utility program"
DEFAULT_KEY_LIST = 'm209keys.cfg'
LOG_CHOICES = ['debug', 'info', 'warning', 'error', 'critical']


def keylist_range(start, end):
    """A generator function to generate key list indicators.

    Generates a range of indicators from start to end, inclusive.

    """
    def to_int(s):
        return (ord(s[0]) - ord('A')) * 26 + ord(s[1]) - ord('A')

    x = to_int(start)
    y = to_int(end)

    for n in range(x, y + 1):
        c = n // 26
        d = n % 26
        yield chr(c + ord('A')) + chr(d + ord('A'))


def encrypt(args):
    """Encrypt subcommand processor"""
    print('Encrypting!', args)


def decrypt(args):
    """Decrypt subcommand processor"""
    print('Decrypting!', args)


def keygen(args):
    """Key list generation subcommand processor"""
    print('Creating key list!', args)


def main(argv=None):
    """Entry point for the m209 command-line utility."""

    # create the top-level parser
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument('-l', '--log', choices=LOG_CHOICES, default='warning',
        help='set log level [default: %(default)s]')
    subparsers = parser.add_subparsers(title='list of commands',
        description='type %(prog)s {command} -h for help on {command}')

    # create the parser for encrypt
    enc_parser = subparsers.add_parser('encrypt', aliases=['en'],
        help='encrypt text')
    enc_parser.add_argument('-k', '--keylist', default=DEFAULT_KEY_LIST,
        help='path to key list file [default: %(default)s]')
    enc_parser.add_argument('-i', '--keylist-indicator',
        help='2 letter key list indicator')
    enc_parser.add_argument('-p', '--plaintext',
        help='plaintext string to encrypt; prompted if omitted')
    enc_parser.add_argument('-e', '--ext-msg-ind',
        help='6 letter external message indicator; if omitted a random one is used')
    enc_parser.add_argument('-s', '--sys-ind',
        help='1 letter system indicator; if omitted a random one is used')
    enc_parser.set_defaults(subcommand=encrypt)

    # create the parser for decrypt
    dec_parser = subparsers.add_parser('decrypt', aliases=['de'],
        help='decrypt text')
    dec_parser.add_argument('-k', '--keylist', default=DEFAULT_KEY_LIST,
        help='path to key list file [default: %(default)s]')
    dec_parser.add_argument('-c', '--ciphertext',
        help='ciphertext string to decrypt; prompted if omitted')
    dec_parser.set_defaults(subcommand=decrypt)

    # create the parser for generating key lists

    kg_parser = subparsers.add_parser('keygen', aliases=['kg'],
        description='Generate key list files',
        help='generate key list')
    kg_parser.add_argument('-f', '--file', default=DEFAULT_KEY_LIST,
        help='path to key list file [default: %(default)s]')
    kg_parser.add_argument('-o', '--overwrite', action='store_true',
        help='overwrite key list file if it exists')
    kg_parser.add_argument('-i', '--indicators', nargs='+', metavar='XX',
        help='key list indicators [e.g. AA BB XA-XZ]')
    kg_parser.add_argument('-r', '--random', type=int, metavar='N',
        help='generate N random key lists')
    kg_parser.set_defaults(subcommand=keygen)

    args = parser.parse_args(args=argv)

    log_level = getattr(logging, args.log.upper())
    logging.basicConfig(level=log_level, format='%(levelname)s:%(message)s')

    args.subcommand(args)


if __name__ == '__main__':
    main()
