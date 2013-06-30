# Copyright (C) 2013 by Brian Neal.
# This file is part of m209, the M-209 simulation.
# m209 is released under the MIT License (see LICENSE.txt).

"""This module contains the main() entry point for the command-line m209
utility.

"""
import argparse
import logging
import os.path
import random
import re
import sys

from . import M209Error
from .converter import M209_ALPHABET_SET
from .data import KEY_WHEEL_DATA
from .keylist.generate import generate_key_list
from .keylist.key_list import valid_indicator, IndicatorIter
from .keylist.config import write as write_config, read_key_list
from .procedure import StdProcedure


DESC = "M-209 simulator and utility program"
DEFAULT_KEY_LIST = 'm209keys.cfg'
LOG_CHOICES = ['debug', 'info', 'warning', 'error', 'critical']
SYS_IND_RE = re.compile(r'^[A-Z]{1}$')


def validate_key_list_indicator(s):
    """Validation/conversion function for validating the supplied starting key
    list indicator.

    Returns the string value if valid, otherwise raises an ArgumentTypeError.

    """
    if len(s) == 2:
        s = s.upper()
        if valid_indicator(s):
            return s

    raise argparse.ArgumentTypeError('must be in the range AA-ZZ')


def validate_num_key_lists(s):
    """Validation/conversion function for validating the number of key lists to
    generate.

    Returns the integer value if valid, otherwise raises an ArgumentTypeError

    """
    bounds = (1, 26 ** 2)
    msg = "value must be in range {}-{}".format(*bounds)
    try:
        val = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(msg)

    if not (bounds[0] <= val <= bounds[1]):
        raise argparse.ArgumentTypeError(msg)
    return val


def validate_ext_indicator(s):
    """Validation function for the external message indicator option.

    Returns the string value if valid, otherwise raises an ArgumentTypeError.

    """
    if len(s) == 6:
        s = s.upper()
        for n, c in enumerate(s):
            if c not in KEY_WHEEL_DATA[n][0]:
                break
        else:
            return s

    raise argparse.ArgumentTypeError(
        "{} is not a valid external message indicator".format(s))


def validate_sys_indicator(s):
    """Validation function for the system message indicator option.

    Returns the string value if valid, otherwise raises an ArgumentTypeError.

    """
    if len(s) == 1:
        s = s.upper()
        if s in M209_ALPHABET_SET:
            return s

    raise argparse.ArgumentTypeError('value must be 1 letter')


def encrypt(args):
    """Encrypt subcommand processor"""
    print('Encrypting!', args)

    logging.info("Encrypting using key file %s", args.file)
    if not os.path.isfile(args.file):
        sys.exit("key list file not found: {}\n".format(args.file))

    # Get a key list from the key list file
    key_list = read_key_list(args.file, args.key_list_ind)
    if not key_list:
        sys.exit("key list not found in file: {}\n".format(args.file))

    proc = StdProcedure(key_list=key_list)
    plaintext = "HELLOZWORLDX"
    ct = proc.encrypt(plaintext, ext_msg_ind=args.ext_ind, sys_ind=args.sys_ind)
    print(ct)


def decrypt(args):
    """Decrypt subcommand processor"""
    print('Decrypting!', args)


def keygen(args):
    """Key list generation subcommand processor"""
    logging.info("Creating key list file: %s", args.file)

    if not args.overwrite and os.path.exists(args.file):
        sys.exit("File '{}' exists. Use -o to overwrite\n".format(args.file))

    if args.start is None:   # random indicators
        indicators = random.sample([i for i in IndicatorIter()], args.number)
        indicators.sort()
    else:
        it = IndicatorIter(args.start)
        n = len(it)
        if n < args.number:
            sys.exit("Error: can only produce {} key lists when starting at {}\n".format(
                n, args.start))

        indicators = (next(it) for n in range(args.number))

    key_lists = (generate_key_list(indicator) for indicator in indicators)

    write_config(args.file, key_lists)


def main(argv=None):
    """Entry point for the m209 command-line utility."""

    # create the top-level parser
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument('-l', '--log', choices=LOG_CHOICES, default='warning',
        help='set log level [default: %(default)s]')
    subparsers = parser.add_subparsers(title='list of commands',
        description='type %(prog)s {command} -h for help on {command}')

    # create the sub-parser for encrypt
    enc_parser = subparsers.add_parser('encrypt', aliases=['en'],
        help='encrypt text')
    enc_parser.add_argument('-f', '--file', default=DEFAULT_KEY_LIST,
        help='path to key list file [default: %(default)s]')
    enc_parser.add_argument('-p', '--plaintext', default='-',
        help='path to plaintext file or - for stdin [default: %(default)s]')
    enc_parser.add_argument('-k', '--key-list-ind', metavar='XX',
        type=validate_key_list_indicator,
        help='2-letter key list indicator; if omitted a random one is used')
    enc_parser.add_argument('-e', '--ext-ind', metavar='ABCDEF',
        type=validate_ext_indicator,
        help='6-letter external message indicator; if omitted a random one is used')
    enc_parser.add_argument('-s', '--sys-ind', metavar='S',
        type=validate_sys_indicator,
        help='1-letter system indicator; if omitted a random one is used')
    enc_parser.set_defaults(subcommand=encrypt)

    # create the sub-parser for decrypt
    dec_parser = subparsers.add_parser('decrypt', aliases=['de'],
        help='decrypt text')
    dec_parser.add_argument('-k', '--keylist', default=DEFAULT_KEY_LIST,
        help='path to key list file [default: %(default)s]')
    dec_parser.add_argument('-c', '--ciphertext',
        help='ciphertext string to decrypt; prompted if omitted')
    dec_parser.set_defaults(subcommand=decrypt)

    # create the sub-parser for generating key lists

    kg_parser = subparsers.add_parser('keygen', aliases=['kg'],
        description='Generate key list file',
        help='generate key list')
    kg_parser.add_argument('-f', '--file', default=DEFAULT_KEY_LIST,
        help='path to key list file [default: %(default)s]')
    kg_parser.add_argument('-o', '--overwrite', action='store_true',
        help='overwrite key list file if it exists')
    kg_parser.add_argument('-s', '--start', metavar='XX',
        type=validate_key_list_indicator,
        help='starting indicator; if omitted, random indicators are used')
    kg_parser.add_argument('-n', '--number', type=validate_num_key_lists, default=1,
        help='number of key lists to generate [default: %(default)s]')
    kg_parser.set_defaults(subcommand=keygen)

    args = parser.parse_args(args=argv)

    log_level = getattr(logging, args.log.upper())
    logging.basicConfig(level=log_level, format='%(message)s')

    try:
        args.subcommand(args)
    except EnvironmentError as ex:
        sys.exit('{}\n'.format(ex))
    except KeyboardInterrupt:
        sys.exit('Interrupted\n')
    except M209Error as ex:
        sys.exit('{}\n'.format(ex))


if __name__ == '__main__':
    main()
