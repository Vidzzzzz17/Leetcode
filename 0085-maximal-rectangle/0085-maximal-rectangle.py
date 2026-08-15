class Solution:

  def maximalRectangle(self, matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]:
      return 0

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    def largestRectangleArea(heights: list[int]) -> int:
      """Helper to calculate max rectangle in a 1D histogram using a monotonic stack."""
      stack = []  # stores indices
      max_h_area = 0
      # Append 0 to flush remaining elements from the stack at the end
      extended_heights = heights + [0]

      for i, h in enumerate(extended_heights):
        while stack and extended_heights[stack[-1]] >= h:
          height = extended_heights[stack.pop()]
          # If stack is empty, width stretches from index 0 to i
          width = i if not stack else i - stack[-1] - 1
          max_h_area = max(max_h_area, height * width)
        stack.append(i)

      return max_h_area

    # Process each row as a histogram base
    for r in range(rows):
      for c in range(cols):
        if matrix[r][c] == "1":
          heights[c] += 1
        else:
          heights[c] = 0

      max_area = max(max_area, largestRectangleArea(heights))

    return max_area