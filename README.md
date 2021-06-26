# FizzBuzz
The classic game now done in python! Includes user input to make the game more personal!

The user gets to select as many numbers as they wish and what they want to call each of them. Then the user will be asked how high they'd like to count to.

Then the program will count from 0 to the user's specified number, checking for multiples of the numbers the user entered!

Give it a go yourself. Comments in the code will walk you through to make things clear.

Enjoy!

## `fizzbuzz.py`
The rules of FizzBuzz are simple, if a number is a multiple of 3 you shout "Fizz", a multiple of 5 you shout "Buzz", and if its both you shout "FizzBuzz"

This program goes a little further, it lets the user define what words they want to use and on what numbers. So the user could define multiples of 4 be assigned the word "Bang".

First we create an empty 2D list
```python
fb_list = ([], [])
```
Then we ask the user to input a name that they'd like to use for a multiple, and then the multiple itself. We do the name first so the user can type `exit` to exit the loop that asks them the question over and over so they can add as many conditions as they'd like without causing an error
```python
while user_names.strip().lower() != "exit":
    fb_list[0].append(user_number)
    fb_list[1].append(user_names)
    user_names = str(input("What would you like to call a number?\nType `exit` when you are done: "))
    if user_names.strip().lower() == "exit":
        break
    else:
        user_number = int(input("Type that number: "))
```
We append these values to the list, to create a pseudo-dictionary, with the multiple being the key and the name being the value.

Then we convert the list to a `zip` which is similar in structure to a `dict` except it is mutable, for some reason you can't go straight from `list` to `dict` so we use `zip` as a stopgap!

Using a `dict` is important too since `fb_dict` later on is going to be searched through, when this is done with a list it will throw an `indexError` which we don't want:
```python
fb_zip = zip(fb_list[0], fb_list[1])
fb_dict = dict(fb_zip)
```
Then we ask the user to what number they wish to count up to. Typically FizzBuzz is played from 0 to 100, but here the program is designed to count from 0 to whatever the user wants!
```python
limit = int(input("How high do we want to go: "))
```
Finally here is the part that makes the game possible, the FizzBuzz loop.
```python
for counter in range(limit): # counting from 0 to the limit
    output = "" # Preparing the output which we will modify based on whether or not the number will be Fizz or Buzz
    for number in fb_dict.keys(): # Scans through the dictionary for matching keys
        if counter % number == 0:
            output += fb_dict[number] # Adds the word to the current output
    if output == "": # If the output is still empty...
        output = counter # Add the current counter value to it...
    print(output) # Print the output for this loop
```

## OOP
There is an OOP version of this task on the OOP branch. You may find that [here](https://github.com/monotiller/engineering89_python_fizzbuzz_task/tree/oop)