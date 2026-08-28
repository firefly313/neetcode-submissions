class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        total = 1
        non_zero = 1
         
        ## if all zeros, return nums
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        if zero_count == len(nums):
            return nums

        ## 
        for i, num in enumerate(nums):
            total *= num
            if num != 0:
                non_zero *= num
            arr[i] = num
        #print(total)
        #print(arr)
        for i, num in enumerate(arr):
            if num == 0 and zero_count == 1:
                arr[i] = non_zero
                continue
            if num == 0:
                arr[i] = 0
                continue
            arr[i] = int(total / num)
        #print(arr)
        return arr