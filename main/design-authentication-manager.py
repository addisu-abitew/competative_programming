class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = [currentTime, currentTime + self.timeToLive]

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId][1] > currentTime:
            self.tokens[tokenId][1] = max(self.tokens[tokenId][1], currentTime + self.timeToLive)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        unexpired = 0
        for token in self.tokens:
            startTime, endTime = self.tokens[token]
            if startTime <= currentTime and endTime > currentTime:
                unexpired += 1
        return unexpired


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)