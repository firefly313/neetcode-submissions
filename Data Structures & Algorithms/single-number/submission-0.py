class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = {}
        for num in nums:
            if num not in ans:
                ans[num] = 1
            else:
                ans[num] += 1
        
        for key, val in ans.items():
            if val == 1:
                return key