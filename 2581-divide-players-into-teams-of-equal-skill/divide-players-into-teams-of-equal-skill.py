class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        sum = 0
        target = skill[-1] + skill[0]
        left, right = 0,  len(skill) -1
        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            else:
                sum += (skill[left] * skill[right])
                left +=1
                right -=1
        return sum

        