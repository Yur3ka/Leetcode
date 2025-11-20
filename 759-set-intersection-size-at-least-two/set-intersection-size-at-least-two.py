class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[1],-x[0]))
        # print(intervals)
        ans = []
        for s,e in intervals:
            if not ans:
                ans.append(e-1)
                ans.append(e)
            else:
                if  s<=ans[-2] < e:
                    continue
                elif s <= ans[-1] <e:
                    ans.append(e)
                else:
                    ans.append(e-1)
                    ans.append(e)
        # print(ans)
        return len(ans)
