class Solution(object):
    def sortArray(self, nums):

        def merge(self, left,right):
            i,j = 0, 0
            merged=[]

            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    merged.append(right[j])
                    j +=1
                elif left[i] < right[j]:
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j])
                    merged.append(left[i])
                    i +=1
                    j+=1
            
            while i < len(left):
                merged.append(left[i])
                i+=1
            
            while j < len(right):
                merged.append(right[j])
                j +=1
            
            return merged

        if len(nums) <= 1:
            return nums

        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return merge(self, left,right)

        