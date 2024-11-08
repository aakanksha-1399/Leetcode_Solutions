# check if the number is divisible by 2 if yes till the end, then it is power of two, else it is not
# time complexity - O(logn)
# space complexity - O(logn)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print(n//2)
        if n == 1:
            return True
        if n % 2 == 1 or n == 0:
            return False

        return self.isPowerOfTwo(n//2)
        
