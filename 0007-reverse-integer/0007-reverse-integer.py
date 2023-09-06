class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            result = int(str(x)[::-1])
        elif x < 0:
            result = -1 * int(str(x*-1)[::-1])
        else:
            result = 0

        return result if result in range(-2**31, 2**31) else 0