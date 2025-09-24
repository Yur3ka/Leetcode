class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = []
        if (numerator < 0 and denominator> 0)or (numerator > 0 and denominator < 0):
            ans.append('-')
        denominator = abs(denominator)
        numerator = abs(numerator)
        bf = numerator // denominator
        ans.append(str(bf))
        numerator %= denominator
        if numerator == 0:
            return ''.join(ans)
        used = {}
        ans.append('.')
        curr = len(ans)
        used[numerator] = curr
        while numerator != 0:
            numerator*=10
            ans.append(str(numerator//denominator))
            remain = numerator%denominator
            if remain in used:
                ans.insert(used[remain],'(')
                ans.append(')')
                break
            else:
                curr+= 1
                used[remain] = curr
                numerator = remain
        return ''.join(ans)