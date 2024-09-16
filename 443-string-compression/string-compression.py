class Solution:
    def compress(self, chars: List[str]) -> int:
            s = []
            dic1 = {}
            i = 0
            while i < len(chars):
                char = chars[i]
                count = 1
                while i + 1 < len(chars) and chars[i + 1] == char:
                    count += 1
                    i += 1
                s.append(char)
                if count > 1:
                    for digit in str(count):
                        s.append(digit)
                i += 1
                  
            chars[:] = s
            return len(chars)