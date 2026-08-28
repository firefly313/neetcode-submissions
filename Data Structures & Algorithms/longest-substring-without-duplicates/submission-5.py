class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = 0
        longest = 0
        seen = {}
        ## recurse forward
        for let in s:
            if let in seen:
                seen = {}
                current = 0
                continue
            else:
                seen[let] = 1
                current += 1
                if current > longest:
                    longest = current
        ## recurse backwards
        #print(s[::-1])
        current = 0
        seen = {}
        for let in s[::-1]:
            if let in seen:
                current = 0
                seen = {}
                continue
            else:
                seen[let] = 1
                current += 1
                if current > longest:
                    longest = current
        return longest