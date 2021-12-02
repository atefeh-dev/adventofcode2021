import sys
infile = sys.argv[1] if len(sys.argv)>1 else 'number'
p1=0
p2=0
fwd = 0
depth =0
xs =[]
aim=0
for line in open(infile):
    cmd,amt = line.split()
    amt = int(amt)
    if cmd == 'forward' :
        fwd +=amt
        depth +=amt*aim
    elif cmd =='up':
        aim -=amt
    else:
        aim +=amt
print(fwd*depth)