print("Volume of a Sphere ")
def volume(r):
    pi=3.1415
    v=(4/3)*pi*r*r*r
    return v
    
r=float(input("Enter the radius : "))
v1=volume(r)
print(f"Volume of a sphere is {v1}")
