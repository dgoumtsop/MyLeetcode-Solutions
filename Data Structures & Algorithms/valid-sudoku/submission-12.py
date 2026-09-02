class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                nums = board[i][j]
                if nums == ".":
                    continue
                box = (i // 3) * 3 + (j // 3)
                if nums in rows[i] or nums in cols[j] or nums in boxes[box]:
                    return False
                rows[i].add(nums)
                cols[j].add(nums)
                boxes[box].add(nums)
        return True

            
