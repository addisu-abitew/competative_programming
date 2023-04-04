class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        res = []
        for i in range(len(l)):
            if r[i]-l[i] < 1:
                res.append(False)
                continue
            elif r[i]-l[i] == 1:
                res.append(True)
                continue
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            flag = True
            dif = temp[1]-temp[0]
            for ind in range(1, r[i]-l[i]):
                if temp[ind+1] - temp[ind] != dif:
                    flag = False
                    break
            res.append(flag)
        return res