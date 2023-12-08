class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = {}
        for winner, loser in matches:
            losers[loser] = losers.get(loser, 0) + 1
            winners.add(winner)
        return [sorted([winner for winner in winners if winner not in losers]), sorted([loser for loser in losers if losers[loser] == 1])]