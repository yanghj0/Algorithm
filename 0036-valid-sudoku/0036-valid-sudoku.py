class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    res += [(i,num),(num,j),(i//3,j//3,num)]
                    # (i, element): 행 i에 숫자 element가 있다
                    # (element, j): 열 j에 숫자 element가 있다
        return len(res) == len(set(res))