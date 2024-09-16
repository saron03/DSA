class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        one = set(word1)
        two = set(word2)
        count1 = Counter(word1)
        count2 = Counter(word2)
        if len(word1) != len(word2):
            return False
        if one != two:
            return False
        return sorted(count1.values()) == sorted(count2.values())