#!/usr/bin/env python

from Crypto.Cipher import AES
import base64
import getpass
import os

# set some aes properties
BLOCK_SIZE = 32
PADDING = '{'
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

# target user
user = "<username here>"

# calculated the needed filling
offset = 32 - len(user)

secret = ""

# fill string with zeros
for i in range(0,offset):
	secret += "0"

# append username to secret
secret += user

# create cipher
cipher = AES.new(secret)

# encode source code
encoded = EncodeAES(cipher, "print \"Hello World\"")

# print result
print 'Encrypted string:', encoded