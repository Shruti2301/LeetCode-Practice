class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        while x:
            res = res * 10 + x % 10
            x //= 10
        if res.bit_length() > 31:
            return 0
        return res * sign
        
