class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        
        for string in strs:
            ret += string + "~"
        return ret

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        curr = ""

        for let in s:
            if let == "~":
                decoded_strs.append(curr)
                print(curr)
                curr = ""
            else:
                curr = curr + let

        return decoded_strs