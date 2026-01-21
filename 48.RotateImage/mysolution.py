class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix) - 1
        levelmin = 0
        levelmax = length
        while levelmin <= length // 2:
            minimum = levelmin
            maximum = levelmax
            while minimum < levelmax:
                temp = matrix[levelmin][minimum]
                matrix[levelmin][minimum] = matrix[maximum][levelmin]
                matrix[maximum][levelmin] = matrix[levelmax][maximum]
                matrix[levelmax][maximum] = matrix[minimum][levelmax]
                matrix[minimum][levelmax] = temp
                minimum += 1
                maximum -= 1
                print(matrix, minimum, maximum, levelmin, levelmax)
            levelmin += 1
            levelmax -= 1
        