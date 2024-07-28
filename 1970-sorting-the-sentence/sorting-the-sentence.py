class Solution:
    def sortSentence(self, s: str) -> str:
        result = ""
        words = s.split()
        word = sorted(words, key = lambda x : int(x[-1]))
        for i in word:
            new = i[0:len(i) -1]
            result += new + " "
        y = result.strip()
        return y