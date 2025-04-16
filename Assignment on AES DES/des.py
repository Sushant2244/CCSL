from Crypto.Cipher import DES
from secrets import token_bytes

key = token_bytes(8)

cipher = DES.new(key, DES.MODE_EAX)
nonce = cipher.nonce  

plaintext = input("Enter the plaintext: ")
msg = plaintext.encode()

ciphertext = cipher.encrypt_and_digest(msg)

print("Cipher text is:", ciphertext.hex())

cipher_dec = DES.new(key, DES.MODE_EAX, nonce=nonce)
decrypted_msg = cipher_dec.decrypt(ciphertext)

print("Plain text:", decrypted_msg.decode())

