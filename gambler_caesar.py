#!/usr/bin/env python
# coding=utf-8

import string,argparse

alphabet = string.ascii_lowercase

def caesar_encrypt(text, key):
    table = string.maketrans(alphabet, alphabet[key:] + alphabet[:key])
    print text.translate(table)

def caesar_decrypt(text,key):
    if key == 0:
        for key in range(1,26):
            table = string.maketrans(alphabet[key:] + alphabet[:key], alphabet)
            print text.translate(table)
    else:
            table = string.maketrans(alphabet[key:] + alphabet[:key], alphabet)
            print text.translate(table)

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mode', action = 'store', dest = 'mode',required = True, help = 'e/encrypt or d/decrypt')
parser.add_argument('-t', '--text', action = 'store', dest = 'text', required = True, help = 'the text to encrypt or decrypt')
parser.add_argument('-k', '--key', action = 'store', dest = 'key', type=int, required = False, help = 'the number of key')
args = parser.parse_args()

if args.mode.lower() == 'e' or args.mode.lower() == 'encrypt':
    if args.key:
        caesar_encrypt(args.text.lower(),args.key)
if args.mode.lower() == 'd' or args.mode.lower() == 'decrypt':
    if args.key:
        caesar_decrypt(args.text.lower(),args.key)
    else:
        caesar_decrypt(args.text.lower(),0)
