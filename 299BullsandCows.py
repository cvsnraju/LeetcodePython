# 299. Bulls and Cows
# Easy

# You are playing the following Bulls and Cows game with your friend: 
# You write down a number and ask your friend to guess what the number is.
# Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows").
# Your friend will use successive guesses and hints to eventually derive the secret number.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        dic = {}
        rpos = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                rpos.append(i)
                dic[secret[i]] = dic.get(secret[i],0) + 1
        for i in rpos:
            if guess[i] in dic and dic[guess[i]] > 0:
                cows += 1
                dic[guess[i]] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'
        
        
        