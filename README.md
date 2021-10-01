# CodeStack 2021 Scripts :
## A guide to writing custom python scripts for automating test cases creation for hackerrank coding competitions .
## This repository contains a few problems from CSI RAIT's Codestack 2021 as examples.
<br /><br />

# Requirements
>## 1. GNU C/C++ Compiler
>## 2. Python v3+

<br>

# Steps 

<br />

>## 1. Create a Folder , add the C/C++ solution to the folder and compile it . 
<br>

```
gcc filename.c    //for c code --->or
g++ filename.cpp  //for c++ code
```
<br>

>## 2. In your created folder, run *problem_name.py* file to create input text files . 
### I have set the *default number* of test cases to be created to 15. Edit the code in the for loop according to your problem requirements.
### This file basically creates input text files according to *input format* specified in the question
<br>

```
python filename.py
```

<br>

>## 3. In your created folder, run *print_op.py* file to create output textfiles . This files stays the same for all questions.
<br>

```
python print_op.py
```

