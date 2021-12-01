p1=0
p2=0
XS = [int(x) for x in open('number')]
for i in range(len(XS)):
    if i>=3 and XS[i]+XS[i-1]+XS[i-2]>XS[i-1] +XS[i-2]+XS[i-3]:
        p2 += 1
print(p2)