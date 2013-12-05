#!/usr/bin/python
import sys
import string
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def _rot13(s):
    """ convert a string to its ROT13 equivalent. """
    rot13 = string.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return string.translate(s, rot13)


def _ascii_to_64(s):
    """ convert an ascii string to its base 64 equivalent """
    pass


def _ascii_to_hex(s):
    tmp = map(ord, s)
    x = [hex(t).lstrip('0x') for t in tmp]
    return ''.join(x)


def _hex_to_ascii(s):
    pass


def _hex_to_binary(s):
    pass


def encrypt(s):
    s = _rot13(s)
    s = _ascii_to_hex(s)
    s = _rot13(s)
    return s

def decrypt(s):
    s = _rot13(s)


if __name__ == '__main__':
    try:
        d = sys.argv[1]
    except:
        d = None
    if d not in ['-c', '-d']:
        logging.info("Usage: python crypt.py (-c|-d) [string]")
        sys.exit(0)

    try:
        s = sys.argv[2]
    except:
        s = None

    if not s:
        s = raw_input("String to convert: ")


    logging.info(encrypt(s))
    print "%x" %encrypt(s)
