sugar = float(input("Type on your sugar level: -")) 
if sugar < 80:
    print("Your sugar level is low by",80-sugar)
elif sugar > 100:
  print("Your sugar level is high by",sugar-100)
else:
      print("Your sugar level is normal")
      
  