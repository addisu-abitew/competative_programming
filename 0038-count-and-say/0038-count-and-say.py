class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"

        encoded = "1"
        for i in range(1, n):
            encoded = self.encode(encoded)
            
        return encoded

    def encode(self, s):
        compressed = ""
        cur_char = s[0]
        cur_count = 1
        for char in s[1:]:
            if char == cur_char:
                cur_count += 1
            else:
                compressed += str(cur_count) + cur_char
                cur_char = char
                cur_count = 1
        compressed += str(cur_count) + cur_char
        return compressed