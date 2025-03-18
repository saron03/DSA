class Solution(object):
    def makeFancyString(self, s):
        prev = s[0]
        frequency = 1
        ans = s[0]

        for i in range(1, len(s)):
            if s[i] == prev:
                frequency += 1
            else:
                prev = s[i]
                frequency = 1

            if frequency < 3:
                ans += s[i]

        return ans