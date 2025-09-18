class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_to_user = {}
        self.task_to_priority = {}
        self.priority_heap = []

        for task in tasks:
            self.add(task[0], task[1], task[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_to_user[taskId] = userId
        self.task_to_priority[taskId] = priority
        heapq.heappush(self.priority_heap, (-priority, -int(taskId), taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_to_priority[taskId] = newPriority
        heapq.heappush(self.priority_heap, (-newPriority, -int(taskId), taskId))

    def rmv(self, taskId: int) -> None:
        del self.task_to_user[taskId]
        del self.task_to_priority[taskId]

    def execTop(self) -> int:
        while self.priority_heap:
            priority, _, taskId = heapq.heappop(self.priority_heap)
            if taskId in self.task_to_priority and self.task_to_priority[taskId] == -priority:
                userId = self.task_to_user[taskId]
                self.rmv(taskId)
                return userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()