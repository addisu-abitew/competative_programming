from collections import Counter
    
class Solution:
    def findOriginalArray(self, changed):
        if len(changed)%2 == 1: return []
        original = []
        count = Counter(changed)
        changed.sort()
        for val in changed:
            if val == 0:
                if count[0] >= 2:
                    count[0] -= 2
                    original.append(0)
                elif count == 1: return []
            elif count[val]:
                if count[val] and count[val*2]:
                    count[val] -= 1
                    count[val*2] -= 1
                    original.append(val)
                else: return []
        return original