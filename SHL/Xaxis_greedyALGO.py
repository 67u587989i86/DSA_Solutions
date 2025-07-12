# ---------- Step 1. Read input ----------
m = int(input())
starts = list(map(int, input().split()))
ends   = list(map(int, input().split()))

# ---------- Step 2. Build list of (start, end) tuples ----------
segments = []
for i in range(m):
    s, e = starts[i], ends[i]
    if s > e:
        s, e = e, s
    segments.append((s, e))

# ---------- Step 3. Sort by end coordinate ----------
segments.sort(key=lambda seg: seg[1])

# ---------- Step 4. Greedy select touch points ----------
touches = []
for s, e in segments:
    # if current segment already covered by last chosen point, skip
    if touches and s <= touches[-1] <= e:
        continue
    # otherwise touch at e
    touches.append(e)

# ---------- Step 5. Output -------------
print(len(touches))
# Optional: print(touches)
