class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        # Iterate over each of the startTime and endTime and find the max sum in k window
        max_free = startTime[0]
        if n == k:
            for i in range(k-1):
                max_free += startTime[i+1] - endTime[i]
            max_free += eventTime - endTime[n-1]
            return max_free
        else:
            for i in range(k):
                max_free += startTime[i+1] - endTime[i]

            if n == k + 1:
                cur_free = max_free - startTime[0] + (eventTime - endTime[n-1])
                return max(max_free, cur_free)
            else:
                cur_free = max_free - startTime[0] + (startTime[k+1] - endTime[k])
                max_free = max(max_free, cur_free)
                for i in range(k+1, n-1):
                    cur_free +=  (startTime[i+1] - endTime[i]) - (startTime[i-k] - endTime[i-k-1])
                    max_free = max(max_free, cur_free)
                cur_free += eventTime - endTime[n-1] - (startTime[n-k-1] - endTime[n-k-2])
                max_free = max(max_free, cur_free)
        return max_free





        # # Count free times between each consecutive meetings
        # free_times = [0] * (n + 1)
        # free_times[0] = startTime[0]
        # for i in range(n-1):
        #     free_times[i+1] = startTime[i+1] - endTime[i]
        # free_times[n] = eventTime - endTime[n-1]

        # # Find the maximum sum in k window length
        # max_sum = sum(free_times[0:k+1])
        # for i in range(n-k+1):
        #     max_sum = max(max_sum, max_sum - free_times[i] + free_times[i+k])
        # return max_sum