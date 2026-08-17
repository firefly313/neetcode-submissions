class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = []

        word_dict = {}
        group_dict = {}
        for word in strs:
            #word_dict[word] = {}
            word_count = {}
            for let in word:
                if let not in word_count:
                    word_count[let] = 1
                else:
                    word_count[let] += 1
            new_val = tuple(sorted(word_count.items()))
            ## have i seen this val before?
            if new_val in group_dict:
                group_dict[new_val] += [word]
            else:
                group_dict[new_val] = [word]
            #print(key, val)

        
        #for key, val in word_dict.items():    
            #new_val = tuple(sorted(val.items()))
            ## have i seen this val before?
            #if new_val in group_dict:
                #group_dict[new_val] += [key]
            #else:
            #    group_dict[new_val] = [key]
            #print(key, val)
        for key, val in group_dict.items():
            anagram_list.append(val)

        #print(group_dict)
        #print(anagram_list)
        #print(word_dict)

        return anagram_list

        ## map all letter combos to a map
        ## keep track of letter frequencies for each word
        ## if num of letter frequencies is equal to another
        ##   (check all values, key will be the word)
        ##    access the key, add it to array in an array
              ## append []