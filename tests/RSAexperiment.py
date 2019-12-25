# This is a demo file for using RSA for it's main purposes in this project.
# Once this, and other files like it, are no longer needed, a gist will be made

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes


# the passphrase and message to be passed around
# messages seem to require binary format to work with the API
phrase = 'totallyRandomPassphrase'
message = open('message.txt', 'rb').readline()

# create and export encrypted keys
# according to pycryptodome docs, this is the only way to encrypt a key, though
# protection can be any supported algo
key = RSA.generate(4096)
encrypted_key = key.exportKey(passphrase=phrase, pkcs=8, protection='scryptAndAES256-CBC')

with open('privateRSAkey.key', 'wb') as f:
    f.write(encrypted_key)

with open('publicRSAkey.key', 'wb') as f:
    f.write(key.publickey().exportKey())


# encrypt a message
public_key = RSA.importKey(open('publicRSAkey.key').read())
encrypt_cipher = PKCS1_OAEP.new(public_key)
nonce = get_random_bytes(16)
ciphertext = encrypt_cipher.encrypt(message)
print(ciphertext, type(ciphertext))
with open('encrypted_message.rsa', 'wb') as ef:
    ef.write(nonce+ciphertext)
    ef.close()

# decrypt a message
# because the private key is encrypted, the passphrase needs to be included to
# allow decryption
with open('encrypted_message.rsa', 'rb') as f:
    x = f.read()
private_key = RSA.importKey(open('privateRSAkey.key').read(), phrase)
decrypt_cipher = PKCS1_OAEP.new(private_key)
plaintext = decrypt_cipher.decrypt(x[16:])
print(plaintext, type(plaintext))
