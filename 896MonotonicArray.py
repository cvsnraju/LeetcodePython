def isMonotonic(self, A: List[int]) -> bool:
  if A[0] <= A[-1]:
      return all(i-j >=0 for i, j in zip(A[1:], A))
  else:
      return all(i-j >=0 for i, j in zip(A, A[1:]))