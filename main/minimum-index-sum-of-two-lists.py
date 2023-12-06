class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least_pairs = []
        for i in range(len(list1)):
            if list1[i] in list2:
                index_sum = i+list2.index(list1[i])
                if not least_pairs or least_pairs[0][0] > index_sum:
                    least_pairs = [(index_sum, list1[i])]
                elif least_pairs and least_pairs[0][0] == index_sum:
                    least_pairs += [(index_sum, list1[i])]
        result = [pair[1] for pair in least_pairs]
        return result