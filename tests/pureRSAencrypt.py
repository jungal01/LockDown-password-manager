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
    def __init__(self, phrase, message, keysize=2048):
        self._phrase = phrase
        self._message = message
        self.keysize = keysize

    def mkKey(self, keyid='_'):
        key = RSA.generate(self.keysize)
        encrypted_key = key.exportKey(passphrase=self.__phrase, pkcs=8, protection='scryptAndAES256-CBC')

        with open('privateRSAkey_{}.key'.format(keyid), 'wb') as f:
            f.write(encrypted_key)

        with open('publicRSAkey_{}.key'.format(keyid), 'wb') as f:
            f.write(key.publickey().exportKey())

    def RSAencrypt(self, filename, keyid='_', write=False):
        if not os.path.exists('publicRSAkey_{}.key' .format(keyid)):
            self.mkKey(keyid)

        public_key = RSA.importKey(open('publicRSAkey_{}.key' .format(keyid)).read())
        encrypt_cipher = PKCS1_OAEP.new(public_key)
        ciphertext = encrypt_cipher.encrypt(self._message)

        if write:
            with open(filename, 'wb') as ef:
                ef.write(ciphertext)
                ef.close()
        else:
            return ciphertext

    def RSAdecrypt(self, encryptedName, plainName, keyid='_', write=False):
        with open(encryptedName, 'rb') as f:
            ciphertext = f.read()

        private_key = RSA.importKey(open('privateRSAkey_{}.key' .format(keyid)).read(), self.__phrase)
        decrypt_cipher = PKCS1_OAEP.new(private_key)
        plaintext = decrypt_cipher.decrypt(ciphertext)

        if write:
            with open(plainName, 'wb') as f:
                f.write(plaintext)
                f.close()
        else:
            return plaintext

    def encryptFile(self, file, phrase, idx):
        pass

    def decryptFile(self, file, phrase, idx):
        pass


def main():
    file = open('message.txt', 'rb')
    message = file.readline()
    phrase = 'totallyRandomPassPhrase'
    rsa = pureRSA(phrase, message)
    rsa.RSAencrypt('encrypted_message.rsa', 'basic', write=True)

    newRSA = pureRSA(phrase, message)
    newRSA.RSAdecrypt('encrypted_message.rsa', 'little_message', 'basic', write=True)


if __name__ == '__main__':
    main()
