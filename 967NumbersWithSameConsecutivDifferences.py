def NumbersWithSameConsecutiveDifference(N, K):

    if N == 1:
        return xrange(0,10)


res = NumbersWithSameConsecutiveDifference(1,12)
print(res)