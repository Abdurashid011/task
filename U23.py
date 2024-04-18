class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        lst = [j for i in grid for j in i]
        l = len(lst)

        for i in range(k):
            lst.insert(0,lst.pop(-1))

        m = len(grid)
        n = len(grid[0])

        s=0
        result = []

        for i in range(m):
            result.append(list(lst[s:s+n]))
            s += n

        return result

print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))