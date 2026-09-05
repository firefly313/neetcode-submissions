class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        right = len(nums) - 1
        left = 0
        counter = 0

        while(counter <= len(nums) - 1):
            mid = (left + right) // 2
            num = nums[mid]
            if num == target:
                return mid
            if target > num:
                ## want to look at right side of arr
                left = mid + 1
            if target < num:
                ## want to look at left side of arr
                right = mid - 1

            counter += 1

        return -1