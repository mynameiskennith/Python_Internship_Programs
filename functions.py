# def sum(a, b):
#     return a+b


# print(sum(3, 4))

def calculate_si(p, t, r):
    print("Simple Interest = ", int(p*t*r/100))
    return calculate_si(p, t, r)


p = int(input("Principal Amount"))
t = int(input("Time : "))
r = int(input("Rate : "))
calculate_si(p, t, r)
