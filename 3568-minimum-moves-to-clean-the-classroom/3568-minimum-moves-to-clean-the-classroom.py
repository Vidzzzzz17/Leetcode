from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r, start_c = -1, -1
        litters = []
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
                    
        num_litters = len(litters)
        litter_map = {pos: i for i, pos in enumerate(litters)}
        target_mask = (1 << num_litters) - 1
        
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
            
        max_energy = [[[-1] * (1 << num_litters) for _ in range(n)] for _ in range(m)]
        
        queue = deque([(start_r, start_c, initial_mask, energy, 0)])
        max_energy[start_r][start_c][initial_mask] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, cur_energy, moves = queue.popleft()
            
            if mask == target_mask:
                return moves
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = cur_energy - 1
                    
                    if next_energy < 0:
                        continue
                        
                    cell = classroom[nr][nc]
                    next_mask = mask
                    
                    if cell == 'L':
                        litter_idx = litter_map[(nr, nc)]
                        next_mask |= (1 << litter_idx)
                    elif cell == 'R':
                        next_energy = energy
                        
                    if next_energy > max_energy[nr][nc][next_mask]:
                        max_energy[nr][nc][next_mask] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, moves + 1))
                        
        return -1