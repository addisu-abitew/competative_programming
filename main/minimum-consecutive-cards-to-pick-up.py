class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_cards = float('inf')
        seen = {}
        for i, card in enumerate(cards):
            if card in seen:
                min_cards = min(min_cards, i-seen[card]+1)
            seen[card] = i
        return min_cards if min_cards != float('inf') else -1