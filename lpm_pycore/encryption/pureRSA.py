import os
import shutil
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes


class pureRSA:
    """
    ============================================================================
    This class handles all operations for RSA. It has 5 methods. At the moment,
    the homebrew RSA encryption methods are not completed.

    mkKey: generates a public/encrypted private RSA key pair based on keysize.
        It doesn't return anything, but does write the key pairs to individual
        files.

    RSAencrypt: This encrypts a message of (keysize/8)-11 bytes of data and is
        is mostly useful for encrypting randomly generated block cipher keys.
        If write is true, the message will be written to the given filename. If
        there is no RSA key file with the given name, this will automatically
        call mkKey.

    RSAdecrypt: This is the complement to RSAencrypt. Currently it assumes that
        the message to be decrypted is written to a file.

    encryptFile: An unimplemented function for getting around the message
        size limitations of RSA. It's intended use in this app is one of the
        encryption methods for the password file. The full spec for this
        homebrew method is found below. It is expected to be highly
        computationally expensive, but should provide high levels of security.

    decryptFile: An unimplemented complement to encryptFile.
    ============================================================================
    """
    def __init__(self, phrase, message, keysize=2048):
        self._phrase = phrase
        self._message = message
        self.keysize = keysize

    def mkKey(self, keyid='_'):
        key = RSA.generate(self.keysize)
        encrypted_key = key.exportKey(passphrase=self._phrase, pkcs=8, protection='scryptAndAES256-CBC')

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

        private_key = RSA.importKey(open('privateRSAkey_{}.key' .format(keyid)).read(), self._phrase)
        decrypt_cipher = PKCS1_OAEP.new(private_key)
        plaintext = decrypt_cipher.decrypt(ciphertext)

        if write:
            with open(plainName, 'wb') as f:
                f.write(plaintext)
                f.close()
        else:
            return plaintext


    # pure RSA SPEC: user enters longterm key to encrypt. The algo will create
    # a short term key using longterm key+nonce. Nonce is randomly generated 16
    # bytes, and stored like salt in front of the encrypted string. If the
    # message is too large to be stored in one RSA pass, a new nonce is
    # generated and the process is repeated until the entire message is
    # encrypted. All keys are stored in a compressed tar file

    def encryptFile(self, file, phrase, idx):
        raise NotImplementedError()

    def decryptFile(self, file, phrase, idx):
        raise NotImplementedError()
