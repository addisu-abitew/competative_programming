class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        name_char_count = []
        while i < len(name):
            char = name[i]
            count = 0
            while i+count < len(name) and char == name[i+count]:
                count += 1
            name_char_count.append([char, count])
            i += count
        
        j = 0
        for item in name_char_count:
            if j >= len(typed):
                return False
            char, count = item
            type_count = 0
            while j+type_count < len(typed) and char == typed[j+type_count]:
                type_count += 1
            j += type_count
            if  count > type_count:
                return False
        
        return j == len(typed)