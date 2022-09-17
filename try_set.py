import random 
import datetime
a =[random.randint(0,100000000)for i in range(10000000)]
b =[random.randint(0,100000000)for i in range(100)]
start = datetime.datetime.now()
for temp in b: 
        if temp in a:
            print(f'temp:{temp} in a')
end = datetime.datetime.now()
print (end-start)

c = set(a)
start = datetime.datetime.now()
for temp in b: 
        if temp in c:
            print(f'temp:{temp} in c')
end = datetime.datetime.now()
print (end-start)
