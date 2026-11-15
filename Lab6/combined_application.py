import random

while True:
    print("\n===== MAIN MENU =====")
    print("1. ATM Simulation")
    print("2. Student Grade Calculator")
    print("3. Guessing Game")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    # ATM Simulation
    if ch == 1:
        balance = 5000

        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Back to Main Menu")

            c = int(input("Enter choice: "))

            if c == 1:
                print("Balance:", balance)

            elif c == 2:
                amount = int(input("Enter amount: "))
                balance += amount
                print("Deposited successfully")

            elif c == 3:
                amount = int(input("Enter amount: "))
                if amount <= balance:
                    balance -= amount
                    print("Withdrawn successfully")
                else:
                    print("Insufficient balance")

            elif c == 4:
                break

            else:
                print("Invalid choice")

    # Student Grade Calculator
    elif ch == 2:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "Fail"

        print("Student:", name)
        print("Grade:", grade)

    # Guessing Game
    elif ch == 3:
        num = random.randint(1, 50)
        score = 100

        while True:
            guess = int(input("Guess number (1-50): "))

            if guess == num:
                print("Correct Guess!")
                print("Score:", score)
                break

            else:
                score -= 10

                if num % 2 == 0:
                    print("Hint: Even number")
                else:
                    print("Hint: Odd number")

                if num % 5 == 0:
                    print("Hint: Multiple of 5")
                else:
                    print("Hint: Not a multiple of 5")

                print("Wrong Guess! Score:", score)

    elif ch == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")