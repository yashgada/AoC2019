with open("day1input.txt") as f:
    raw = f.readlines()
lines=[int(x.strip()) for x in raw]
fuel=totalFuel=0
for line in lines:
    fuel+=line//3-2
    
def calcTotalFuel(weight):
    total=0
    while weight>8:
        weight=weight//3-2
        total+=weight
    return total
        
for line in lines:
    totalFuel+=calcTotalFuel(line)
print(fuel)
print(totalFuel)
