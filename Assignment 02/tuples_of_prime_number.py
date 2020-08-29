lower=2
upper=int(input("Enter the limit "))
print("prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
    if (num>1):
        for i in range(2,num):
            if(num%i==0):
                print((num,"non prime"))
                break
        else:
            print((num,"prime"))
