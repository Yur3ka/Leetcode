
class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.task_map = {}  # Maps taskId to (userId, priority)
        self.task_heap = []  # Max-heap to store (-priority, -taskId, userId)
        
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        """
        Thêm một task với taskId và priority cho user có userId.
        """
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.task_heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.task_map:
            userId, _ = self.task_map[taskId]
            self.task_map[taskId] = (userId, newPriority)
            heapq.heappush(self.task_heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.task_heap:
            priority, taskId, userId = heapq.heappop(self.task_heap)
            taskId = -taskId
            priority = -priority
            if taskId in self.task_map and self.task_map[taskId] == (userId, priority):
                del self.task_map[taskId]
                return userId
        return -1