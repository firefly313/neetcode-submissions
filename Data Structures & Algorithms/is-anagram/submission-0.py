class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        ## change to track num of occurrences
        for let in s:
            if let in smap:
                smap[let] += 1
            else:
                smap[let] = 1
        for let1 in t: 
            if let1 in tmap:
                tmap[let1] += 1
            else:
                tmap[let1] = 1

        ## check if num of occurence equal
        ## checking smap first
        for key in smap.keys():
            if key in tmap.keys():
                if smap[key] == tmap[key]:
                    continue
                else:
                    return False
            else:
                return False
        ## then tmap
        for key in tmap.keys():
            if key in smap.keys():
                if tmap[key] == smap[key]:
                    continue
                else:
                    return False
            else:
                return False

        return True
        