class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        count = 0
        left, right = 0, len(people) - 1
        while left < right:
            if people[right] == limit:
                count +=1
                right -=1
            elif people[left] + people[right] == limit:
                count +=1
                left +=1
                right-=1
            elif people[left] + people[right] > limit:
                right -=1
                count +=1
            else:
                count +=1
                left +=1
                right -=1
        if left == right:
            count +=1
        return count



        