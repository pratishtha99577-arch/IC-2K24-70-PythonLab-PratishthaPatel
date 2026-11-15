import random

while True:
    print("\n--- MENU ---")
    print("1. Armstrong Number")
    print("2. Fibonacci Series")
    print("3. Number Guessing Game")
    print("4. Concentric Number Square")
    print("5. Palindrome Number")
    print("6. Patterns")
    print("7. Prime Number")
    print("8. Perfect Number")
    print("9. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        num = int(input("Enter number: "))
        temp = num
        s = 0

        while temp > 0:
            digit = temp % 10
            s = s + digit ** 3
            temp = temp // 10

        if s == num:
            print("Armstrong Number")
        else:
            print("Not Armstrong Number")

    elif ch == 2:
        n = int(input("Enter terms: "))
        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            c = a + b
            a = b
            b = c
        print()

    elif ch == 3:
        num = random.randint(1, 100)

        for i in range(7):
            guess = int(input("Guess number: "))

            if guess == num:
                print("Correct Guess!")
                break
            elif guess > num:
                print("Too High")
            else:
                print("Too Low")
        else:
            print("Game Over! Number was", num)

    elif ch == 4:
        n = int(input("Enter size: "))

        for i in range(2*n-1):
            for j in range(2*n-1):
                print(max(abs(n-1-i), abs(n-1-j))+1, end=" ")
            print()

    elif ch == 5:
        num = int(input("Enter number: "))
        temp = num
        rev = 0

        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp = temp // 10

        if num == rev:
            print("Palindrome Number")
        else:
            print("Not Palindrome")

    elif ch == 6:
        n = int(input("Enter rows: "))

        print("1. Star Triangle")
        print("2. Number Pattern")
        print("3. Centered Pyramid")

        p = int(input("Choose pattern: "))

        if p == 1:
            for i in range(1, n+1):
                for j in range(i):
                    print("*", end=" ")
                print()

        elif p == 2:
            for i in range(1, n+1):
                for j in range(1, i+1):
                    print(j, end=" ")
                print()

        elif p == 3:
            for i in range(1, n+1):
                for j in range(n-i):
                    print(" ", end="")
                for k in range(2*i-1):
                    print("*", end="")
                print()

        else:
            print("Invalid Pattern Choice")

    elif ch == 7:
        num = int(input("Enter number: "))

        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    print("Not Prime")
                    break
            else:
                print("Prime Number")
        else:
            print("Not Prime")

    elif ch == 8:
        num = int(input("Enter number: "))
        s = 0

        for i in range(1, num):
            if num % i == 0:
                s = s + i

        if s == num and num > 0:
            print("Perfect Number")
        else:
            print("Not Perfect Number")

    elif ch == 9:
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")