import random
import sys

n=int(sys.argv[1])
v=[]
for i in range(0,n):
    v.append(random.randint(1,6))
#print(v)
value=sum(v)
durchschnitt= value/n
print(durchschnitt)
