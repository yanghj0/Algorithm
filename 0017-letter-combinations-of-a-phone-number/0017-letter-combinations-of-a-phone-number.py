class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        digit_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtraking(comb, next_d):
            # next_d가 비어있으면 현재 조합을 결과에 추가하고 종료
            if not next_d:
                result.append(comb)
                return

            # 다음 숫자를 가져옴
            curr_d = next_d[0]
            # 문자 가져옴
            word = digit_dict[curr_d]
            # 재귀적으로 문자를 조합에 추가
            for i in word:
                backtraking(comb+i, next_d[1:])

        backtraking('',digits)
        return result