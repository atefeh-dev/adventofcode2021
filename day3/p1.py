import sys
infile = sys.argv[1] if len(sys.argv)>1 else 'number'
ans = 0
v0 = {}
v1 = {}
for line in open (infile):
    line = line.strip()
    for i,c in enumerate(line):
        if i not in v0:
            v0[i]=0
        if i not in v1:
             v1[i]=0
        if c =='1':
            v1[i] += 1
        else :
            v0[i] += 1
gamma = ''
epsilon = ''
for i in v0:
    if v0[i] > v1[i]:
        gamma +='0'
        epsilon +='1'
    else:
        gamma +='1'
        epsilon +='0'
print(int(gamma,2)*int(epsilon,2))