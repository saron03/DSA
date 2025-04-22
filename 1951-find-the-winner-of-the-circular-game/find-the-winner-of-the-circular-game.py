class Solution(object):
    def findTheWinner(self, n, k):
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        j=0
        while len(arr)>1:
            j=(j+k-1) % len(arr)
            arr.pop(j)
        return arr[0]

