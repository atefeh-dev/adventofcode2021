p1=0
P2=None
prev = None
for line in open ('number'):
    line = line.strip()
    x = int(line)
    if prev and x > prev:
        p1 += 1
    prev = x
print(p1)
