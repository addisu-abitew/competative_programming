class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = self.parse_to_int(num1)
        num2_int = self.parse_to_int(num2)
        return str(num1_int * num2_int)

    def parse_to_int(self, str_num):
        int_num = 0
        for num in str_num:
            for dig in range(10):
                if num == str(dig):
                    int_num = int_num * 10 + dig
        return int_num