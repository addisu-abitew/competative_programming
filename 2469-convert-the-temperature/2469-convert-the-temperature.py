class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        def toFahren(temp):
            return temp*1.80 + 32
        def toKelv(temp):
            return temp + 273.15
        
        ans = [toKelv(celsius), toFahren(celsius)]
        return ans