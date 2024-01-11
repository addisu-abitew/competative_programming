class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Count T's
        changed = 0
        left = -1
        F_pos = []
        max_t = 0
        for right in range(len(answerKey)):
            if answerKey[right] == "F":
                if changed == k:
                    left = F_pos.pop(0)
                else:
                    changed += 1
                F_pos.append(right)
            max_t = max(max_t, right-left)
            
        # Count F's
        changed = 0
        left = -1
        T_pos = []
        max_f = 0
        for right in range(len(answerKey)):
            if answerKey[right] == "T":
                if changed == k:
                    left = T_pos.pop(0)
                else:
                    changed += 1
                T_pos.append(right)
            max_f = max(max_f, right-left)
            
        print(max_t, max_f)
        return max(max_t, max_f)