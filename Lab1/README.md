# Python Lab 1

This folder contains the Python programs completed for Lab 1.

---

## 1. Variable and Identifier Practice

### Aim
To declare variables for name, age, height, and student status, and display each variable along with its data type.

### Logic
Four variables are declared with different data types: string, integer, float, and Boolean.
The `type()` function is used to display the data type of each variable.

### Sample Input / Output

No input is required.

**Output:**

    Name: Pratishtha | Type: <class 'str'>
    Age: 19 | Type: <class 'int'>
    Height: 5.4 | Type: <class 'float'>
    Student: True | Type: <class 'bool'>

---

## 2. Greeting Program

### Aim
To take a user's name, age, and city as input and print a greeting using an f-string.

### Logic
The program takes the user's name, age, and city using `input()`.
An f-string is used to combine all three values into a single sentence.

### Sample Input / Output

**Input:**

    Enter your name: Pratishtha
    Enter your age: 19
    Enter your city: Dewas

**Output:**

    Hello Pratishtha, you are 19 years old and you live in Dewas.

---

## 3. Arithmetic Operations

### Aim
To perform basic arithmetic operations on two numbers.

### Logic
Two numbers are taken as input and converted into floating-point numbers.
The program calculates and displays their sum, difference, product, quotient, and remainder.

### Sample Input / Output

**Input:**

    Enter the first number: 10
    Enter the second number: 3

**Output:**

    Sum: 13.0
    Difference: 7.0
    Product: 30.0
    Quotient: 3.3333333333333335
    Remainder: 1.0

---

## 4. Celsius to Fahrenheit

### Aim
To convert a temperature from Celsius to Fahrenheit.

### Logic
The temperature in Celsius is taken as input and converted into a floating-point number.
The given conversion formula is used to calculate the Fahrenheit value.

### Sample Input / Output

**Input:**

    Enter temperature in Celsius: 25

**Output:**

    Temperature in Fahrenheit: 77.0

---

## 5. String Manipulation

### Aim
To perform different string operations on a full name.

### Logic
A full name is taken as input from the user.
The program converts the name to uppercase and lowercase, reverses it using slicing, and calculates its length.

### Sample Input / Output

**Input:**

    Enter your full name: Pratishtha Patel

**Output:**

    Uppercase: PRATISHTHA PATEL
    Lowercase: pratishtha patel
    Reversed: letaP ahtsihsitarP
    Length: 17

---

## 6. Escape Sequence Practice

### Aim
To create a simple receipt using tab and newline escape sequences.

### Logic
The program uses `\t` to align item names and prices.
Separate print statements are used to display the receipt neatly.

### Sample Input / Output

No input is required.

**Output:**

    ========== RECEIPT ==========
    Item            Price
    -----------------------------
    Burger          ₹120
    Fries           ₹80
    Cold Drink      ₹50
    -----------------------------
    Total           ₹250
    =============================

---

## 7. Menu-Driven Calculator (Optional)

### Aim
To create a menu-driven calculator that performs four basic arithmetic operations.

### Logic
The program displays a menu containing addition, subtraction, multiplication, division, and exit options.
It repeatedly accepts the user's choice and numbers until the user selects the exit option.

### Sample Input / Output

**Addition:**

    Enter your choice: 1
    Enter the first number: 10
    Enter the second number: 5

**Output:**

    Result: 15.0

**Division:**

    Enter your choice: 4
    Enter the first number: 10
    Enter the second number: 2

**Output:**

    Result: 5.0

**Exit:**

    Enter your choice: 5
    Calculator exited. Thank you!

---

## Programs Included

1. `variable_practice.py`
2. `greeting.py`
3. `arithmetic.py`
4. `celsius_to_fahrenheit.py`
5. `string_manipulation.py`
6. `escape_sequence.py`
7. `calculator.py` (Optional)