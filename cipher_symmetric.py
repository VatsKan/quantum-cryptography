from abc import ABC, abstractmethod

class SymmetricCipherMixin:
  def updateMessage(self, plain_text):
    self._plain_text=plain_text
    self.encrypted_text=self.encrypt(plain_text)

  def updateKey(self, key):
    self._key = key
    self.updateMessage(self._plain_text)

#TODO: figure out/ask how to implement python interfaces and typing+overloading in python properly! Then import interface into files and use.
class SymmetricCipherInterface(ABC, SymmetricCipherMixin):
  def __init__(self, key, message):
    self._key = key 
    self._plain_text = message
    self.encrypted_text=''
  
  @abstractmethod
  def encrypt(self, plain_text: str, key: int) -> str:
    pass

  @abstractmethod
  def decrypt(self, cipher_text: str, key: int) -> str:
    pass 

  @abstractmethod
  def updateMessage(self, plain_text: str) -> None:  
    pass 

  @abstractmethod
  def updateKey(self, key: int) -> None: 
    pass 

