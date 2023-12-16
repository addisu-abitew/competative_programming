class ATM:

    def __init__(self):
        # notes of $20, $50, $100, $200, and $500
        self.notes = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        withdrawn = [0]*5
        notes = [20, 50, 100, 200, 500]
        for i in range(4, -1, -1):
            count = min(self.notes[i], amount // notes[i])
            amount -= count * notes[i]
            withdrawn[i] = count
        if amount == 0:
            for i in range(5):
                self.notes[i] -= withdrawn[i]
            return withdrawn
        else:
            return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)