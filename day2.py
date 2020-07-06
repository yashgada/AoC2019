with open("day2input.txt") as f:
    raw=f.readline().split(',')

nums=[int(x.strip()) for x in raw]

nums[1]=12
nums[2]=2
g=nums[:]
ans=0

verbose=0

def addition(a,b,c):
    nums[c]=nums[a]+nums[b]

def multiplication(a,b,c):
    nums[c]=nums[a]*nums[b]

def loop():
    for i,num in enumerate(nums):
        if i%4==0:
            if verbose:
                print(i,num)
            if num==99:
                break
            else:
                a,b,c=nums[i+1],nums[i+2],nums[i+3]
                
                if num==1:
                    addition(a,b,c)
                    
                elif num==2:
                    multiplication(a,b,c)
                    
                else:
                    print("error",i,num)
    return nums[0]

print("The answer to the hirst half is: ",loop())

for j in range(100):
    for k in range(100):
        nums=g[:]
        nums[1],nums[2]=j,k
        loop()
        if nums[0]==19690720:
           ans=nums[1]*100+nums[2]

print(ans)
