with open("day3input.txt") as f:
    raw=f.readlines()

line1=[x for x in raw[0].strip().split(',')]
line2=[x for x in raw[1].strip().split(',')]
dists=[]
def traceRoute(line):
    x=y=xflag=yflag=0
    route=set()
    for i in line:
        if i[0]=='R':
            for j in range(int(i[1:])):
                x+=1
                route.add((x,y))
        elif i[0]=='L':
            for j in range(int(i[1:])):
                x-=1
                route.add((x,y))
        elif i[0]=='U':
            for j in range(int(i[1:])):
                y+=1
                route.add((x,y))
        elif i[0]=='D':
            for j in range(int(i[1:])):
                y-=1
                route.add((x,y))
        else:
            print("Error")
    return route

def manDistance(tup):
    return abs(tup[0])+abs(tup[1])

route1=traceRoute(line1)
route2=traceRoute(line2)
intersections=route1.intersection(route2)

for i in intersections:
    dists.append(manDistance(i))

print(min(dists))
