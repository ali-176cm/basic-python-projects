#Lets say you are running a 5 km race. Write a program that,

#1-Upon completing each 1 km asks you "are you tired?"If you reply "yes" then it should break and print "you didn't finish the race"
#2-If you reply "no" then it should continue and ask "are you tired" on every km
#3-If you finish all 5 km then it should print congratulations message



for i in range(1,6):
    a=input("Are you tired, Yes or No : ")
    if a.lower() == "yes":
        print ("you didn't finish the race")
        break
    elif a.lower()== "no":
     continue
else:     
      print("you completed the race") 
