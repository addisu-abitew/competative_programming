class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        minTime = 0
        for i in range(len(processorTime)):
            minTime = max(minTime, processorTime[i] + max(tasks[i*4:(i+1)*4]))
        return minTime