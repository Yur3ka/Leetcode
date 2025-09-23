class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1 = version1.split('.')
        n2 = version2.split('.')
        k = max(len(n1),len(n2))
        for i in range(k):
            if i >= len(n1):
                curr1 = 0
            else:
                curr1 = int(n1[i])
            if i >= len(n2):
                curr2 = 0
            else:
                curr2 = int(n2[i])
            if curr1 > curr2:
                return 1
            elif curr1 < curr2:
                return -1
        return 0