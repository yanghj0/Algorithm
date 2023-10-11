class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def gwalho(left, right, s): #(열린괄호, 닫힌괄호, 생성된문자열)
            if len(s) == n*2:
                res.append(s)
                return
            if left < n:
                gwalho(left+1, right, s+'(')
            if right < left:
                gwalho(left, right+1, s+')')
        gwalho(0,0,'')
        return res