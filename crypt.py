#!/usr/bin/python
import sys
import string
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

ENCRYPT = '-e'
DECRYPT = '-d'


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
    tmp = list(s)
    l = []
    ret = ''
    while tmp:
        l.append(''.join([tmp.pop(0), tmp.pop(0)]))
    for i in l:
        ret += chr(int(i, 16))
    return ret


def _hex_to_binary(s):
    pass


def encrypt(s):
    s = _rot13(s)
    s = _ascii_to_hex(s)
    s = _rot13(s)
    return s


def decrypt(s):
    s = _rot13(s)
    s = _hex_to_ascii(s)
    s = _rot13(s)
    return s


if __name__ == '__main__':
    try:
        d = sys.argv[1]
    except:
        d = None
    if d not in [ENCRYPT, DECRYPT]:
        logging.info("Usage: python crypt.py ({0}) [string]".format('|'.join([ENCRYPT, DECRYPT])))
        sys.exit(0)

    try:
        s = ' '.join(sys.argv[2:])
    except:
        s = None

    if not s:
        s = raw_input("String to convert: ")

    if d == ENCRYPT:
        s = encrypt(s)
    elif d == DECRYPT:
        s = decrypt(s)
    logging.info(s)
