#1. In Feb, how many dollars you spent extra compare to January?
#2. Find out your total expense in first quarter (first three months) of the year.
#3. Find out if you spent exactly 2000 dollars in any month
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this
exp = [2200,2350,2600,2130,2190]
months = ['January','February','March','April','May']
#1
print("Extra dollars spent in February in comparison to January",exp[1]-exp[0])
#2 
print("Total expense in the first quarter of the year",exp[0]+exp[1]+exp[2])
#3
i = 0 
if 2000 in exp:
    print ('2000 dollars were spent in',exp[i],"month")
else:
        print("2000 dollars weren't spent in any month")
#4
exp.append(1980)    
months.append('June')
#5
exp[3] = exp[3] - 200
print(exp)
print(months)
    
    
    



