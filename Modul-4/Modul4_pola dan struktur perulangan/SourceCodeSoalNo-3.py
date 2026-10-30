n = int(input("Masukkan bilangan bulat positif n: "))

jarak = 1

for i in range(1, n + 1):
    print("  " * (n - i), end="") 
    for j in range(1, i + 1):     
        print(j, end=" ")
    for j in range(i - 1, 0, -1): 
        print(j, end=" ")
    print("  " * (n - i), end="") 

    print(" " * jarak, end="")

    b = n - i + 1                        
    print("  " * (i - 1), end="")        
    for j in range(1, b + 1):            
        print(j, end=" ")
    for j in range(b - 1, 0, -1):        
        print(j, end=" ")
    print()