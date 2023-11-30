class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        for i in range(len(command)):
            if i+1 < len(command) and command[i] == '(' and command[i+1] == ')':
                ans += 'o'
            elif command[i] != '(' and command[i] != ')':
                ans += command[i]
        return ans