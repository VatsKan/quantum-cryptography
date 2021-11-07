from cipher_symmetric import SymmetricCipherMixin
import math

#transposition is rearranging of the letters
class TranspositionRailfenceCipher(SymmetricCipherMixin):
  def __init__(self, depth, message):
    self._key = depth 
    self._plain_text = message
    self.encrypted_text = self.encrypt(message, depth)

  # complexity of my encrypt algorithm: O(n)
  def encrypt(self, plain_text=None, depth=None):
    if plain_text is None:
      plain_text=self._plain_text
    if depth is None:
      depth=self._key
    
    levels = {}
    for letterIndex in range(len(plain_text)):
      letter = plain_text[letterIndex]
      if letterIndex%depth in levels:
        levels[letterIndex%depth] += letter
      else:
        levels[letterIndex%depth] = '' + letter
    
    encrypted_text=''
    for i in range(len(levels)):
      encrypted_text += levels[i]
    
    return encrypted_text
     
  def decrypt(self, encrypted_text=None, depth=None):
    if encrypted_text is None:
      encrypted_text=self.encrypted_text
    if depth is None:
      depth=self._key

    decrypt_depth = math.ceil(len(encrypted_text)/depth)
    return self.encrypt(encrypted_text, decrypt_depth)

# TODO: create tests for below:
# alice = TranspositionRailfenceCipher(3, 'hello')
# print(alice.encrypted_text)
# print(alice.decrypt())
# alice.updateMessage('jimmy hendrix is cool')
# print(alice.encrypted_text)
# print(alice.decrypt())
# print(alice.__dir__())