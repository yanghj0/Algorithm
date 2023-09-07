class Solution:
    def myAtoi(self, s: str) -> int:
        num = []
        sign = 1

        # 시작 공백 제거
        s = s.lstrip()

        # 입력 문자열이 비어 있는 경우
        if not s:
            return 0

        # 부호 확인
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # 숫자 변환
        for i in s:
            if i.isdigit():
                num.append(i)
            else:
                break
        if not num:
            return 0
        result = sign * int(''.join(num))
        
        if result > 2**31-1:
            return 2**31-1
        elif result < -2**31:
            return -2**31
        else:
            return result
