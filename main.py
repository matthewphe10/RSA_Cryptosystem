#  -------------
# | main module |
#  -------------
# Input: none
# Output: none
# Driver module that generates the keys, encrypts a given message, then decrypts it
import decryption
import encryption
import key_setup


def main():
    # generate keys
    key_setup.keygen()
    # encrypt message
    encryption.encrypt()
    # decrypt message
    decryption.decrypt()


if __name__ == "__main__":
    main()
