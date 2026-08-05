class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        # Multiply each digit from right to left
        for i in range(m - 1, -1, -1):
            digit1 = ord(num1[i]) - ord("0")
            for j in range(n - 1, -1, -1):
                digit2 = ord(num2[j]) - ord("0")

                # Product of current digits
                mul = digit1 * digit2

                # Indices in result array
                p1, p2 = i + j, i + j + 1

                # Add to existing value at p2
                total = mul + res[p2]

                res[p2] = total % 10  # Remainder stays at p2
                res[p1] += total // 10  # Carry adds to p1

        # Skip leading zeros
        start_idx = 0
        while start_idx < len(res) and res[start_idx] == 0:
            start_idx += 1

        # Convert digits to string
        return "".join(map(str, res[start_idx:]))