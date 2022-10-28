#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self._value = value
    
  def get_value(self):
    return self._value

  def set_value(self, stringVal):
    if (type(stringVal) == str):
      self._value = stringVal
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  # Refactored Solution
  # def __init__(self, value = []):
  #   if (type(value) == str):
  #     self._value = value
  #   else:
  #     print("The value must be a string.") 



  def is_sentence(self):
    if self._value[len(self._value) - 1] == '.':
      return True
    
    return False
    # return self._value.endswith('.')  => Refactored solution
    pass

  def is_question(self):
    if self._value[len(self._value) - 1] == '?':
      return True
    
    return False
    # return self._value.endswith('?')  => Refactored solution

  def is_exclamation(self):
    if self._value[len(self._value) - 1] == '!':
      return True
    
    return False
    # return self._value.endswith('!')  => Refactored solution

  def count_sentences(self):
    def emptyString(string):
      if string == '':
        return False
      else:
        return True

    if self._value == '':
      return 0 
    else:
      replaced_question = self._value.replace('?', '.')
      replaced_exclamation = replaced_question.replace('!', '.')
      filtered = filter(emptyString, replaced_exclamation.split('.'))
      return len(list(filtered))

  pass
