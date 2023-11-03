class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res = skill[0]*skill[-1]
        exp_sum = skill[0]+skill[-1]
        l, r = 1, len(skill)-2
        while l < r:
            if skill[l] + skill[r] != exp_sum: return -1
            res += skill[l]*skill[r]
            l += 1
            r -= 1
        return res