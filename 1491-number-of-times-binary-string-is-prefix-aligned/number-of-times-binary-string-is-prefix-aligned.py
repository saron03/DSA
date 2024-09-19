class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        binary = [0] * n
        count = 0
        max_index = 0
        
        for i in range(n):
            binary[flips[i] - 1] = 1
            max_index = max(max_index, flips[i])  # Track the maximum index flipped
            
            # Check if the prefix [1, i] is all blue
            if max_index == i + 1:
                count += 1
        
        return count
