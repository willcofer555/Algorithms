def num_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or grid[r][c] == '0'):
            return

        visited.add((r, c))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dr, dc in directions:
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1

    return count


def max_area_of_island(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or grid[r][c] == 0):
            return 0

        visited.add((r, c))
        area = 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dr, dc in directions:
            area += dfs(r + dr, c + dc)

        return area

    max_area = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                max_area = max(max_area, dfs(r, c))

    return max_area


def surrounded_regions(board):
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return

        board[r][c] = 'T'
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dr, dc in directions:
            dfs(r + dr, c + dc)

    for r in range(rows):
        if board[r][0] == 'O':
            dfs(r, 0)
        if board[r][cols - 1] == 'O':
            dfs(r, cols - 1)

    for c in range(cols):
        if board[0][c] == 'O':
            dfs(0, c)
        if board[rows - 1][c] == 'O':
            dfs(rows - 1, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'T':
                board[r][c] = 'O'


def word_search(board, word):
    if not board or not board[0]:
        return False

    rows, cols = len(board), len(board[0])

    def dfs(r, c, index, visited):
        if index == len(word):
            return True

        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or board[r][c] != word[index]):
            return False

        visited.add((r, c))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dr, dc in directions:
            if dfs(r + dr, c + dc, index + 1, visited):
                return True

        visited.remove((r, c))
        return False

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0, set()):
                return True

    return False


def shortest_path_binary_matrix(grid):
    if not grid or grid[0][0] == 1:
        return -1

    n = len(grid)
    if n == 1:
        return 1 if grid[0][0] == 0 else -1

    from collections import deque

    queue = deque([(0, 0, 1)])
    visited = {(0, 0)}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while queue:
        r, c, dist = queue.popleft()

        if r == n - 1 and c == n - 1:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < n and 0 <= nc < n and
                grid[nr][nc] == 0 and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1
