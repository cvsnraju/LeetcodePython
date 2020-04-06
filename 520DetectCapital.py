class Solution:
  def detectCapitalUse(self, word: str) -> bool:
    w = [ 1 + (ord(c) < 91) for c in word]
    return sum(w[1:]) == len(w[1:]) or sum(w) % len(w) == 0