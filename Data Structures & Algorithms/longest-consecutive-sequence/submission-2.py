class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        longest = 1
        nums = sorted(list(set((nums))))
        #print(nums)
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                break
            if nums[i] == nums[i+1] - 1:
                count += 1
            else:
                count = 1
            if count > longest:
                longest = count


        return longest