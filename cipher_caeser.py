from cipher_symmetric import SymmetricCipherMixin 

class CaeserCipher(SymmetricCipherMixin): #Q: SymmetricCipherInterface (add as superclass?)
  def __init__(self, shift, message):
    self._key = shift # should it be key-1? or should we assume key takes values 0 onwards (say up to 25), but actually can be any integer the way the code has been written due to mod26 implementation
    self._plain_text = message
    self.encrypted_text = self.encrypt(message, shift)

  @staticmethod
  def __letterValue(letter):
    # letter A is value 65 in ascii. (only for upper case!! - letter 'a' is value 97)
    # traditionally can just assume plain_text is all upper case, normal A-Z letters for CaeserCipher cipher.
    return ord(letter.upper()) - 65

  @staticmethod
  def __getShiftedAsciiValueFromLetterValue(letter_value, shift):
    return (letter_value+shift)%26 + 65

  def encrypt(self, plain_text=None, shift=None):
    if plain_text is None:
      plain_text=self._plain_text
    if shift is None:
      shift=self._key
    encrypted_text=''
    for letter in plain_text:
      encrypted_text += chr(self.__getShiftedAsciiValueFromLetterValue(self.__letterValue(letter), shift))
    return encrypted_text

  def decrypt(self, cipher_text=None, shift=None):
    if cipher_text is None:
      cipher_text=self.encrypted_text
    if shift is None:
      shift=self._key
    decrypted_text=''
    unshift = -shift
    for letter in cipher_text:
      decrypted_text += chr(self.__getShiftedAsciiValueFromLetterValue(self.__letterValue(letter), unshift))
    return decrypted_text

# TODO: turn print() statements below into tests
# test class initialisation
# alice_cipher = CaeserCipher(5, 'zasdf') #keep key in secure env variable, and message as data request or from secure database.

#test encrypt and decrypt functions (with default values)
# print('e1', alice_cipher.encrypt())
# print('d1', alice_cipher.decrypt())

#test updateKey
# print(alice_cipher.encrypted_text)
# alice_cipher.updateKey(7)
# print(alice_cipher.encrypted_text)

# #test updateMessage
# print(alice_cipher.encrypted_text)
# alice_cipher.updateMessage('abcdef')
# print(alice_cipher.encrypted_text)

# TODO: make input of plain_text more flexible (rather than just A-Z characters, e.g. at least with capitilisation)
# TODO: add pydantic 
# how to comment code in a class? add versioning/author etc.

# GET CODE REVIEW/FEEDBACK ON:
# correct use of single/double underscores? in particular should i use double underscore for things like self.__key and __plain_text?
# correct user of @staticmethod?
# what variables should the class store?
# which methods should be 'private' and which 'public'?
# default values in encrypt, decrypt function
# note that key for a particular instance can easily be deduced by using public encrypt() method on any piece of text (e.g. print(encrypt('a'))) (or using updateMesssage('a') method followed by printing encryptedText field). how to improve security of class if it is possible to do so?
