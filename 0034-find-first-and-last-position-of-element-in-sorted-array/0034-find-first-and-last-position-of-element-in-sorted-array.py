class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            if target == nums[i]:
                a.append(i)
        return [min(a),max(a)] if a else [-1,-1]
