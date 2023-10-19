class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def toBin(num):
            if num==0: return '0'
            binary = ''
            while num > 0:
                if num%2 == 0:
                    binary += '0'
                else:
                    binary += '1'
                num //= 2
            return binary[::-1]
        
        def toDec(binary):
            dec = 0
            for i in range(len(binary)):
                dec = 2*dec + int(binary[i])
            return dec
        return toBin(toDec(a) + toDec(b))