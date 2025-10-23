grid = [
    ['W','L','W','W','W'],
    ['W','L','W','W','W'],
    ['W','W','W','L','W'],
    ['W','W','L','L','W'],
    ['L','W','W','L','L'],
    ['L','L','W','W','W']
]

def island(grid):

    visited = set()
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, visited):
                count += 1 
    return count

def explore(grid, r, c, visited):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return False
    
    if grid[r][c] == 'W':
        return False
    if (r, c) in visited:
        return False
    
    visited.add((r,c))
    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c-1, visited)
    explore(grid, r, c+1, visited)

    return True

print(island(grid))





