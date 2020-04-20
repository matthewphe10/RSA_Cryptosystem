#  -------------------
# | decryption module |
#  -------------------
# Input: an encrypted message and the private key
# Output: the encrypted message (ciphtertext.txt)


def decrypt():
    # open ciphertext.txt and get the encrypted message
    with open('ciphertext.txt', 'r') as g:
        message = long(g.readline())
    # get the private key
    with open('private_key.txt', 'r') as f:
        private = long(f.readline())
    # get the public key
    with open('public_key.txt', 'r') as f:
        public = long(f.readline())
        exponent = long(f.readline())
    # decrypt the message using the private key
    decrypted_message = pow(message, private, public)
    # save the decrypted message
    with open('decrypted_message.txt', 'w') as n:
        print >> n, decrypted_message
