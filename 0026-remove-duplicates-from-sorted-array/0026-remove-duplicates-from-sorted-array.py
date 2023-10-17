class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 기존 nums 리스트를 그대로 유지하면서 순서만 바꿈, [:]이 없으면 새로운 리스트로 생성
        nums[:] = sorted(set(nums))
        return len(nums)