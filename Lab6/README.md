# Python Lab 6

This folder contains the Python programs completed for Lab 6.

---

# Section A: Concept Check

### 1. Menu-Driven Program

When a menu-driven program needs to remember something across multiple choices in the same run, that value must be stored **outside** the main loop, not inside it.

### 2. Random Number

To generate a random number in Python, you first need to **import** the random module.

### 3. Reverse Guessing Game

The computer narrows its guesses using feedback from the user, which is the same principle as a **binary search**.

### 4. ATM Simulation

If a withdrawal amount exceeds the current balance, the correct response is to **reject** the transaction and print an error.

### 5. While Loop

A while loop condition that depends on a variable changed inside the loop will only terminate if that variable is **updated** correctly on every iteration.

---

# Section B: Trace the Logic

## 1. ATM Simulation

The ATM starts with a balance of ₹5000.

| Operation | Balance |
|---|---:|
| Initial Balance | ₹5000 |
| Check Balance | ₹5000 |
| Withdraw ₹2000 | ₹3000 |
| Deposit ₹500 | ₹3500 |
| Withdraw ₹4000 | Rejected |

The ₹4000 withdrawal should be rejected because the current balance is only ₹3500. The balance must not become negative.

**Final Balance: ₹3500**

---

## 2. Reverse Guessing Game

The secret number is **37** and the range is **1 to 100**.

The computer uses the midpoint of the current possible range.

### Guess 1

Current range: `1–100`

Computer guesses:

`50`

Feedback: **Too high**

New range: `1–49`

### Guess 2

Current range: `1–49`

Computer guesses:

`25`

Feedback: **Too low**

New range: `26–49`

### Guess 3

Current range: `26–49`

Computer guesses:

`37`

Feedback: **Correct**

Therefore:

```text
50 → Too High
25 → Too Low
37 → Correct