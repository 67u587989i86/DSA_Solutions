# ── Step 1. Read input ─────────────────────────────────────
m = int(input())                      # number of line segments

start_points = list(map(int, input().split()))
end_points   = list(map(int, input().split()))

# ── Step 2. Build a flat list of every x‑coordinate touched ─
all_points = []                       # will hold 1,2,3,4, ...

for i in range(m):
    start = start_points[i]
    end   = end_points[i]

    # Ensure start ≤ end (just in case input is unordered)
    if start > end:
        start, end = end, start

    # Add every integer point from start to end (inclusive)
    for x in range(start, end + 1):
        all_points.append(x)

# ── Step 3. Sort the list of points ────────────────────────
n = sorted(all_points)
max = 0
count = 1
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        count +=1
        if count > max :
            max = count
    else:
        count = 1
if max != 1:
    print(m - max + (m - max))   
else:
    print(m)
