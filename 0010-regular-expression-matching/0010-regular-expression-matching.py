class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp 테이블 크기 결정
        m, n = len(s), len(p)

        # dp 테이블 초기화
        dp = [[False] * (n+1) for _ in range(m+1)]

        # 빈 문자열과 빈 패턴이 매칭되는 경우
        dp[0][0] = True

        # 패턴 p에서 *를 고려한 초기 상태 설정
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2] # *는 0번 이상 반복될 수 있으므로 직전문자를 제거한 경우와 동일
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]

                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n] 