class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        ordered = []
        for num in arr2:
            for _ in range(counter[num]):
                ordered.append(num)
            del counter[num]
        for num, rep in sorted(counter.items()):
            for _ in range(rep):
                ordered.append(num)
        return ordered