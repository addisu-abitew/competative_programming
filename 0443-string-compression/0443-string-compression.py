class Solution(object):
    def compress(self, chars):
        left, right = 0, 0
        count = 0
        while right < len(chars):
            if chars[right] == chars[left]:
                count += 1
            else:
                if count > 1:
                    ptr = left + 1
                    while ptr < right:
                        chars.pop(ptr)
                        right -= 1
                    for di in range(len( str(count))):
                        chars.insert(left+1+di, str(count)[di])
                    right += 1
                left = right
                count = 1
            right += 1
        if count > 1:
            ptr = left + 1
            while ptr < right:
                chars.pop(ptr)
                right -= 1
            for di in range(len( str(count))):
                chars.insert(left+1+di, str(count)[di])
                