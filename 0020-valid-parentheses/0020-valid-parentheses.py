class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', '}': '{', ']': '['}
        for i in s:
            if i in dic:
                top = stack.pop() if stack else '#'
                if dic[i] != top:
                    return False
            else:
                stack.append(i)
        return not stack