class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        cur_capacity = capacity
        for i in range(len(plants)):
            if plants[i] <= cur_capacity:
                steps += 1
            else:
                cur_capacity = capacity
                steps += 2*i + 1
            cur_capacity -= plants[i]
        return steps