# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""This module contains the main() entry point for the command-line m209
utility.

"""
import argparse


DESC = "M-209 simulator and utility program"
DEFAULT_KEY_LIST = 'm209keys.cfg'


def encrypt(args):
    """Encrypt subcommand processor"""
    print('Encrypting!', args)


def decrypt(args):
    """Decrypt subcommand processor"""
    print('Decrypting!', args)


def main(argv=None):
    """Entry point for the m209 command-line utility."""

    # create the top-level parser
    parser = argparse.ArgumentParser(description=DESC)
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
    enc_parser = subparsers.add_parser('decrypt', aliases=['de'],
        help='decrypt text')
    enc_parser.add_argument('-k', '--keylist', default=DEFAULT_KEY_LIST,
        help='path to key list file [default: %(default)s]')
    enc_parser.add_argument('-c', '--ciphertext',
        help='ciphertext string to decrypt; prompted if omitted')
    enc_parser.set_defaults(subcommand=decrypt)

    args = parser.parse_args(args=argv)
    args.subcommand(args)


if __name__ == '__main__':
    main()
