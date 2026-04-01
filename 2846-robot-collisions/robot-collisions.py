class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        ans = []
        pos = []
        for i in range(len(healths)):
            pos.append((positions[i],healths[i],directions[i],i))
        pos.sort()
        for i in range(len(pos)):
            if pos[i][2] == 'R':
                stack.append((pos[i][1],pos[i][3]))
            else:
                curr = pos[i][1]
                while stack:
                    last,idx = stack.pop()
                    if curr == last:
                        curr = -1
                        break
                    elif curr < last:
                        curr = -1
                        last -= 1
                        stack.append((last,idx))
                        break
                    else:
                        curr -= 1
                if curr != -1:
                    ans.append((curr,pos[i][3]))
        ans.extend(stack)
        ans.sort(key=lambda x:x[1])
        res = [i for i,_ in ans]
        return res