class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dupe = sorted(list(set(nums)))
        nums = sorted(nums)
        if no_dupe == nums:
            return False
        else:
            return True
