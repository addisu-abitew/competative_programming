class Solution(object):
    def getRow(self, rowIndex, arr = [1]):
        if rowIndex == 0: return arr
        if len(arr) == 1:
            arr = [1, 1]
        else:
            arr = [1] + self. addRow(arr) + [1]
        return self.getRow(rowIndex-1, arr)
    
    def addRow(self, arr):
        sumRow = []
        for i in range(len(arr)-1):
            sumRow.append(arr[i] + arr[i+1])
        return sumRow