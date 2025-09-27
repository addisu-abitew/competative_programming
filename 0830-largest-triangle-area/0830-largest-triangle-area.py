class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        lengths = []
        n = len(points)
        max_a = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x = points[i][0] - points[j][0]
                    y = points[i][1] - points[j][1]
                    l1 = (x**2 + y**2) ** 0.5
                    
                    x = points[i][0] - points[k][0]
                    y = points[i][1] - points[k][1]
                    l2 = (x**2 + y**2) ** 0.5
                    
                    x = points[k][0] - points[j][0]
                    y = points[k][1] - points[j][1]
                    l3 = (x**2 + y**2) ** 0.5

                    s = (l1 + l2 + l3) / 2
                    a = (s * (s - l1) * (s - l2) * (s - l3)) ** 0.5
                    if max_a < abs(a):
                        max_a = a
        return max_a