class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = [0]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                score.append(0)
            else:
                li = stack.pop()
                if i-li>1:
                    score.append(score[-1]*2 + score[li])
                else:
                    score.append(1 + score[li])
        return score[-1]