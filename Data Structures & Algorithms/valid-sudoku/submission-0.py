class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares={}
        for i in range(9):
            squares[i] = set()

        for i in range(9):
            rows = set()
            columns = set()
            


            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rows:
                        return False
                    rows.add(board[i][j])

                    if board[i][j] in squares[(i // 3) * 3 + (j // 3)]:
                        return False

                    squares[(i // 3) * 3 + (j // 3)].add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in columns:
                        return False
                    columns.add(board[j][i])

                
                
        return True
                
                        