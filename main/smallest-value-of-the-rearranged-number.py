class Solution:
    def smallestNumber(self, num: int) -> int:
        if num >= 0:
            digs = sorted(list(str(num)))
            for i in range(len(digs)):
                if digs[i] != '0':
                    digs[i], digs[0] = digs[0], digs[i]
                    break
            digs = [str(x) for x in digs]
            return int(''.join(digs))
        else:
            digs = sorted(list(str(num)[1:]), reverse=True)
            digs = [str(x) for x in digs]
            return -1 * int(''.join(digs))