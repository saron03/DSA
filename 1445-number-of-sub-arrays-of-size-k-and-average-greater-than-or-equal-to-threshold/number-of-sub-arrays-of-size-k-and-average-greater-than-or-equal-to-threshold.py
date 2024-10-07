class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        total = sum(arr[0:k])
        if total/ k >= threshold:
            count +=1
        i = 1
        while i < len(arr) - k +1:
            total = total - arr[i-1] + arr[i +k-1]
            if total/k >= threshold:
                count +=1
            i +=1
        return count 