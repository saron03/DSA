# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Assuming the guess API is defined
def guess(num):
    # This is a placeholder for the actual API implementation.
    # In the actual problem, this function will be provided.
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        
        while low <= high:
            mid = (low + high) // 2
            result = guess(mid)  # Call the guess API
            
            if result == 0:
                return mid  # Found the correct number
            elif result == -1:
                high = mid - 1  # Guess was too high
            else:  # result == 1
                low = mid + 1   # Guess was too low

# Example usage:
# sol = Solution()
# print(sol.guessNumber(10))  # This would call the guess function as defined

        