# 🍬 Sugar Level Checker

#A simple Python program to check if your sugar level is low, high, or normal based on user input.

## 💡 Source

#Inspired by [https://github.com/codebasics/py/tree/master/Basics/Exercise].

sugar = float(input("Type on your sugar level: -")) 
if sugar < 80:
    print("Your sugar level is low by",80-sugar)
elif sugar > 100:
  print("Your sugar level is high by",sugar-100)
else:
      print("Your sugar level is normal")
      
  
