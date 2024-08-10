from typing import List
from collections import defaultdict
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic1 = defaultdict(list)
        word1 = "qwertyuiop"
        word2 = "asdfghjkl"
        word3 = "zxcvbnm"
        for word in words:
            if all(c in word1 for c in word.lower()):
                dic1["word1"].append(word)
            elif all(c in word2 for c in word.lower()):
                dic1["word2"].append(word)
            elif all(c in word3 for c in word.lower()):
                dic1["word3"].append(word)
        result = []
        for key, values in dic1.items():
            if values:  
                result.extend(values)
        return result
