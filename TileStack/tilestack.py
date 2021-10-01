from random import seed,randint
import os

if not os.path.isdir('./input'):
    os.mkdir('./input')


for k in range(15):
    seed(k)
    T = randint(1,50)
    
    testname="./input/input"+"%02d"%k+".txt"
    
    
    f=open(testname,'+a')
    f.write(str(T))
    f.write('\n')
    
    for _ in range(T):
        n= randint(1,50)
        f.write(str(n))
        f.write('\n')
        numbers = []
        
        for x in range(n):
          numbers.append(str(randint(1,50)))
          
          
        f.write(' '.join(numbers))
        f.write('\n')
             