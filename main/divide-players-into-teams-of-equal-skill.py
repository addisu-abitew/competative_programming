class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = 2*sum(skill)/len(skill)
        count = Counter(skill)
        chemistry = 0
        for cur_skill in skill:
            if total - cur_skill != cur_skill and count[total - cur_skill] == count[cur_skill]:
                chemistry += cur_skill * (total - cur_skill) * count[cur_skill]
                count[total - cur_skill] = 0
                count[cur_skill] = 0
            elif count[cur_skill] % 2 == 0:
                chemistry += (cur_skill ** 2) * (count[cur_skill]//2)
                count[total - cur_skill] = 0
            else:
                return -1
        return int(chemistry)