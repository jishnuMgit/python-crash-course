cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
   if car == 'bmw':
     print(car.upper())
   else:
     print(car.title())

age = 22

for n in range(1,30):
    if n==age :
        print(f"my age {n}")
    else:
      print(f"{n} is not my age ")    


requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
 print("Hold the anchovies!")


# The if-elif-else Chain

age = 18

if age > 18 :
 print("Your admission cost is $0.")
elif(age <= 18):
 print("Your admission cost is $10.")


# Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
 print("Adding pepperoni")
if 'extra cheese' in requested_toppings : 
  print("adding extra cheese")  


users = {
    "alice": 20,
    "bob": 25,
    "charlie": 30
}

for name, age in users.items():
    print(name,age)
    # print(age)
 


# Removing Key-Value Pairs
# When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely remove a key-value pair.
# All del needs is the name of the dictionary and the key that you want to
# remove


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

for name in favorite_languages.keys():
 print(name.title())
for name in favorite_languages.values():
 print(name.title()) 

 
 #items() // access all the item in a dist
 #keys()//only key
 #values() //only values

lists=[
    {'color': 'green', 'points': 5, 'speed': 'slow'},
{'color': 'green', 'points': 5, 'speed': 'slow'},
{'color': 'green', 'points': 5, 'speed': 'slow'},
{'color': 'green', 'points': 5, 'speed': 'slow'},
{'color': 'green', 'points': 5, 'speed': 'slow'},
] 
print(lists)


#USER INPUT AND WHILE LOOPS
