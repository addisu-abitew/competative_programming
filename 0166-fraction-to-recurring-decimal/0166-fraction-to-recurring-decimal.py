class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"

        neg = numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0
        numerator, denominator = abs(numerator), abs(denominator)
        ans = "0" if numerator < denominator else ""
        seen = {}
        while numerator:
            if numerator >= denominator:
                ans += str(numerator // denominator)
                numerator %= denominator
            elif numerator in seen:
                parts = ans.split(".")
                integer, decimal = parts[0], parts[1]
                idx = seen[numerator]
                non_repeating = decimal[:idx]
                repeating = decimal[idx:]
                ans = integer + "." + non_repeating + "(" + repeating + ")"
                numerator = 0
            else:
                orginal = numerator
                while numerator < denominator:
                    if "." in ans:
                        if numerator // orginal >= 10:
                            ans += "0"
                    else:
                        ans += "."
                    seen[numerator] = len(ans.split(".")[1])
                    numerator *= 10

        return ans if not neg else "-" + ans