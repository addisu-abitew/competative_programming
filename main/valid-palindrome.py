class Solution(object):
    def isPalindrome(self, s):
        lower_s = s.lower()
        filtered = ''
        alphanumerics = 'abcdefghijklmnopqrstuvwxyz1234567890'
        for letter in lower_s:
            if letter in alphanumerics:
                filtered += letter
        return filtered == filtered[::-1]