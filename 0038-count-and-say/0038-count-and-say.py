class Solution:
    def countAndSay(self, n: int) -> str:
        # 수열의 첫 번째 항을 위한 기본 케이스
        if n == 1:
            return "1"
        
        # (n-1)번째 항을 구하기 위해 재귀적으로 메서드 호출
        previous_term = self.countAndSay(n - 1)
        
        result = ""
        count = 1 # 현재숫자
        
        for i in range(len(previous_term)):
            # 현재 숫자가 다음 숫자와 같다면 카운트를 증가
            if i + 1 < len(previous_term) and previous_term[i] == previous_term[i + 1]:
                count += 1
            else:
                # 그렇지 않다면, 카운트와 해당 숫자를 결과 문자열에 추가
                result += str(count) + previous_term[i]
                # 다음 숫자를 위해 카운트를 1로 리셋
                count = 1
        
        return result