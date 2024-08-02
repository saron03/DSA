class Solution:
    def isPalindrome(self, s: str) -> bool:
        word_final = ""
        for i in s:
            if i.isalnum():  
                word_final += i.lower()  

        return word_final == word_final[::-1]  