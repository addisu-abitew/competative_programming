class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # sort by the difference between actual and minimum giving better priority for those with higher minimum if actual and minimum are equal
        tasks.sort(key=lambda x: (x[1] - x[0], x[1]), reverse=True)
        min_effort = cur_effort = 0
        for task in tasks:
            if cur_effort < task[1]:
                min_effort += task[1] - cur_effort
                cur_effort = task[1]
            cur_effort -= task[0]
        return min_effort