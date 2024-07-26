# Ranges and Lists  

Before we come onto ``for`` loops we must understand **ranges** and **lists**. 

# 1. List

A ``list`` in python is used to store multiple values in a single variable.

For example:

```python
list1 = [1,2,3]
```

```python
list2 = ["Citreon", "Ford", "Audi", "Mercedes"]
```

```python
list3 = ["Citreon", "Ford", 67, True]
```

You can access an element in a ``list`` using indexing. Each member of the ``list`` has an index number starting from ``0``.

For example the code,
```python
list3 = ["Citreon", "Ford", 67, True]
print(list3[0])
print(list3[2])
```
results in the output:
```
Citreon
67
```

Try creating your own ``list`` in the console and printing some of its elements.

For now, we will not discuss more about lists until later in the course. It suffices to know that they store multiple values and are **heterogeneous** (a fancy way of saying they can store different types). 

# 2. Ranges

A ``range`` allows us to create a sequence of numbers using the ``range()`` function.

```python
range(10) # This will create a range of numbers 0,1,2,3,4,5,6,7,8,9
```

```python
range(3, 10) # This will create a range of numbers 3,4,5,6,7,8,9
```

```python
range(2, 10, 2) # This will create a range of numbers 2,4,6,8
```

Ranges can take either:

* an end value ``range(end)``
* a start and end value ``range(start, end)``
* a start, end, and step value ``range(start, end, step)``

In some ways a ``range`` behaves like a ``list``, however, to save space, Python doesn't create the ``list``.

If you type the following into the console, you will see that the object type of a ``range`` is a ``range``!

```python
a = range(10)
print(type(a)) # prints <class 'range'>
```

So think of it as a convenient way to store a ``list`` of numbers without actually storing them!

By default ``start`` is ``0`` and ``step`` is ``1``.

So ``range(10)`` is the same as both ``range(0,10)`` and ``range(0,10,1)``.

## 2.1 Convert a Range to a List

If you try and print a ``range`` you won't get the numbers. Try the following in the console,

```python
a = range(10)
print(a)
```
and you will get the output:
```
range(0, 10)
```

You can convert the range to a list using the ``list()`` function. 

```python
a = list(range(2, 10)) # converts the range to a list [2,3,4,5,6,7,8,9]
print(a)
```
If you run the following code in the console or **main.py** you will get the output:

```
[2,3,4,5,6,7,8,9]
```

The ``list()`` function is forcing Python to build the **list** in memory.

To prove this to ourselves let's check the size of ``range(10**6)``. Note ``10**6 = 1000000``

```python
import sys
a = range(10**6)
print(sys.getsizeof(a))
```

This returns ``48`` which is 48 bytes of memory. Try a ``range`` of any size and you will always get ``48``.

Now let's convert it to a ``list`` and print the size:

```python
import sys
a = list(range(10**6))
print(sys.getsizeof(a))
```

This returns a whopping ``8000056`` (8 million) bytes, which is approximately ``166667`` times as large!

***
# === TASK ===

Using the ``range()`` and ``list()`` functions, print out the odd numbers from ``1`` up to and including ``99``.

Your output should look like this:

<!-- [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41,
> 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 
> 83, 85, 87, 89, 91, 93, 95, 97, 99]-->
```
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
```

HINT: Make sure you have read Section 2.1
***