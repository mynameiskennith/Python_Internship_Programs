from random import randint
crt = 0
wrg = 0
for i in range(1, 5):
    a = randint(0, 100)
    c = int(input("%d x %d = " % (a, i)))
    if (c == a*i):
        print("Correct")
        crt = crt+1
    else:
        print("Wrong")
        wrg = wrg+1
print("Correct = ", crt)
print("Wrong = ", wrg)
