def solve(N):
    if N == 0:
        return 0
    
    N = abs(N)  # Work with positive target due to symmetry
    
    # Use a dictionary to store the minimum cost to reach each position
    cost_map = {0: 0}
    
    # BFS queue initialized with the starting position (0) and cost (0)
    queue = deque([0])
    
    while queue:
        current = queue.popleft()
        current_cost = cost_map[current]
        
        # Try to move to the next positions
        for i in range(1, N + 1):
            next_positions = [current + i, current - i]
            
            for next_pos in next_positions:
                if next_pos not in cost_map or cost_map[next_pos] > current_cost + i:
                    cost_map[next_pos] = current_cost + i
                    queue.append(next_pos)
                
                # If we reach the target position, return the cost immediately
                if next_pos == N:
                    return cost_map[next_pos]

# Example usage:
N = int(input().strip())
print(solve(N))
