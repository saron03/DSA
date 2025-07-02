from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Frequency map
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Step 2: Bucket sort (index = frequency)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        # Step 3: Collect top k frequent elements
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
