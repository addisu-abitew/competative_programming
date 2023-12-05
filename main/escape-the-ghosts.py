class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        nearest_ghost_location = min(ghosts, key = lambda location: self.distance(location, target))
        nearest_ghost_distance_to_target = self.distance(nearest_ghost_location, target)
        my_distance_to_target = self.distance([0, 0], target)
        return my_distance_to_target < nearest_ghost_distance_to_target
    
    def distance(self, location, target):
        return abs(location[0]-target[0]) + abs(location[1]-target[1])