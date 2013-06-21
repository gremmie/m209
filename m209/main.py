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


def encrypt(args):
    """Encrypt subcommand processor"""
    print('Encrypting!', args)


def decrypt(args):
    """Decrypt subcommand processor"""
    print('Decrypting!', args)


def keygen(args):
    """Key list generation subcommand processor"""
    print('Creating key list!', args)
    if not valid_indicator(args.keylist_indicator):
        sys.exit("Invalid key list indicator\n")

    print(generate_key_list(args.keylist_indicator))


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
        help='generate key list')
    kg_parser.add_argument('-k', '--keylist', default=DEFAULT_KEY_LIST,
        help='path to key list file [default: %(default)s]')
    kg_parser.add_argument('-i', '--keylist-indicator',
        help='2 letter key list indicator')
    kg_parser.set_defaults(subcommand=keygen)

    args = parser.parse_args(args=argv)

    log_level = getattr(logging, args.log.upper())
    logging.basicConfig(level=log_level, format='%(levelname)s:%(message)s')

    args.subcommand(args)


if __name__ == '__main__':
    main()
