class Solution:
    def search(self, nums: List[int], target: int) -> int:
        counter = 0
        left = 0
        right = len(nums) - 1
        while counter <= len(nums)-1:
            length = len(nums)
            mid_i = (right + left) // 2
            ## check if num < or > nums[mid_i]
            if target == nums[mid_i]:
                return mid_i
            if target < nums[mid_i]:
                ## split left
                right = mid_i
                #left = 0
            if target > nums[mid_i]:
                ## split right
                #right = 
                left = mid_i + 1
            counter += 1
        return -1

         #[1, 2, 3, 4]

        #target = 3
        #len = 4
        #counter = 0
        #mid_i = 0+3 / 2 = 1
        #is 3 < 2? no
        #is 3. 2? yes
        #look at right side
        #counter=1, 

       