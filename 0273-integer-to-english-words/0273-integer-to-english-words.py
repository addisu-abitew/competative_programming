class Solution(object):
    def numberToWords(self, num):
        if num == 0: return 'Zero'
        num_word = {
            0: '',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred',
            1000: 'Thousand',
            1000000: 'Million',
            1000000000: 'Billion',
        }
        result = ''
        digits = [1000000000, 1000000, 1000, 100]
        for dig in digits:
            if num//dig > 0:
                result += self.numberToWords(num//dig) + ' ' + num_word[dig] + ' '
                num %= dig
        if num > 20:
            result += num_word[num - num%10] + ' '
            if  num%10 > 0:
                result += num_word[num%10] + ' '
        elif num > 0:
            result += num_word[num] + ' '
        return result[:len(result)-1]