class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ""
        int_str = 0
        arr = []
        for num in digits:
            num_str += str(num)
        int_str = int(num_str)
        int_str += 1
        num_str = str(int_str)
        print(num_str)
        for i in range(len(num_str)):
            arr.append(int(num_str[i]))
        return arr
        

    
      ## go thro list
      ## make string num
      ## convert to int
      ## add one
      ## convert back to string then array   