# message=int(input("enter your age"))

# if message < 18:
#     print("stop go back")
# else:
#     print("come on")    

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1  



# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#  message = input(prompt)
#  print(message)    

# while True:
#     city = input(prompt)
#     if city == 'quit':
#        break
#     else:
#       print(f"I'd love to go to {city.title()}!") 

# current_number = 0
# while current_number < 10:
#  current_number += 1
#  if current_number % 2 == 0:
#       continue
#  print(current_number)      

unconfirmed_users = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
confirmed_users = []
print(unconfirmed_users)
while unconfirmed_users :
    current_user=unconfirmed_users.pop()
    chechyesno = input(f"Is {current_user} verified y/n: ")
    if chechyesno =="y" :
        confirmed_users.append(current_user)

print(confirmed_users)        


res={}

name = input("\nWhat is your name? ")
response = input("Which mountain would you like to climb someday? ")

res[name]=response

print(res)