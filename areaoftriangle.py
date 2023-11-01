# Python program to find the area of a triangle whose sides are given

a=float(input("Enter the length of one side of triangle: "))
b=float(input("Enter the length of second side of triangle: "))
c=float(input("Enter the length of third side of triangle: "))

# calculate semi-perimeter
s=(a+b+c)/2

# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  

print('The area of the triangle is %0.2f' %area)  

# OUTPUT

# Enter the length of one side of triangle: 12
# Enter the length of second side of triangle: 13
# Enter the length of third side of triangle: 10
# The area of the triangle is 57.00