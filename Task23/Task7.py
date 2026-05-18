def preobr(start, end):
    if start > end or start == 27: return 0
    if start == end: return 1
    if start < end:
         return preobr(start + 2, end) + preobr(start * 2, end)

print(preobr(3, 15) * preobr(15, 72))

