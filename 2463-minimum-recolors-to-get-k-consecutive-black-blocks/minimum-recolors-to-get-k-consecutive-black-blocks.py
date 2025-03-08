class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = float("inf")  
        w_count = 0  
        j = 0  
        for i in range(len(blocks)):
            if blocks[i] == 'W':  
                w_count += 1  

            if i - j + 1 > k:  
                if blocks[j] == 'W':  
                    w_count -= 1  
                j += 1  

            if i - j + 1 == k:  
                count = min(count, w_count)

        return count