user_input = input("Enter your name   ")
surname = input("Enter your surnamename   ")
message = "Hello %s %s!" % (user_input,surname)
print(message)
#only after python 3.6 
message = f"Hello {user_input} {surname} !!!!!!!" 
print(message)