# ⏳ Python Countdown Timer

A simple countdown timer written in Python.  
The program asks the user for a number of seconds, validates the input, and then counts down to zero.

---

## 📜 Full Code

```python
import time

while True:
    user_input = input("Enter number of seconds to begin the timer: ")

    if not user_input.isdigit():  # Check if the input is a valid number
        print("Please enter a valid number.")
        continue

    seconds = int(user_input)

    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)

    print("Time's up!")
    break
````

---

## 🔍 How It Works

### 1. Import the `time` Module

```python
import time
```

The `time` module allows the program to pause using `time.sleep(1)` so the countdown happens once per second.

---

### 2. Infinite Loop (`while True`)

```python
while True:
```

This loop keeps running until the user enters valid input.
If the input is invalid, the program will ask again.

---

### 3. User Input

```python
user_input = input("Enter number of seconds to begin the timer: ")
```

The program asks the user to enter the number of seconds for the countdown.

---

### 4. Input Validation

```python
if not user_input.isdigit():
    print("Please enter a valid number.")
    continue
```

* `isdigit()` checks if the input contains only digits.
* If invalid:

  * An error message is printed.
  * `continue` restarts the loop.

---

### 5. Convert to Integer

```python
seconds = int(user_input)
```

Since `input()` returns a string, it must be converted to an integer before using it in a loop.

---

### 6. Countdown Loop

```python
for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)
```

* Starts at the entered number.
* Counts down to 1.
* Decreases by 1 each iteration.
* Waits 1 second between numbers.

Example (if user enters `5`):

```
5
4
3
2
1
Time's up!
```

---

## ✅ Key Concepts Used

* `while` loop
* `for` loop
* `input()` function
* `.isdigit()` validation
* Type conversion (`str` → `int`)
* `time.sleep()` delay
* `break` statement

---



