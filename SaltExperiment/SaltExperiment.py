from random import seed,randint
import os

if not os.path.isdir('./input'):
    os.mkdir('./input')

for k in range(15):
    seed(k)    
    t=randint(1,1000)
    
    testname="./input/input"+"%02d"%k+".txt"
    
    for i in range(15):
        f=open(testname,'+a')
        f.write(str(t))
        
        for _ in range(t):
            x = randint(31,40)
            a = randint(101,120)
            b = randint(1,5)
           
            f.write('\n')
            f.write(str(x))
            f.write(' ')
            f.write(str(a))
            f.write(' ')
            f.write(str(b))
            