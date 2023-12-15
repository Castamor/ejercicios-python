num = int(input("\nTECLEA UN NÚMERO:\n>>> "))

for x in range(num):

    for y in range(num):

        if(x == 0 or x == num-1):
            print("*", end="  ")
        else:
            if(y == 0 or y == num-1):
                print("*", end="  ")
            else:
                print("   ", end="")
        
        if(y == num-1):
            print("\n",end="")
            if(x == num-1): print("")