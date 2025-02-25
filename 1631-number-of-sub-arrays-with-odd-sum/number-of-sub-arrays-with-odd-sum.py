class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even_count = []
        evens = 1
        for num in arr:
            if num%2==1:
                even_count.append(evens)
                evens = 1
            else:
                evens += 1
        if even_count:
            even_count.append(evens)
        ans = 0
        n = len(even_count)
        past = [0]*n
        for i in range(n - 2, -1, -1):  # Duyệt từ i = n-2 đến 0
            past[i] = even_count[i + 1] + (past[i + 2] if i + 2 < n else 0)

        for i in range(n):
            ans += even_count[i]*past[i]
        return ans %(10**9+7) 