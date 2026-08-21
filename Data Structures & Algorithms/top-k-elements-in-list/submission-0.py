class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        ret = []

        for num in nums:
            if num not in ans:
                ans[num] = 1
            else:
                ans[num] +=1
        sorted_dict = dict(sorted(ans.items(), key=lambda x: x[1], reverse=True))
        counter = 0
        for key in sorted_dict.keys():
            if counter == k:
                break
            ret.append(key)
            counter += 1

        return ret
        #print(ret)
        #print(ans)