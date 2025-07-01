# ⭐ Star Pyramid

#A simple Python program to print a star pyramid based on user input.

## 💡 Source

#Inspired by [https://github.com/codebasics/py/tree/master/Basics/Exercise]
---
lines =int(input('Number of rows you want in the star pyramid: ')) 
for i in range(1,lines+1):
    print(' '*(lines-1),"*"*(2*i-1),)
    lines = lines - 1
