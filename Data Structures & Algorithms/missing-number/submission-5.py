class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        last_num = len(nums)
        for i in range(len(nums)):
            if nums[i] != i:
                return i
            if nums[-1] != last_num:
                return last_num
        return 0

        #nums = sorted(nums)
        #last_num = len(nums)
        #for i in range(len(nums) - 1):
        #    if last_num != nums[-1]:
        #        return last_num
        #    else:
        #        return 0
        #    if nums[i] == nums[i+1] - 1:
        #        continue
        #    else:
        #        return nums[i] + 1
            

