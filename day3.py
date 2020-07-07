
with open("day3input.txt") as f:
    raw=f.readlines()

line1=[x for x in raw[0].strip().split(',')]
line2=[x for x in raw[1].strip().split(',')]
dists=[]
dists2=[]
def traceRoute(line):
    x=y=dist=0
    route=set()
    routeDict={}
    for i in line:
        xflag=yflag=0
        if i[0]=='R':
            xflag=1
                
        elif i[0]=='L':
            xflag=-1
            
        elif i[0]=='U':
            yflag=1
            
        elif i[0]=='D':
            yflag=-1
            
        else:
            print("Error")
            
        for j in range(int(i[1:])):
            dist+=1
            x+=xflag
            y+=yflag
            if (x,y) not in routeDict:
                routeDict[(x,y)]=dist
    return routeDict

def manDistance(tup):
    return abs(tup[0])+abs(tup[1])

route1=traceRoute(line1)
route2=traceRoute(line2)
intersections=set(route1).intersection(set(route2))

for i in intersections:
    dists.append(manDistance(i))

for i in intersections:
        dists2.append(route1[i]+route2[i])

print(min(dists))
print(min(dists2))
