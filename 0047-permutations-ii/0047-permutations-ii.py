class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]
        
        def permutation(given_arr, start, perm_list):
            if len(given_arr) - start <= 1:
                return
            for i in range(start, len(given_arr)):
                arr = given_arr.copy()
                arr[start], arr[i] = arr[i], arr[start]
                if start + 2 == len(arr) and arr not in perm_list:
                    perm_list.append(arr)
                permutation(arr, start+1, perm_list)
            return perm_list
        
        return permutation(nums, 0, [])