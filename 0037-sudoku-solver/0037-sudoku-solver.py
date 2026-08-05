class Solution:

    def solveSudoku(self, board: list[list[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        # Sets to keep track of placed numbers for O(1) validation
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Step 1: Pre-fill tracking sets and record empty cell locations
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        # Step 2: Backtracking helper function
        def backtrack(index: int) -> bool:
            # If all empty cells are filled, puzzle is solved
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)

            for digit in "123456789":
                if (
                    digit not in rows[r]
                    and digit not in cols[c]
                    and digit not in boxes[box_idx]
                ):
                    # Place digit
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)

                    # Recurse to next empty cell
                    if backtrack(index + 1):
                        return True

                    # Backtrack (undo move)
                    board[r][c] = "."
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)

            return False

        backtrack(0)    