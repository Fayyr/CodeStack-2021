from subprocess import Popen, PIPE, STDOUT
import subprocess,os

if not os.path.isdir('./output'):
    os.mkdir('./output')

for k in range(15):
        
    testname="./output/output"+"%02d"%k+".txt"
    
    f=open(testname,'w')
    inpu=open("./input/input"+"%02d"%k+".txt",'r')
    p = Popen(['./a.exe'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
    x=inpu.read()
    # print(x)
    grep_stdout = p.communicate(input=x.encode())[0]
    f.write(grep_stdout.decode())