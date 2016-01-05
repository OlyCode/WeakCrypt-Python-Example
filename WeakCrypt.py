#!/usr/bin/env python

# WeakCrypt.py
# Copyright 2015, Olympia Code LLC
# Author: Joseph Mortillaro
# Contact at: Olympia.Code@gmail.com
#
# All rights reserved.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# Note that the python implementation of WeakCrypt generates different 
# results than the C# and Java implementations because they are using
# different encoding methods (utf8 on Python vs. utf16 for C# and Java).

import hashlib

def encodeText(p_password, p_message):
    oneTimePad = ""
    # Makes oneTimePad
    hash0 = hashlib.sha256(p_password).digest()
    while len(oneTimePad) < len(str(p_message)):
        for x in range(241):
            hash0 = hashlib.sha256(hash0).hexdigest()
        oneTimePad += hash0        
    # Prepares Message
    message = ""
    for x in range(len(p_message)):
        message += str(hex(ord(p_message[x])^ord(oneTimePad[x])))\
                                                        [2:].zfill(2) 
    return message

def decodeText(p_password, p_message):
    oneTimePad = ""
    # Makes oneTimePad
    hash0 = hashlib.sha256(p_password).digest()
    while len(oneTimePad) < len(str(p_message))/2:
        for x in range(241):
            hash0 = hashlib.sha256(hash0).hexdigest()
        oneTimePad += hash0        
    # Decodes Message
    message = ""
    for x in range(0, len(p_message), 2):
        message += chr(int(p_message[x:x+2],16)^ord(oneTimePad[x/2]))
    return message
    
password = "passsword"
message = "This WeakCrypt. This is encrypted using an SHA256 hash as a stream cypher."

A = encodeText(password, message)
print "\nPlaintext:", message
print "Cyphertext:", A, "\n"

B = decodeText(password, A)
print "Cyphertext:", A
print "Plaintext:", B, "\n"
