class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)