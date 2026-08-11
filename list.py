bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])



motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)



motorcycles.insert(0, 'ducati')
print(motorcycles)

popped_motorcycle = motorcycles.pop(2)
print(motorcycles)
print(popped_motorcycle)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)



#sort 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

print(len(cars))



#for loop


#for then a veriable , then using the veriable access all th array
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician)


magicians1 = ['alice', 'david', 'carolina']
for magician1 in magicians1:
   print(magician1)


# Python’s range() function makes it easy to generate a series of numbers.
# For example, you can use the range() function to print a series of numbers

for value in range(1, 5):
 print(value)  


square=[]

for value in range(1,11):
    # new_value=value ** 2
    # square.append(new_value)
     square.append(value**2) 

print(square)    

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))

print(max(digits))
print(sum(digits))


#Slicing a List

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])