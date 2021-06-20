# str_input = int(input("Enter your Number : "))

# if str_input%2==0:
#     print("even number")
# else:
#     print("odd number")

# if str_input%5!=0:
#     print("Given number is not in multiple of 5")
# else:
#     print("Given number is in multiple of 5")
    

# if str_input%2==1:
#     print("odd number")
# if str_input%2==0:
#     print("The given number is in multiple of 2")
# elif str_input%3==0:
#     print("The given number is in multiple of 3")
# elif str_input%5==0:
#     print("The given number is in multiple of 5")
# else:
#     print("The given number is not in multiple of 2, 3, 5")


# if str_input%2==0:
#     print("number is in multiple of 2")
# elif str_input%7==0:
#     print("number is in multiple of 7")

# num1 = 15
# num2 = 10

# print("num1 is greater") if num1>num2 else print("num2 is greater")

num1 = int(input("Enter your Number : "))
num2 = int(input("Enter your Number : "))

if not (num1%3==0 and num2%5==0):
    print("num1 is multiple of 3")
    print("num2 is multiple of 5")
else:
    print("bad numbers")

######################## XOR Operator #######################
# TRUE xor TRUE = FALSE = NOT(TRUE)
# FALSE xor TRUE = False = NOT(TRUE)
# TRUE xor FALSE = FALSE = NOT(TRUE)
# FALSE xor FALSE = TRUE = NOT(FALSE)
######################## OR Operator #######################
# TRUE or TRUE = TRUE
# FALSE or TRUE = TRUE
# TRUE or FALSE = TRUE
# FALSE or FALSE = FALSE
######################## AND Operator #######################
# TRUE and TRUE = TRUE
# FALSE and TRUE = FALSE
# TRUE and FALSE = FALSE
# FALSE and FALSE = FALSE
######################## NAND Operator #######################
# TRUE nand TRUE = FALSE
# FALSE nand TRUE = TRUE
# TRUE nand FALSE = TRUE
# FALSE nand FALSE = TRUE
