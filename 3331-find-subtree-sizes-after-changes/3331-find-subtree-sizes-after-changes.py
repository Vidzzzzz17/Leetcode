from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        last = [-1] * 26
        new_parent = parent[:]
        order = []  # preorder

        # stack entries: (node, state, saved)
        stack = [(0, 0, -1)]
        while stack:
            node, state, saved = stack.pop()
            c = ord(s[node]) - 97
            if state == 0:
                order.append(node)
                if node != 0 and last[c] != -1:
                    new_parent[node] = last[c]
                # enter: save old value, set self as last
                stack.append((node, 1, last[c]))
                last[c] = node
                for ch in children[node]:
                    stack.append((ch, 0, -1))
            else:
                last[c] = saved  # restore

        size = [1] * n
        for node in reversed(order):
            if node != 0:
                size[new_parent[node]] += size[node]
        return size