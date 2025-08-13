import time
from collections import deque

maze = [
    [0,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,0,1,1,1,0,1,0,1,0],
    [1,0,1,0,0,0,1,0,1,0],
    [1,0,1,0,1,1,1,0,1,0],
    [1,0,0,0,1,0,0,0,0,1],
    [1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,1,1],
    [1,0,0,0,0,0,0,0,0,0]
]

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    m = [row[:] for row in maze]
    parent = {}
    q = deque([start])
    m[start[0]][start[1]] = 1
    moves = [(0,1),(0,-1),(1,0),(-1,0)]

    while q:
        x, y = q.popleft()
        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            return [start] + path[::-1]
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and m[nx][ny] == 0:
                m[nx][ny] = 1
                parent[(nx, ny)] = (x, y)
                q.append((nx, ny))
    return None

# Test cases
test_data = [
    (0,0, 9,9),
    (1,0, 9,9),
    (0,9, 9,9),
    (1,5, 9,9),
    (2,1, 9,5),
    (2,5, 9,5),
    (1,7, 9,5),
    (3,5, 9,1),
    (5,1, 9,1),
    (4,7, 9,1)
]

# Run BFS for each test case
for i, (sx, sy, gx, gy) in enumerate(test_data, 1):
    start_time = time.time()
    path = bfs(maze, (sx, sy), (gx, gy))
    end_time = time.time()
    duration = (end_time - start_time) * 1000

    print("\n=" + "="*150)
    print(f"\nTest {i}")
    print(f"Start: ({sx},{sy})")
    print(f"Goal: ({gx},{gy})")
    if path:
        print(f"Path length: {len(path)-1} steps")
        print("Path:", " -> ".join(f"({x},{y})" for x, y in path))
    else:
        print("No path found")
    print(f"Time taken: {duration:.3f} ms")
