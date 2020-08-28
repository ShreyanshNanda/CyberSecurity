print("Checks whether a passed in string is palindrome or not")
def string(s):
    if s==s[::-1]:
        print("yes")
    else:
        print("no")
s=input("Enter the string : ")
string(s)
