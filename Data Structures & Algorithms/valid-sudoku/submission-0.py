class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        boxset = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                else:
                    if val in rowset[r] or val in colset[c] or val in boxset[(r // 3, c // 3)]:
                        return False
                    else:
                        rowset[r].add(val)
                        colset[c].add(val)
                        boxset[(r//3, c//3)].add(val)
        
        return True
