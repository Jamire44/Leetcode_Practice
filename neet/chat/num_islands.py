def num_islands(grid):
    if not grid: return 0
    R,C = len(grid), len(grid[0])
    seen = set()
    def dfs(r,c):
        if (r,c) in seen or not (0 <= r < R and 0<=c<C) or grid[r][c]=='0':
            return
        seen.add((r,c))
        dfs(r+1,c); dfs(r+1,c); dfs(r+1,c); dfs(r+1,c)
    count = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c]=='1' and (r,c) not in seen:
                dfs(r,c); count+=1
    return count
