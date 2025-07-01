# 🦸‍♂️ Heroes List

#A simple Python program to practice list operations like adding, removing, replacing, and sorting heroes.

## 💡 Source

#Inspired by [your source here].

#1. Length of the list
#2. Add 'black panther' at the end of this list
#3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
#4. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code.
#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros=['spider man','thor','hulk','iron man','captain america']
#1
print('Number of heros in the list:', len(heros))
#2
heros. append('black panther')
#3
heros.pop(5)
heros.insert(heros.index('hulk')+1,'black panther') 
print('after adding black panther after hulk:',heros)
#4
heros[1:3] = ['doctor strange']
print('after removing hulk and thor and adding doctor strange in their place', heros)
#5
heros.sort()
print('after arranging the list in alphabetical order', heros)

