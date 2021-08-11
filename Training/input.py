def whether_cond(temp):
    if temp > 27:
        return 'Warm'
    else :
        return 'Cold'

user_input =   float(input("Enter the temp : "))
print(whether_cond (user_input))

