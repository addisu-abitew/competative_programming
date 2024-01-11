class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []
        i = 0
        for item in firstList:
            a, b = item
            while i < len(secondList) and secondList[i][0] <= b:
                # print(item, secondList[i])
                c, d = secondList[i]
                
                x, y = max(a, c), min(b, d)
                if x <= y:
                    intersection.append([x, y])
                if b < d:
                    break
                i += 1
        return intersection