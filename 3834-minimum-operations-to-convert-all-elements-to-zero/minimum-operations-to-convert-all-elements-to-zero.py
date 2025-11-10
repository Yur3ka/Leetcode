class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        c = defaultdict(list)
        for i in range(len(nums)):
            c[nums[i]].append(i)
        num_list = sorted(list(set(nums)))
        zero_pos = [-1,len(nums)]
        if 0 in c:
            zero_pos.extend(c[0])
        zero_pos.sort()
        for i in range(len(num_list)):
            if num_list[i] == 0:
                continue
            temp = set()
            for p in c[num_list[i]]:
                seg = bisect_left(zero_pos,p)
                temp.add(seg)
            ans += len(temp)
            for s in c[num_list[i]]:
                insort(zero_pos, s)
            # zero_pos.sort()
        return ans