class Solution(object):
    def maximumWealth(self, accounts):
        maxSum = 0
        for i in range(len(accounts)):
            maxSum =max(maxSum, sum(accounts[i]))
        return maxSum
        