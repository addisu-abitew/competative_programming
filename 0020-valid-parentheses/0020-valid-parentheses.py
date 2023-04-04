class Solution(object):
    def isValid(self, s):
        bs = '{(['
        cs = '})]'
        stack = []
        for b in s:
            if b in bs:
                stack.append(bs.index(b))
            else:
                if len(stack)==0: return False
                c = stack.pop()
                if cs[c] != b:
                    return False
        if len(stack)>0:
            return False
        else:
            return True