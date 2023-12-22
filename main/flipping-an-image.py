class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        for row in range(rows):
            for col in range(math.ceil(cols/2)):
                last = cols-col-1
                if image[row][col] == image[row][last]:
                    inverted = 1 - image[row][col]
                    image[row][col] = image[row][last] = inverted
        return image