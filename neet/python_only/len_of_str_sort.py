arr = ["bob", "alice", "jane", "doe"]
arr.sort(key=lambda x: len(x))
print(arr)