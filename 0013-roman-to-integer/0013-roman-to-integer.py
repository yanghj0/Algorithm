class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000
        }

        answer = 0
        prev = 0
        for i in s[::-1]:
            v = nums[i]
            if v < prev:
                answer -= v
            else:
                answer += v
            prev = v
        return answer