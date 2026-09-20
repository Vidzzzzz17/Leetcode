class Solution:

    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # Find the point on/in the rectangle closest to the circle's center
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        # Calculate squared distance from center to closest point
        dx = closestX - xCenter
        dy = closestY - yCenter

        return (dx * dx + dy * dy) <= radius * radius