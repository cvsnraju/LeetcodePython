# 415. Add Strings
class Solution:
	def addStrings(self, num1: str, num2: str) -> str:
		def StringtoInt(num):
			value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
			result = 0
			for i in num:
				result = result*10 + value[i]
			return result
		num1 = StringtoInt(num1)
		num2 = StringtoInt(num2)

		return str(num1+num2)