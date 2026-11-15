n = int(input("Enter number: "))

for i in range(2*n-1):
    for j in range(2*n-1):
        print(max(abs(n-1-i), abs(n-1-j)) + 1, end=" ")
    print()