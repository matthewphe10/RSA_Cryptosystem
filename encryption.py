#  -------------------
# | encryption module |
#  -------------------
# Input: a message and public key
# Output: the encrypted message (ciphertext.txt)


def encrypt():
    # open the message file and read it in as a long integer
    with open('message.txt', 'r') as g:
        message = long(g.readline())
    # get the public key and our exponent
    with open('public_key.txt', 'r') as f:
        public = long(f.readline())
        exponent = long(f.readline())
    # encrypt the message with the given public key and exponent then save it
    ciphertext = pow(message, exponent, public)
    with open('ciphertext.txt', 'w') as m:
        print >> m, ciphertext
