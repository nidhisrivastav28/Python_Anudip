# A transport company charges the fare according to following table:
# Distance Charges
# 1-50 8 Rs./Km
# 51-100 10 Rs./Km
# > 100 12 Rs/Km

def dist_fare():
    dist= int(input("Enter distance:"))
    if dist>=1 and dist<=50:
        fare = dist * 8
    elif dist>=51 and dist<=100:
        fare = dist * 10
    elif dist>100:
        fare = dist * 12
    else:
        print("Invalid fare")
    print("The total fare is:",fare)

dist_fare()

# OUTPUT
# Enter distance:12
# The total fare is: 96