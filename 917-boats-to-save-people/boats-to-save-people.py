class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        count = 0
        left, right = 0, len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1

        return count

            