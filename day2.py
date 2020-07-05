with open("day2input.txt") as f:
    raw=f.readline().split(',')

nums=[int(x.strip()) for x in raw]

nums[1]=12
nums[2]=2
g=nums[:]

verbose=0

def addition(a,b,c):
    nums[c]=nums[a]+nums[b]

def multiplication(a,b,c):
    nums[c]=nums[a]*nums[b]

for i,num in enumerate(nums):
    if i%4==0:
        if verbose:
            print(i,num)
        if num==99:
            print("Broken at",i,num)
            break
        else:
            a,b,c=nums[i+1],nums[i+2],nums[i+3]
            
            if num==1:
                addition(a,b,c)
                if verbose:
                    print("Addition ")
            elif num==2:
                multiplication(a,b,c)
                if verbose:
                    print("Multiplication")
            else:
                print("error")

print(nums[0])
