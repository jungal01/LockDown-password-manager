# This file is to test out a method of pure RSA encryption. It's not
# cryptographically analysed as of yet, but based on other encryption methods,
# it should be secure.
#
# SPEC: user enters longterm key to encrypt. The algo will create a short term
# key using longterm key+nonce. Nonce is randomly generated 16 bytes, and
# stored like salt in front of the encrypted string. If the message is too
# large to be stored in one RSA pass, a new nonce is generated and the
# process is repeated until the entire message is encrypted. All keys are
# stored in a compressed tar file


import os
import shutil
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes


class pureRSA:
    def __init__(self, phrase, file=None, keysize=2048, generate=False, encrypt=True, pure=False, idx='_'):
        self.keysize = keysize
        self.fileId = idx

        if generate:
            self.mkKey(phrase, self.keysize)
        if file is not None:
            if encrypt:
                self.RSAencrypt(file, phrase)
            elif not encrypt:
                self.RSAdecrypt(file, phrase)
        else:
            raise ValueError("File name is required")

    def mkKey(self, phrase, keysize, idx='_'):
        key = RSA.generate(keysize)
        encrypted_key = key.exportKey(passphrase=phrase, pkcs=8, protection='scryptAndAES256-CBC')

        with open('privateRSAkey_{}.key'.format(idx), 'wb') as f:
            f.write(encrypted_key)

        with open('publicRSAkey_{}.key'.format(idx), 'wb') as f:
            f.write(key.publickey().exportKey())

    def RSAencrypt(self, file, phrase):
        if os.path.exists(file):
            message = open(file, 'rb').read()
        message = file
        encrypted_message = open('{}.encypted'.format(file), 'wb')


    def RSAdecrypt(self, file, phrase):
        pass

    def pureEncrypt(self, file, phrase):
        message = open(file, 'rb').read()
        encrypted_message = open(file+'.encypted', 'wb')
        text_limit = (self.keysize//16) - 42
        encrypted_file = open('passwords.rsa', 'wb')

        if os.path.exists('RSAkeyArchive.tar.gz'):
            pass
        else:
            idx = 0
            for i in range(0, len(message), text_limit):
                nonce = get_random_bytes(16).decode('utf-8', errors='surrogateescape')
                self.mkKey(phrase+nonce, self.keysize, idx)
                public_key = RSA.importKey(open('publicRSAkey{}.key'.format(idx)).read())
                encrypt_cipher = PKCS1_OAEP.new(public_key)
                ciphertext = encrypt_cipher.encrypt(i)
                encrypted_file.write(nonce.encode('ascii', errors='surrogateescape')+ciphertext)
                idx += 1

    def pureDecrypt(self, file, phrase):
        pass
