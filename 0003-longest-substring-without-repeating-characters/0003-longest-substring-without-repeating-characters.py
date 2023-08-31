class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {} # 문자와 해당 문자의 인덱스를 저장할 해시맵
        max_len = 0 # 최대 부분 문자열 길이
        start = 0 # 슬라이딩 윈도우의 시작인덱스(길이)

        for end in range(len(s)):
            # 현재 문자가 이미 딕셔너리에 있고, 슬라이딩 윈도우 값과 같거나 길다면
            # 즉, 중복되는 문자가 발견되었다면
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            char_index[s[end]] = end
            max_len = max(max_len, end - start + 1)
        return max_len