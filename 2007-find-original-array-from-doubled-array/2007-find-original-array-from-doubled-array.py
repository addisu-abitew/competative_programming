# class Solution:
#     def findOriginalArray(self, changed: List[int]) -> List[int]:
#         if len(changed)%2 == 1: return []
#         original = []
#         i = 0
#         while i < len(changed):
#             temp_i = i
#             # find the base value
#             while changed[i] != 0 and changed[i]/2 in changed:
#                 i = changed.index(changed[i]/2)
                
#             cur val = changed[i]
#             changed.pop(i)
#             if changed[]

#             multiples = []
#             # find multiples of the base val and delete them from the list
#             while i < len(changed):
#                 cur_val = changed[i]
#                 changed.pop(i)
#                 if cur_val in changed:
#                     multiples.append(cur_val)
#                     i = changed.index(cur_val)
#                 elif cur_val*2 in changed:
#                     multiples.append(cur_val)
#                     i = changed.index(cur_val*2)
#                 else: break
#             if temp_val != 0:
#                 multiples.append(changed[i])
#                 changed.pop(i)
#             if len(changed) % 2 == 1: 
#                 print('odd length', multiples)
#                 return []
#             for i in range(len(multiples)//2):
#                 original.append(multiples[i*2])
#             i = temp_i + 1
#         return original
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