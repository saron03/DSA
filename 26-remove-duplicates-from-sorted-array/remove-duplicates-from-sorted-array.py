class Solution(object):
    def removeDuplicates(self, nums):
        i,j= 0, 0
        count = 0
        for k in range(len(nums)-1):
             if nums[k] == nums[k+1]:
                nums[k] = "_"
        while i < len(nums):
            if nums[i] != "_":
                nums[i], nums[j] = nums[j], nums[i]
                j +=1
                count +=1
            i +=1
        return count
        
        

        