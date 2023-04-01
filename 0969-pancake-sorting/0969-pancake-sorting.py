class Solution(object):
    def pancakeSort(self, arr):
        sol = []
        n = len(arr)
        for i in range(n, 0, -1):
            ind = arr.index(i) + 1
            if ind == 1:
                sol.append(i)
                sub_arr = arr[:i]
                sub_arr.reverse()
                arr = sub_arr + arr[i:]
            else:
                sol.append(ind)
                sub_arr = arr[:ind]
                sub_arr.reverse()
                arr = sub_arr + arr[ind:]

                sol.append(i)
                sub_arr = arr[:i]
                sub_arr.reverse()
                arr = sub_arr + arr[i:]
        return sol