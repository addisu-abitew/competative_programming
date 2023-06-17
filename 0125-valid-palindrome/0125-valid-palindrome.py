class Solution(object):
    def isPalindrome(self, s):
        # change the string to lowercase
        s = s.lower()

        # filter the alphanumeric characters from the given string
        filtered = ''
        for letter in s:
            if letter.isalnum():
                filtered += letter
        
        return filtered[::-1] == filtered