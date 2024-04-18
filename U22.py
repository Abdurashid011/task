class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        def prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        primero = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j or i+j == len(nums) - 1:
                    if prime(nums[i][j]) == True and nums[i][j] > primero:
                            primero = nums[i][j]
        return primero

print(Solution().diagonalPrime(nums = [[1,2,3],[5,6,7],[9,10,11]]))