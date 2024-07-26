# While Loops

A while loop lets us execute a series of statements as long as the condition (boolean expression) remains ``True``.

A while loop has the basic structure:

```python
while <condition>:
    # Do something until the condition is False
```

## 1. While Loop Using a Counter

A good portion of the ``while`` loops that you write will involve a counter variable.

The following example demonstrates a basic while loop that prints out the numbers ``1`` - ``5``:

```python
i = 1 # Define a variable i and bind the value 1 to it
while i < 6: 
    print(i)  # print out the value of i
    i += 1    # This increments i by 1. i.e. i = i + 1

print("Program has ended!")
```

Note the indentation here! The indented block is the loop body (the code that is executed inside the loop).

The above code first defines a counter variable ``i = 1``. It then defines a ``while`` loop that tests whether ``i < 6``. If this is ``True`` it prints out the value of ``i`` and then adds ``1`` to ``i``.

Note it is traditional to use ``i`` for a counter variable.

The image below demonstrates how the code runs:

![While loop animation](assets/while_gif.gif)

## 2. While Loop Using a Boolean Variable

Consider the following program which just keeps asking the user for a number until they enter a ``0``. Then the program ends.
```python
# loop until the user enters 0

input_string = input("Please enter a number:\n")
num = int(input_string)

while num != 0:
    input_string = input("Please enter a number:\n")
    num = int(input_string)

print("Program has ended!")
```
We can rewrite this program by using a ``bool`` variable (``program_over``) which keeps track of whether the ``while`` loop should continue or stop.

After a number is entered, we use an ``if`` statement to test if the number entered was ``0``, if it was, then we set ``program_over`` to ``True``. This will then stop the ``while`` loop and the program will end.
```python
# loop until the user enters 0

program_over = False

while program_over:
    input_string = input("Please enter a number:\n")
    num = int(input_string)
    if num == 0:
         program_over = True

print("Program has ended!")
```

## 3. Non-terminating While Loop

Now consider the code if you forget to increment (add to) ``i``.
```python
i = 1 # Define a variable i and bind the value 1 to it
while i < 6: 
    print(i)  # print out the value of i
```

This loop will repeat forever! ``i`` will never change its value from ``1`` and therefore the condition ``i < 6`` will forever remain ``True``. 

* What will be the output?
* Try it in **main.py**. To stop (exit) the program in the **console** press ``Ctrl + c``.


## 4. Nested While Loops

Just like ``if`` statements, we can nest loops. 

The following program shows an outer and an inner loop. This prints out the multiplication table.

```python
i = 1
while i < 13:
    j = 1
    while j < 13:
        print(f"{i} x {j} = {i*j}")
        j += 1
    i += 1
```

The outer loop has a counter variable ``i`` and the inner loop has a counter variable ``j``. Below is a flow diagram of the program.

![While loop multiplication flow](assets/while_multiplication_flow.png)

The following is of an animation of a similar program (below), but the conditions are changed to allow us to visualise it quicker.

```python
i = 1
while i < 3:
    j = 1
    while j < 3:
        print(f"{i} x {j} = {i*j}")
        j += 1
    i += 1
```

![While loop nested animation](assets/while_multi_gif.gif)

***
# === TASK ===
 
Use a while loop to print out the even numbers starting at 2 and up to and including 100.

```
2
4
6
.
.
.
100
```

Note that the dots represent numbers between 6 and 100. It saves us writing it all out!

HINT: You only need a single while loop.
***