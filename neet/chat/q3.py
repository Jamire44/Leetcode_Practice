grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Output: 3   (one big block at top-left, one in middle, one bottom-right cluster)

grid2 = [
  ["1","0","1","0"],
  ["0","1","0","1"],
  ["1","0","1","0"],
  ["0","1","0","1"]
]
# Output: 8   (checkerboard pattern → each '1' isolated island)

grid3 = [
  ["0","0","0"],
  ["0","0","0"]
]
# Output: 0   (all water)


# def islands(grid):
