from random import seed,randint
import random
import string
import os

if not os.path.isdir('./input'):
    os.mkdir('./input')

for k in range(15):
    seed(k)    
    
    
    testname="./input/input"+"%02d"%k+".txt"
    
    
    numbers = []
    f=open(testname,'+a')
    
    
    for _ in range(26):
        n = randint(1,20)
        numbers.append(str(n))
    inp = ''        
    f.write(' '.join(numbers))
    f.write('\n')
    inp  = ''.join((random.choice(string.ascii_lowercase) for _ in range(randint(1,10))))
    f.write(inp)
        
        
            
            
            