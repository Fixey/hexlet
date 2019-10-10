#method 1
def is_palindrome(word):
  palindrome = ""
  for i in word:
    palindrome = i + palindrome
  return palindrome == word
  
 #method 2
def is_palindrome2(word):
  for i in range(0, len(word)//2):
    if word[i] != word[-i-1]:
      return False
  return True
