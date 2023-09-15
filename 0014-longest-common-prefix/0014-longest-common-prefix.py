class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0] # 초기 공통 접두사
        for s in strs[1:]:
            i = 0
            # 문자열의 위치가 같고 prefix, s의 길이보다 작을 때(=비교할 문자가 없을 경우)
            while i < len(prefix) and i < len(s) and prefix[i] == s[i]: 
                i += 1
            prefix = prefix[:i]
        return prefix