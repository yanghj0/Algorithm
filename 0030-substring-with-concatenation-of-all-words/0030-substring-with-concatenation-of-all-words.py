class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        total_len = word_len * len(words)
        # words 배열 문자열 빈도 계산
        # word_cnt = {'foo': 2, 'bar': 1}
        word_cnt = Counter(words) 
        result = []

        for i in range(word_len):
            left = i
            right = i
            cur_cnt = Counter()

            while right + word_len <= len(s):
                word = s[right:right+word_len] # 현재 윈도우의 문자열
                right += word_len # 오른쪽 포인터 이동
                cur_cnt[word] += 1 # 현재 문자열 빈도 증가

                while cur_cnt[word] > word_cnt[word]:
                    left_word = s[left:left+word_len]
                    left += word_len
                    cur_cnt[left_word] -= 1

                if right - left == total_len:
                    result.append(left)
        return result