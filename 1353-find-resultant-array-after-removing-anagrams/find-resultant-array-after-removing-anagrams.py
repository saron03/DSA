class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        letter_counts = {}
        for word in words:
            letter_counts[word] = Counter(word)
        res = []
        i,j = 0,1
        while j < len(words):
            if letter_counts[words[j]] == letter_counts[words[i]]:
                j +=1
            else: 
                res.append(words[i])
                i = j
                j +=1
        res.append(words[i])

        return res





