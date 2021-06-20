#Nested Function
print(__name__)
def outerFunction(word):
    def innerFunction():
        pi = 3.14
        print(word, pi)
    return innerFunction

if __name__ == "__main__":
    myanotherfunction = outerFunction("Hi")
    # print(myanotherfunction)
    myanotherfunction()