class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        i = 0
        while i < len(position):
            j = i+1
            while j < len(position):
                t1, t2 = (target-position[i])/speed[i], (target-position[j])/speed[j]
                # print(position[i], position[j], t1, t2)
                if position[i]==position[j] or (position[i]>position[j] and t1>=t2):
                    position.pop(j)
                    speed.pop(j)
                elif position[i]<position[j] and t1<=t2:
                    position[i], speed[i] = position[j], speed[j]
                    position.pop(j)
                    speed.pop(j)
                    j = i + 1
                else:
                    j += 1
            i += 1
        return len(position)