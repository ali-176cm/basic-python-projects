india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
a, b= input(" Enter the name of two cities: ").split()

if a in india and b in india:
    print("The cities",a,"and",b,"are in India")
elif a in pakistan and b in pakistan:
    print(" The cities",a,"and",b,"are in Pakistan")
elif a in bangladesh and b in bangladesh:
    print("The cities",a,"and",b,"are in Bangladesh")
else:
    print("The cities",a,"and",b,"aren't in the same country")
    
    
    