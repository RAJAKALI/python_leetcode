#output true if it contains duplicate values
n=int(input('enter the length of the list:'))
nums=[]
c=0
for i in range(n):
    nums.append(int(input('')))
for i in nums:
    for j in nums:
        if(i==j):
            c=c+1
if(c>n):
    print('true')
else:
    print('false')
