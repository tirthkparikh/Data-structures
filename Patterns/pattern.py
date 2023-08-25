for i in range(1,6):
    
    if i == 1 or i==5:
        for j in range(5):
            print("*",end=" ")
    else:
            print("*",end=" ")
            for j in range(4):
               print(" ")  
            print("*",end=" ")
    print()