india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulna","rangpur"]
Name = input(" Type the name of a city: ")
if Name in india:
 print("The city",Name," is in india")
elif Name in pakistan:
     print("The city", Name,"is in Pakistan")
elif Name in bangladesh:
     print("the city",Name,"is in bangladesh")
else:
   print(" Based on the little       information I have, I can't tell      in    which country",Name,'is located')


