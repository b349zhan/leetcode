from typing import List
def maxPoints(points: List[List[int]]) -> int:
    if len(points)<=2: return len(points)
    ks = {}
    maxCount = -1
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            A, B = points[i], points[j]
            if B[0]==A[0]: 
                k=float('inf')
                b=A[0]
            else: 
                k=(B[1]-A[1])/(B[0]-A[0])
                b=A[1]-A[0]*k
            if (k, b) not in ks:
                ks[(k, b)]=set()
            ks[(k, b)].add(tuple(A))
            ks[(k, b)].add(tuple(B))
            maxCount = max(maxCount, len(ks[(k, b)]))
    return maxCount
