class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        return ''.join([word1[i]+word2[i] for i in range(min(len(word1), len(word2)))]+[word1[len(word2):] if len(word1)>len(word2) else word2[len(word1):]])