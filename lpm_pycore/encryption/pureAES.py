from Crypto.Cipher import AES
from hashlib import sha3_256
from Crypto.Random import get_random_bytes


class pureAES:

    def __init__(self, key, message):
        self._key = sha3_256(key).digest()
        self._message = message

    def encrypt(self, output='a.aes', file=True):
        if file:
            message = open(self._message, 'rb').read()
        else:
            message = self._message

        cipher = AES.new(self._key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(message)

        with open(output, 'wb') as out:
            [out.write(x) for x in (cipher.nonce, tag, ciphertext)]

    def decrypt(self, output='a.txt', file=True):
        if file:
            with open(self._message, 'rb') as f:
                nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
        else:
            raise NotImplementedError("Decryption of nonfiles not yet supported")

        cipher = AES.new(self._key, AES.MODE_EAX, nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)

        with open(output, 'wb') as ptf:
            ptf.write(plaintext)
