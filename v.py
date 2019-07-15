d1,a2=map(int,input().split())
w3=d1
r4=a2
if(d1>a2):
    while(d1>0):
        if((d1%a2)==0 and (d1%w3)==0):
            print(d1)
            break
        else:
            d1=d1+1
    
else:
    while(a2>0):
        if((a2%d1)==0 and (a2%r4)==0):
            print(a2)
            break
        else:
            a2=a2+1
