class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols, currColor = len(image), len(image[0]), image[sr][sc]
        def fill(sr, sc):
            if not(-1<sr<rows) or not(-1<sc<cols) or  image[sr][sc] != currColor or  image[sr][sc]==color: return
            image[sr][sc] = color
            fill(sr-1,sc)
            fill(sr+1,sc)
            fill(sr,sc-1)
            fill(sr,sc+1)
        fill(sr, sc)
        return image