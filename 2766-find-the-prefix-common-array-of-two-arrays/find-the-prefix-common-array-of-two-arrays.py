class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        dictA = {}
        dictB = {}
        ans = []
        count = 0
        for i in range(len(A)):
            if A[i] == B[i]:
                count += 1
            if A[i] in dictB:
                count += 1
            if B[i] in dictA:
                count += 1
            dictA[A[i]] = True
            dictB[B[i]] = True
            ans.append(count)
        return ans                