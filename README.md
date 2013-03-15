##Cryptedware##

A proof-of-concept inspired by [this article](http://arstechnica.com/security/2013/03/the-worlds-most-mysterious-potentially-destructive-malware-is-not-stuxnet/).

The "malware" code can only be decoded and executed if the username matches the one used in the encryption process. This should show how malware developers attack special targets.

(The method is less sophisticated than in real malware, but does what it should.)

#encrypt.py#

This script AES-encodes a piece of python code with the target's username. 

#cryptedware.py#

This is the "malware" which tries to decode the code with the machine's username and executes the code if successful.

