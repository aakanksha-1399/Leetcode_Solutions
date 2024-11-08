# power of four
# if the number on continuously dividing by 4 gives us 1 - then it is power of four
# time complexity - O(logn)
# space complexity - O(logn)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #base case
        if n == 1:
            return True
        if n % 4 != 0 or n == 0:
            return False
        
        return self.isPowerOfFour(n//4)
        
