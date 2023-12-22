class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        # blocking statements
        if n < 3: return False
        if arr[0] > arr[1]: return False
        
        increasing = True
        for i in range(n-1):
            if arr[i] == arr[i+1] or (not increasing and arr[i] < arr[i+1]):
                return False
            if arr[i] > arr[i+1]:
                increasing = False
        return not increasing