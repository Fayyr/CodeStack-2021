from random import seed,randint
import os

if not os.path.isdir('./input'):
    os.mkdir('./input')

for k in range(15):
    seed(k)    
    t=randint(1,312)
    
    testname="./input/input"+"%02d"%k+".txt"
    
    
    f=open(testname,'+a')
    f.write(str(t))
    f.write('\n')
    numbers=[]
    for _ in range(t):
      numbers.append(str(randint(0,104)))
    
    f.write(' '.join(numbers))
    
    
    