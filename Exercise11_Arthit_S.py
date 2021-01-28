count = int(input("Number : "))
area = count

for i in range(count) :
    area -= 1
    print(" "*area,"*"*((i*2)+1))