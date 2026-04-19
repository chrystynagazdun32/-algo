import os
from collections import deque

def solve():
    path = os.path.dirname(os.path.abspath(__file__))
    
    with open(os.path.join(path, 'input.txt'), 'r', encoding='utf-8') as f:
        lines = [line.split('#')[0].strip() for line in f if line.strip()]
        n = int(lines[0])
        start = tuple(map(int, lines[1].replace(',', ' ').split()))
        end = tuple(map(int, lines[2].replace(',', ' ').split()))

    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]

    queue = deque([(start[0], start[1], 0)])
    visited = {start}
    res = -1

    while queue:
        x, y, d = queue.popleft()
        if x == end[0] and y == end[1]:
            res = d
            break

        for i in range(8):
            nx, ny = x + row[i], y + col[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, d + 1))

    with open(os.path.join(path, 'output.txt'), 'w', encoding='utf-8') as f:
        f.write(str(res))
    
    print(f"Файл створено! Результат: {res}")

if __name__ == "__main__":
    solve()