print("Number of upper case letters and lower case letters ")
def count_letters(s):
    n=len(s)
    c=0
    c1=0
    for i in range(0,n):
        if(s[i].isupper()==True):
            c=c+1
        if(s[i].islower()==True):
            c1=c1+1
    print(f'Upper case letters are {c}')
    print(f'Lower case letters are {c1}')

s=input("Enter the string : ")
c3=count_letters(s)
