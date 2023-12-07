class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones_pos = [i for i in range(len(boxes)) if boxes[i] == '1']
        moves = []
        for i in range(len(boxes)):
            move = 0
            for one_pos in ones_pos:
                move += abs(one_pos - i)
            moves.append(move)
        return moves