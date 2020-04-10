from collections import defaultdict
class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
            # corner case
    if len(s) != len(t):
      return False

    # creat two dicts
    dic_s = collections.defaultdict(list)
    dic_t = collections.defaultdict(list)

    # key: character value: list of index on the same value
    for i in range(len(s)):
      dic_s[s[i]].append(i)
    for i in range(len(t)):
      dic_t[t[i]].append(i)

    # compare two dictionary's value
    if list(dic_s.values()) == list(dic_t.values()):
      return True
    return False
        