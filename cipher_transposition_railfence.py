import math

#transposition is rearranging of the letters
class TranspositionRailfenceCipher:
  def __init__(self, key, message):
    self.__depth = key 
    self.__plain_text = message
    self.encrypted_text = self.encrypt(message, key)

  # complexity of my encrypt algorithm: O(n)
  def encrypt(self, plain_text=None, depth=None):
    if plain_text is None:
      plain_text=self.__plain_text
    if depth is None:
      depth=self.__depth
    
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
      depth=self.__depth

    decrypt_depth = math.ceil(len(encrypted_text)/depth)
    return self.encrypt(encrypted_text, decrypt_depth)

# TODO: create tests for below:
# alice = TranspositionRailfenceCipher(3, 'hello')
# print(alice.encrypted_text)
# print(alice.decrypt())
