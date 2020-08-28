print("Multiply all the numbers in a list")
def multiply(list):
    multiply=1

    for i in list:
        multiply=multiply * i
    print(multiply)

list=[1,2,3,4,5]
multiply(list)
