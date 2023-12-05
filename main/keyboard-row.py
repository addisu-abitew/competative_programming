class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        one_row_words = []
        for org_word in words:
            word = org_word.lower()
            for row in rows:
                if word[0] in row:
                    cur_row = row
                    break
            is_in_one_row = True
            for letter in word:
                if letter not in cur_row:
                    is_in_one_row = False
            if is_in_one_row:
                one_row_words.append(org_word)
        return one_row_words