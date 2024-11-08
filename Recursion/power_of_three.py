# Power of Three
# check if the number on recursively dividing by 3 ends up at 1 - if yes, then it is a multiple of 3 
# time complexity - O(log n)
# space complexity - O(log n)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        print(n)
        # base case
        if n == 1:
            return True
        if n % 3 != 0 or n == 0:
            return False
        return self.isPowerOfThree(n//3)
