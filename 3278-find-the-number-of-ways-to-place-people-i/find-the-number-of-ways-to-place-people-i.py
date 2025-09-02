class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        def is_upper_left(A,B):
            return A[0] <= B[0] and A[1] >= B[1]

        def inside(A,B,P):
            return A[0] <= P[0] <= B[0] and A[1] >= P[1] >= B[1]
        ans = 0

        for i in range(len(points)):
            for j in range(len(points)):
                if j == i:
                    continue
                if is_upper_left(points[j],points[i]):
                    empty = True
                    for k in range(len(points)):
                        if k == i or k == j:
                            continue
                        else:
                            if inside(points[j],points[i],points[k]):
                                empty = False
                                break
                    if empty:
                        ans += 1
        return ans