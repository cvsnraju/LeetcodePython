# 680. Valid Palindrome II
# Given a non-empty string s, you may delete at most one character. 
# Judge whether you can make it a palindrome. 

def Palindrome(s):
    for k in range(len(s)):
        ListS = list(s)
        ListS.pop(k)
        S = "".join(ListS)
        if S == S[::-1] :
            return True
res = Palindrome('abaa')
print(res)