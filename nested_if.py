str_input = int(input("Enter your number : "))

if str_input%2==0:
    if str_input%3==0:
        if str_input%5==0:
            print("this even number "+str(str_input)+" divisible by 5, 3, 2")