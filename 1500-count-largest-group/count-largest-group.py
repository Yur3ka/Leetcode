class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_of_digits = defaultdict(int)
        sum_of_digits[0] = 0
        def s_digit(a):
            ans = 0
            for digit in str(a):
                ans += int(digit)
            return ans
        for i in range(1,n+1):
            sum_of_digits[s_digit(i)] += 1
        ans = 0
        stack = 0
        for k,v in sum_of_digits.items():
            if v > sum_of_digits[ans]:
                stack = 1
                ans = k
            elif v == sum_of_digits[ans]:
                stack += 1
        return stack