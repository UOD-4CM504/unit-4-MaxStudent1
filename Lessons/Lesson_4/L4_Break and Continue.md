# Break and Continue

``break`` and ``continue`` are keywords in python that allow you to stop the loop or skip the current iteration.

Many times programmers use ``break`` and ``continue`` when they don't need to. Generally ``break`` and ``continue`` can lead to funny flows in your program and bugs. If you can avoid using them then do!

## 1. Break

The ``break`` keyword allows us to exit ("break") out of a loop early. We can do this with both ``while`` and ``for`` loops.

### Example 1.1

The following program will stop short of printing the numbers ``0,1,2,3,4,5,6,7,8,9`` and only print ``0,1,2,3,4``. 

If you need to convince yourself, copy and paste this into **main.py**.
```python
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
```
The program tests each value of ``i`` and if it is equal to ``5`` the program exits the loop.

We can write this without the ``break``.

```python
i = 0
while i < 5:
    print(i)
    i += 1
```
### Example 1.2
Here is the same program with a ``for`` loop
```python
for i in range(0,10):
    if i == 5:
        break
    print(i)
```
We can write this without the ``break``.
```python
for i in range(0,5):
    if i < 5:
        print(i)
```
## 2. Continue

The ``continue`` keyword allows us to skip the current iteration of a loop. We can do this with both ``while`` and ``for`` loops.

### Example 2.1

The following program will not print out the number ``5``, but all other numbers. 

So the output will be the numbers ``0,1,2,3,4,6,7,8,9``. Notice that ``5`` is missing.

If you need to convince yourself, copy and paste this into **main.py**.
```python
i = -1
while i < 9:
    i += 1
    if i == 5:
        continue
    print(i)
```
The program tests each value of ``i`` and if it is equal to ``5`` the program exits the loop.

We can write this without the ``continue``.

```python
i = 0
while i < 10:
    if not i == 5:
        print(i)
    i += 1
```
### Example 2.2
Here is the same program with a ``for`` loop
```python
for i in range(0,10):
    if i == 5:
        continue
    print(i)
```
We can write this without ``continue``.

```python
for i in range(0,10):
    if not i == 5:
        print(i)
```

## 3. No Do...While

To date in Python, we have seen a while loop that will check a condition and execute a code block until the condition becomes False.
```python
while <condition>
    # Do something 
```

In many languages it is possible to do the following:

```
do
  run a block of code
while <condition>
```

This guarantees that the code block runs at least once as the while <condition> is checked after the code block.

One of the major reasons Python does not support such a statement is that it breaks the indentation rule that a code block should be indented. Here it isn't!

### 3.1. Try Not To Use Break

It is quite common to see the following in Python.

```python
while True:
    # do something
    if <condition>:
        break
```

The following essentially emulates a do...while loop. Here is an example.

```python
# The Number Guessing Game 
import random

# randomly generate a number between 1 and 10
secret_guess = random.randint(1,10)

print("Welcome to the Number Guessing Game!")
print("You need to try and guess the number between 1 and 10...")

while True:
    guess = int(input("Please enter a guess:\n"))
    
    print("That is not correct, please try again.")
    
    if guess == secret_guess:
        break
    
print(f"Well done the correct answer is {secret_guess}")
```

However, the use of a ``break`` statement here relies on the person reading this to implicitly understand that the programmer is intending to use a do...while.

There are also other reasons we would not want to do this in other languages which are compiled to do with the fetch-decode-execute cycle. 

We can easily rewrite this with an additional boolean.

```python
# The Number Guessing Game 
import random

# randomly generate a number between 1 and 10
secret_guess = random.randint(1,10)

print("Welcome to the Number Guessing Game!")
print("You need to try and guess the number between 1 and 10...")

game_over = False

while not game_over:
    guess = int(input("Please enter a guess:\n"))
    
    print("That is not correct, please try again.")
    
    if guess == secret_guess:
        game_over = True
    
print(f"Well done the correct answer is {secret_guess}")
```

Now, these are almost identical, however, it is now more clear that the ``while`` will end when ``gameover`` is set to `True`. This conveys the programmers' intention.


*** 
# === TASK ===
Print out the numbers ``1`` to ``100`` but leave out the meaning of life ``42``.

Use a ``continue`` statement.
***