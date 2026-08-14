class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## create our new string, clean lower 
        new_string = ""
        for let in s:
            if let.isalnum():
                new_string += let.lower()
            else:
                continue
        reversed_string = new_string[::-1]
        return reversed_string == new_string

        ## didn't need to compare letter by letter
        ## if its a palindrom, reverse and forward
        ## will be equal
        
        #for i in range(len(new_string)):
        #    if new_string[i] != reversed_string[i]:
        #        return False
        #    else:
        #        continue
        #return True