class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        while i < len(temperatures):
            v = self.checker(temperatures, i)
            if v == 0: break
            i += v
        return temperatures
    
    def checker(self, ts, s):
        if s+1 >= len(ts):
            ts[s] = 0
            return 0
        elif ts[s]<ts[s+1]:
            ts[s] = 1
            return 1
        else:
            tmp = s
            while True:
                v = self.checker(ts, tmp+1)
                if v == 0:
                    ts[s] = 0
                    return 0
                elif ts[s] < ts[tmp+v+1]:
                    ts[s] = (tmp-s)+v+1
                    return (tmp-s)+v+1
                else:
                    tmp += v