class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       ## check row duplicates
        for row in range(9):
            seen = set()
            for col in range(9):
                curr = board[row][col]
                if curr.isnumeric() and curr in seen:
                    return False
                seen.add(curr)

        ## check col duplicates
        for col in range(9):
            seen = set()
            for row in range(9):
                curr = board[row][col]
                if curr.isnumeric() and curr in seen:
                    return False
                seen.add(curr)

        ## check box duplicates
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        curr = board[i+row][j+col]
                        if curr.isnumeric() and curr in seen:
                            return False
                        seen.add(curr)

        return True