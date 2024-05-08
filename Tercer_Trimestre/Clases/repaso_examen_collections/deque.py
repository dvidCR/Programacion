from collections import deque

d = deque("ghi")

d.append("a")

print(d)

d.appendleft("a")

print(d)

d.insert(3, "x")

print(d)