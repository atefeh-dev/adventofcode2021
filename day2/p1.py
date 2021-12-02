import sys
infile = sys.argv[1] if len(sys.argv)>1 else 'number'
p1=0
p2=0
fwd = 0
depth =0
xs =[]
for line in open(infile):
    cmd,amt = line.split()
    amt = int(amt)
    if cmd == 'forward' :
        fwd +=amt
    elif cmd =='up':
        depth -=amt
    else:
        depth+=amt
print(fwd*depth)