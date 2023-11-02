# Find the Simple Interest on Rs. 200 for 5 years at 5% per year.

def simpleinterest(p,r,t):
    SI=(p*r*t)/100
    print("Simple Interest=" ,SI)

p=float(input("enter the principle:"))
r=float(input("enter the rate of interest:"))
t=int(input("enter the time period:"))
simpleinterest(p,r,t)


# OUTPUT
# enter the principle:8
# enter the rate of interest:2
# enter the time period:8
# Simple Interest= 1.28