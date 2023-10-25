class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        maxi = 2**31 - 1
        mini = -2**31

        if dividend == mini and divisor == -1:
            return maxi
        
        minus = dividend * divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        while dividend >= divisor:
            temp, cnt = divisor, 1 # 현재 divisor값, 현재 나눗셈 횟수
            while dividend >= (temp<<1): # 성립할때까지 temp, cnt 증가
                temp <<= 1
                cnt <<= 1
            dividend -= temp
            result += cnt

        return -result if minus else result