class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = defaultdict(int)
        for word in words:
            count[word] += 1
        ans = 0
        remain = 0
        used = set()
        for key in list(count):
            if key not in used and key[0] != key[1]:
                rv = key[1] + key[0]
                use = min(count[key], count[rv])
                ans += use*4
                used.add(rv)
                used.add(key)
            elif key[0] == key[1]:
                if count[key] % 2 == 0:
                    ans += count[key]*2
                else:
                    ans += (count[key]-1)*2
                    remain = 1
        ans += remain*2
        return ans