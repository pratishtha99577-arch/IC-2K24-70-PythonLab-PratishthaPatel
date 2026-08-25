# Python Lab 2

This folder contains the Python programs completed for Lab 2.

---

## 1. Armstrong Number

### Aim
To check whether a number is an Armstrong number and print all Armstrong numbers within a given range.

### Logic
The program calculates the number of digits and finds the sum of each digit raised to the power of the number of digits.
For the range version, every number in the given range is checked using the same Armstrong number function.

### Sample Input / Output

**Input:**

    Enter a number to check: 153

    Enter the starting value: 100
    Enter the ending value: 1000

**Output:**

    153 is an Armstrong number.

    Armstrong numbers between 100 and 1000:
    153 370 371 407

---

## 2. Prime Number

### Aim
To check whether a number is prime and print all prime numbers up to a given limit.

### Logic
A number is checked for divisibility starting from 3, while only testing possible divisors up to the square root of the number.
For the limit version, every number from 2 up to the given limit is checked using the prime-checking function.

### Sample Input / Output

**Input:**

    Enter a number to check: 17

    Enter the limit: 20

**Output:**

    17 is a prime number.

    Prime numbers up to 20:
    2 3 5 7 11 13 17 19

---

## 3. Perfect Number

### Aim
To check whether a number is a perfect number and print all perfect numbers up to a given limit.

### Logic
The program finds the proper divisors of a number and calculates their sum.
If the sum is equal to the original number, it is a perfect number. The same function is used to find perfect numbers up to the given limit.

### Sample Input / Output

**Input:**

    Enter a number to check: 28

    Enter the limit: 1000

**Output:**

    28 is a perfect number.

    Perfect numbers up to 1000:
    6 28 496

---

## 4. Palindrome

### Aim
To check whether a number is a palindrome using arithmetic operations and whether a string is a palindrome.

### Logic
For a number, digits are extracted using the remainder and integer division operators and a reversed number is constructed without converting the number to a string.
For a string, the text is compared with its reversed form after converting it to lowercase.

### Sample Input / Output

**Number Input:**

    Enter a number to check: 121

**Number Output:**

    121 is a palindrome.

**String Input:**

    Enter a string to check: madam

**String Output:**

    "madam" is a palindrome.

---

## 5. Fibonacci Series

### Aim
To print the first n Fibonacci terms using a loop and recursion and compare the number of recursive function calls.

### Logic
The loop version repeatedly updates two variables to generate the next Fibonacci term.
The recursive version calculates each term by calling the function for the two preceding terms, and a counter is used to count recursive function calls.

### Sample Input / Output

**Input:**

    Enter the number of Fibonacci terms: 10

**Output:**

    Fibonacci series using loop:
    0 1 1 2 3 5 8 13 21 34

    Fibonacci series using recursion:
    0 1 1 2 3 5 8 13 21 34

    Number of recursive function calls: 276

---

## 6. Pattern Printing

### Aim
To print a right-angled star triangle, a number pattern, and a centered pyramid using nested loops.

### Logic
Nested loops are used to control the number of symbols or numbers printed in each row.
For the centered pyramid, spaces are printed before the stars so that the pattern is centered.

### Sample Input / Output

**Input:**

    Enter the number of rows: 5

**Output:**

    1. Right-Angled Triangle
    *
    * *
    * * *
    * * * *
    * * * * *

    2. Number Pattern
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5

    3. Centered Pyramid
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *

---

## 7. Menu-Driven Application

### Aim
To combine the main programs from Lab 2 into a single menu-driven application.

### Logic
The program displays a menu containing Armstrong, Prime, Perfect Number, Palindrome, Fibonacci, Pattern Printing, and Exit options.
It accepts the user's choice, runs the corresponding operation, handles invalid choices, and returns to the menu until the user exits.

### Sample Input / Output

**Input:**

    Enter your choice: 1
    Enter a number: 153

**Output:**

    153 is an Armstrong number.

**Another Input:**

    Enter your choice: 2
    Enter a number: 17

**Output:**

    17 is a prime number.

**Exit:**

    Enter your choice: 7
    Exiting the Lab 2 application. Goodbye!

---

## 8. Number Guessing Game

### Aim
To create a number guessing game where the user guesses a randomly generated number within a maximum number of attempts.

### Logic
The program generates a random number between 1 and 100 and gives the user a maximum of 7 attempts.
After every guess, it tells the user whether the guess is too high, too low, or correct, and displays the number of attempts when the number is guessed.

### Sample Input / Output

**Sample Run:**

    ===== NUMBER GUESSING GAME =====
    I have chosen a number between 1 and 100.
    You have 7 attempts to guess it.

    Attempt 1 of 7
    Enter your guess (1-100): 50
    Too high!

    Attempt 2 of 7
    Enter your guess (1-100): 25
    Too low!

    Attempt 3 of 7
    Enter your guess (1-100): 37
    Correct! You guessed the number in 3 attempts.

---

# Analysis

## 1. For Loop vs While Loop

I preferred the `for` loop when the number of repetitions was known or when iterating through a range, such as checking numbers in the Armstrong, Prime, and Perfect Number programs and generating Fibonacci terms.

I preferred the `while` loop when repetition depended on a condition, such as validating user input, extracting digits, checking divisors, and keeping the menu running until the user chooses to exit.

---

## 2. Fibonacci: Loop vs Recursion

The recursive version repeats more work as `n` grows because the same smaller Fibonacci values are calculated multiple times.

The loop-based version is more efficient because each Fibonacci term is calculated once and the previous two values are reused.

---

## 3. Prime Number Check

The largest divisor that needs to be tested is the square root of the number, √n.

If a number has a factor larger than √n, it must have a corresponding factor smaller than √n. Therefore, if no divisor is found up to √n, the number is prime.

---

## 4. Number Guessing Game Strategy

The strategy that minimizes the number of guesses regardless of the range is **Binary Search**.

The user should guess the middle value of the remaining range each time and then eliminate either the higher half or the lower half based on the feedback.

---

# Programs Included

1. `armstrong.py`
2. `prime.py`
3. `perfect_number.py`
4. `palindrome.py`
5. `fibonacci.py`
6. `pattern_printing.py`
7. `menu_driven.py`
8. `number_guessing_game.py`

---

# Repository Structure

```text
IC-2K24-70-PythonLab-PratishthaPatel/
│
├── Lab1/
│   ├── variable_practice.py
│   ├── greeting.py
│   ├── arithmetic.py
│   ├── celsius_to_fahrenheit.py
│   ├── string_manipulation.py
│   ├── escape_sequence.py
│   ├── calculator.py
│   └── README.md
│
├── Lab2/
│   ├── armstrong.py
│   ├── prime.py
│   ├── perfect_number.py
│   ├── palindrome.py
│   ├── fibonacci.py
│   ├── pattern_printing.py
│   ├── menu_driven.py
│   ├── number_guessing_game.py
│   └── README.md
│
└── README.md