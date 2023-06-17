class Solution(object):
    def frequencySort(self, s):
        # count the number of each character in the given string
        count = {}
        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        
        # sort the letters based on their frequency
        sortedFreq = sorted(count.items(), key = lambda entry: entry[1], reverse = True)
        
        sortedStr = ''
        for entry in sortedFreq:
            sortedStr += entry[0]*entry[1]
        
        return sortedStr