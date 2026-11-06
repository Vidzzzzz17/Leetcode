from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        area = 0
        min_x = min_y = float('inf')
        max_a = max_b = float('-inf')

        for x, y, a, b in rectangles:
            area += (a - x) * (b - y)
            min_x, min_y = min(min_x, x), min(min_y, y)
            max_a, max_b = max(max_a, a), max(max_b, b)

            for p in ((x, y), (x, b), (a, y), (a, b)):
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)

        if area != (max_a - min_x) * (max_b - min_y):
            return False

        return corners == {
            (min_x, min_y), (min_x, max_b),
            (max_a, min_y), (max_a, max_b),
        }