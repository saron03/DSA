class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(capacity):
            cur_sum = 0
            days_count = 1
            for weight in weights:
                cur_sum += weight
                if cur_sum > capacity:
                    days_count += 1
                    cur_sum = weight
                    if days_count > days:
                        return False
            return True

        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high)//2
            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low