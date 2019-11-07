# 1189. Maximum Number of Balloons
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1
# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        num_b = len(text.split('b'))-1
        num_a = len(text.split('a'))-1
        num_l = (len(text.split('l'))-1)//2
        num_o = (len(text.split('o'))-1)//2
        num_n = len(text.split('n'))-1
        return min(num_b, num_a, num_l, num_o, num_n)