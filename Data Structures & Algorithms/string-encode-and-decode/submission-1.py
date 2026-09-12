class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for string in strs:
            ret += string + "~"
            #print(string)
            #print(ret)

        return ret
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        curr = ""
        for let in s:
            #print(let)
            if let == "~":
                decoded_strs.append(curr)
                print(curr)
                curr = ""
            else:
                curr = curr + let
            #print(curr)
        

        return decoded_strs