#import time
N=232792560
import rand as r
n=int(input())
#t=time.perf_counter()
#t=int(((t*10)%1)*1e6)
l=r.random_int(a=1,b=N,size=n*20)
i=0
cnt=19
s=[25]*20
while i<n:
    j=0
    while j<20:
        if s[j]:
            x=l[i*20+j]
            x=x%cnt
            if x==0:
                x=cnt
            if s[j]==1:
                cnt-=1
            z=j
            while x>0:
                z=(z+1)%20
                if s[z]>0:
                    x-=1
            s[j]-=1
            s[z]+=1
        j+=1
        if cnt==1:
            break
    if cnt==1:
        break
    i+=1
print(s)
