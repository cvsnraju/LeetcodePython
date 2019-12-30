# 258. Add Digits
# Easy

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:

# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.

def addDigits(num):

  # General solution with modulous operator
  # string_num = str(num)
  # if len(string_num) <= 1 :
  #   return num
  # else :
  #   new_number = 0
  #   for k in string_num:
  #     new_number += int(k)
  #   return addDigits(new_number)

  # Congruence rule

  return 1 + (num-1)%9


res = addDigits(38)
print(res)