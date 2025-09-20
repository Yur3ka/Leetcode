class Router:

    def __init__(self, memoryLimit: int):
        self.memory = deque()
        self.limit = memoryLimit
        self.cache = set()
        self.des = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (timestamp,source,destination) in self.cache:
            return False
        if len(self.memory) == self.limit:
            temp = self.memory.popleft()
            self.cache.remove(temp)
            self.des[temp[2]].popleft()

        self.memory.append((timestamp,source,destination))
        self.cache.add((timestamp,source,destination))
        self.des[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.memory) == 0:
            return []
        timestamp,source,destination = self.memory.popleft()
        self.cache.remove((timestamp,source,destination))
        self.des[destination].popleft()
        return [source,destination,timestamp]
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.des:
            return 0
        # print(self.des[destination])
        return bisect_right(self.des[destination],endTime) - bisect_left(self.des[destination],startTime)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)