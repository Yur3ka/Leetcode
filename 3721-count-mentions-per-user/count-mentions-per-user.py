class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ans = [0]* (numberOfUsers)
        count_all = 0
        online = set(i for i in range(numberOfUsers))
        events.sort(key=lambda x: [int(x[1]),-ord(x[0][1])])
        offline = []
        before = float("inf")
        while events:
            if not offline or int(events[0][1]) < offline[0][0]:
                if events[0][0] == "OFFLINE":
                    id_off = int(events[0][2])
                    # if int(events[0][1]) == before:
                        # ans[id_off] -= 1
                    offline.append([int(events[0][1])+60, id_off])
                    online.remove(id_off)
                else:
                    if events[0][2] == "ALL":
                        count_all += 1
                    elif events[0][2] == "HERE":
                        for id in online:
                            ans[id] += 1
                    else:
                        ids = events[0][2].split()
                        for id in ids:
                            id_pm = int(id[2:])
                            ans[id_pm] += 1
                before = int(events[0][1])
                events.pop(0)

            else:
                online.add(offline[0][1])
                offline.pop(0)
        for i in range(len(ans)):
            ans[i] += count_all
        return ans
                        