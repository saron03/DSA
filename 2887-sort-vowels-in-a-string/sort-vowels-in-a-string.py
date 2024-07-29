class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        extracted_vowels = sorted([ch for ch in s if ch in vowels])
        j = 0
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = extracted_vowels[j]
                j += 1
        s_modified = ''.join(s_list)
        return s_modified

