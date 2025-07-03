class Solution:
    def kthCharacter(self, k: int) -> str:
        # if k == 1:
        #     return 'a'

        def get_height(s):
            heigh = 0
            curr = 1
            while curr < s:
                curr*= 2
                heigh += 1
            return heigh
        step = 0
        while k != 1:
            lv = get_height(k)
            k -= 2**(lv-1)
            step += 1
        return chr(ord('a')+(step%26))