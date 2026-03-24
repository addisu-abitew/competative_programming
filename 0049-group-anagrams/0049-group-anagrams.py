class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            anagrams[key].append(word)
        return list(anagrams.values())