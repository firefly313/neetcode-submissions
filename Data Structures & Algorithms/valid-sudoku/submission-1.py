class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ## prob better optimization to use set instead of dict

        ## 1.) each row must contain the digits 1-9 without duplicates
        ## loop through each row and make sure there is no duplicate
        for row in range(len(board)):
            check_row = {}
            for col in range(len(board[row])):
                curr = board[row][col]
                ## check if its a number and in the dict
                if curr.isnumeric() and curr in check_row:
                    return False
                else:
                    check_row[curr] = 0
                
        ## 2.) each column must contain digits 1-9 without duplicates
        for col in range(len(board[0])):
            check_col = {}
            for row in range(len(board)):
                curr = board[row][col]
                ## check if its a number and in the dict
                if curr.isnumeric() and curr in check_col:
                    return False
                else:
                    check_col[curr] = True

        ## 3.) each of the 3x3 sub-boxes must contain the digits 1-9 no dupes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                check_box = {}
                for i in range(3):
                    for j in range(3):
                        curr = board[row+i][col+j]
                        if curr.isnumeric() and curr in check_box:
                            return False
                        else:
                            check_box[curr] = True

        return True