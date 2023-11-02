# Python program to check leap year.

year=int(input("Enter the year:"))
if(year%400==0 ) or (year%4==0 and year%100!=0):
    print("The year" ,year, "is a leap year")
# elif():
#     print("The year" +year+ "is a leap year")
# elif():
#     print("The year" +year+ "is a leap year")
else:
     print("The year" ,year, "is not a leap year")

# OUTPUT
# Enter the year:2002
# The year 2002 is not a leap year