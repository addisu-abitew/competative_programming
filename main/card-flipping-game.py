class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        possible_res = set(fronts + backs)
        for front, back in zip(fronts, backs):
            if front == back:
                possible_res.discard(front)
        return min(possible_res) if possible_res else 0