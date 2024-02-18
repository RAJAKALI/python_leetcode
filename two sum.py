nums=list(map(int,input('').split(',')))
target=int(input(''))
flag=False
l=len(nums)
for i in range(l-1):
    for j in range(i+1,l):
        if(nums[i]+nums[j]==target):
            print([i,j])
            flag=True
            break
if(flag==False):
    print('no two numbers that can make the target ',target)
