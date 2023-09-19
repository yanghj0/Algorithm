class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # 배열을 정렬합니다.
        closest_sum = float('inf')  # inf: 변수값을 무한대로 설정 => 처음에는 어떤 합이든 이 값보다 작을 것이므로 가장 가까운 합 업데이트 가능
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return current_sum
                diff = abs(current_sum - target)
                
                if diff < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum