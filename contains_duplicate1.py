#another way to duplicate detecter
flag=False
n=list(map(int,input('enter the list of numbers using comma for seperate:').split(',')))
l=len(n)
for i in range(l-1):
    for j in range(i+1,l):
        if(n[i]==n[j]):
            flag=True
print(flag)
        
            
