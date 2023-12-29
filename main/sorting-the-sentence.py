class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        sorted_words = ["placeholder"]*len(words)
        for word in words:
            sorted_words[int(word[len(word)-1])-1] = word[:-1]
        sorted_sentence = ""
        for word in sorted_words:
            sorted_sentence += word + ' '
        return sorted_sentence[:-1]
        