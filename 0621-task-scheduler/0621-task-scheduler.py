class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for task in tasks:
            if task not in d:
                d[task] = 1
            else:
                d[task] += 1
        maxRep = 0
        maxItems = 0
        for rep in d.values():
            if rep > maxRep:
                maxRep = rep
                maxItems = 1
            elif rep == maxRep:
                maxItems += 1
        return max(len(tasks), maxRep + (n*(maxRep - 1)) + (maxItems -1))