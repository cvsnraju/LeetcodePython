def numsSameConsecDiff( N, K):
    """
    :type N: int
    :type K: int
    :rtype: List[int]
    """
    ans = {x for x in range(1, 10)}
    if N == 1:
        ans.add(0)
    for _ in range(N-1):
        ans2 = set()
        for x in ans:
            d = x % 10
            if d - K >= 0:
                ans2.add(10*x + d-K)
            if d + K <= 9:
                ans2.add(10*x + d+K)
        ans = ans2
        if N == 1:
            ans
    return list(ans)
res = numsSameConsecDiff(2,5)
print(res)