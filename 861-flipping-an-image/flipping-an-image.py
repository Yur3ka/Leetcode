class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            for j in range(n//2):
                image[i][j], image[i][n-1-j] = 1 - image[i][n-1-j], 1- image[i][j]
            if n %2==1:
                image[i][n//2] = 1 - image[i][n//2]
        return image