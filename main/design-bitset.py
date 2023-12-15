class Bitset:

    def __init__(self, size: int):
        self.bitset = ['0'] * size
        self.flippedBitset = ['1'] * size
        self.ones = 0
        self.flipped = False

    def fix(self, idx: int) -> None:
        if not self.flipped:
            if self.bitset[idx] == '0':
                self.ones += 1
                self.bitset[idx] = '1'
                self.flippedBitset[idx] = '0'
        else:
            if self.bitset[idx] == '1':
                self.ones -= 1
                self.bitset[idx] = '0'
                self.flippedBitset[idx] = '1'

    def unfix(self, idx: int) -> None:
        if not self.flipped:
            if self.bitset[idx] == '1':
                self.ones -= 1
                self.bitset[idx] = '0'
                self.flippedBitset[idx] = '1'
        else:
            if self.bitset[idx] == '0':
                self.ones += 1
                self.bitset[idx] = '1'
                self.flippedBitset[idx] = '0'

    def flip(self) -> None:
        self.flipped = not self.flipped

    def all(self) -> bool:
        return self.ones == len(self.bitset) if not self.flipped else self.ones == 0

    def one(self) -> bool:
        return self.ones >= 1 if not self.flipped else self.ones <= len(self.bitset)-1

    def count(self) -> int:
        return self.ones if not self.flipped else len(self.bitset)-self.ones

    def toString(self) -> str:
        return ''.join(self.bitset) if not self.flipped else ''.join(self.flippedBitset)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()