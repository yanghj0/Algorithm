class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['' for _ in range(numRows)]
        cur_row, direction = 0, 1 # 현재 행과 방향 초기화(아래방향으로 이동해야하니까 direction = 1)
        for i in s:
            rows[cur_row] += i
            if cur_row == 0:
                direction = 1
            # 마지막 행이여서 방향값을 바꿔주어야 하는 경우
            elif cur_row == numRows-1:
                direction = -1
            cur_row += direction

            if cur_row <= 0:
                cur_row = 0
            elif cur_row >= numRows:
                cur_row = numRows -1
        return ''.join(rows)