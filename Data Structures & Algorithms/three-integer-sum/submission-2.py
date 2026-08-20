class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ < 0:
                    left += 1
                if summ > 0:
                    right -= 1
                if summ == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        ## get rid of dupes
        nodupe_ans = [list(t) for t in dict.fromkeys(tuple(i) for i in ans)]
        #print(ans)
        #print(nodupe_ans)
        return nodupe_ans






        ## brute force for practice
        #ans = []
        #for i in range(len(nums)):
        #    for j in range(i+1, len(nums)):
        #        for k in range(j+1, len(nums)):
        #            if nums[i] + nums[j] + nums[k] == 0:
        #                ans += [[nums[i], nums[j], nums[k]]]
        #if len(ans) == 0:
        #    return []
        #for i in range(len(ans)):
        #    ans[i] = sorted(ans[i])
        ## get rid of dupes
        #unique = [list(t) for t in dict.fromkeys(tuple(i) for i in ans)] 
        #return unique