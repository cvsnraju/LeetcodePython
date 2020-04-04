class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    spos = 0
    tpos = 0
    
    ls = len(s)
    lt = len(t)
    
    if s==t or ls==0:
      return True
    if ls>lt: 
      return False
    ch=s[spos]
    c=0
    while tpos<lt:
      if t[tpos] == ch:
        c+=1
        if c==ls:
          return True
        spos+=1
        ch=s[spos]
      tpos+=1
    return False
        