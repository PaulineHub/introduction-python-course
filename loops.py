#Python control flows - Loops

'''
Python’s for statement iterates over the items of any sequence 
(a list or a string), in the order that they appear in the 
sequence.

The built-in Range function 'range()' comes in handy if you do need 
to iterate over a sequence of numbers. It generates arithmetic progressions:

range(start, stop, step)
start
The value of the start parameter (or 0 if the parameter was not supplied)
stop
The value of the stop parameter
step
The value of the step parameter (or 1 if the parameter was not supplied)
'''

#The basics
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Create a sample collection
users = {
    'Quinn': 'active',
    'Éléonore': 'inactive',
    'John': 'active'
    }

# Strategy:  Iterate over a copy
#users.copy().items() : fait une copie du dictionnaire et retourne une liste [] de tuples() cle:valeur
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


#using the range function
#Create a sequence of numbers from 0 to 5, and print each item in the sequence:
for i in range(5):
    print(i)

#...remember range(start, stop, step)
list(range(5, 10))
#return [5, 6, 7, 8, 9]
list(range(0, 10, 3))
#return [0, 3, 6, 9]
list(range(-10, -100, -30))
#return [-10, -40, -70]

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#using the built-in sum function
sum(range(4))
#return 6