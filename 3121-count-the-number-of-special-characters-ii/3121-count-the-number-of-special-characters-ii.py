class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special_cands = set()
        specials = set()
        denied = set()
        for letter in word:
            lower_letter = letter.lower()
            if lower_letter not in denied:
                if letter == lower_letter:
                    if lower_letter not in specials:
                        special_cands.add(letter)
                    else:
                        denied.add(letter)
                        specials.remove(letter)
                else:
                    if lower_letter in special_cands:
                        specials.add(lower_letter)
                    else:
                        denied.add(lower_letter)
        return len(specials)