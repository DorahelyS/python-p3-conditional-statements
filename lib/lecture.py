'''
Python has slightly different syntax for writing conditional statements using if/else than JavaScript. Here's a relatively complex if/else statement in JavaScript:

// JavaScript
let dog = "cuddly";
let owner;

if (dog === "hungry") {
  owner = "Refilling food bowl.";
} else if (dog === "thirsty") {
  owner = "Refilling water bowl.";
} else if (dog === "playful") {
  owner = "Playing tug-of-war.";
} else if (dog === "cuddly") {
  owner = "Snuggling.";
} else {
  owner = "Reading newspaper.";
}

can also write like this in JS:


Here's how we can write the equivalent statement in Python:
let dog = "cuddly";

if (dog === "hungry") {
  let owner = "Refilling food bowl.";
} else if (dog === "thirsty") {
  let owner = "Refilling water bowl.";
} else if (dog === "playful") {
  let owner = "Playing tug-of-war.";
} else if (dog === "cuddly") {
  let owner = "Snuggling.";
} else {
  let owner = "Reading newspaper.";
}
^
using let to declare a new variable owner within each if and else if statement. However, this will result in a 
scope issue because the owner variable will only be accessible within the block where it is declared. 
Therefore, you won't be able to access the owner variable outside of the if...else statement.

To fix this, you can declare the owner variable outside of the if...else statement and assign its value 
within each condition.


# Python
dog = "cuddly"

if dog == "hungry":
    owner = "Refilling food bowl."
elif dog == "thirsty":
    owner = "Refilling water bowl."
elif dog == "playful":
    owner = "Playing tug-of-war."
elif dog == "cuddly":
    owner = "Snuggling."
else:
    owner = "Reading newspaper."

Notice that the owner variable here was not defined above like it would be in JavaScript. This is because 
Python does not require the variable to be declared or initialized prior to the conditional. In Python, a 
variable can be in scope for the entire class or function. Therefore, we can use the owner variable for the 
rest of the class since it is in local scope.

Truthy/Falsy Values
In order to use control flow effectively, it's important to know what values Python treats as "truthy" and "falsy".

As we saw in the lesson on data types, there are many values Python considers falsy:

Empty lists []
Empty tuples ()
Empty dictionaries {}
Empty sets set()
Empty strings '' or ""
Zero of any numeric type (0, 0.0)
None
And, of course, False

Conditional Expressions
Python also allows us to use conditional expressions (or ternary operators) to evaluate the truthiness of complex 
statements in a single line.

JS:
let age = 1;

let is_baby = (age < 2) ? 'baby' : 'not a baby';

PY:
age = 1

is_baby = 'baby' if age < 2 else 'not a baby'

This is the equivalent of the following if/else statement:

age = 1
if age < 2:
  is_baby = 'baby'
else:
  is_baby = 'not a baby'

value_if_true if condition else value_if_false

try/except Statements:
Throughout our Python assignments so far, we have seen a number of different Exceptions. As we learned in our "Error Messages" lesson, Exceptions are a type of error that we can intercept so that our Python application can continue to run. try/except statements are the tool that allow us to perform these interceptions.

Let's take a look at how we might handle a common mathematical exception. Copy the following code into the Python shell and try to run the divide() function with different arguments.

def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except:
        print("An error occurred")

Use of the finally keyword at the end of a try/except statement allows us to perform actions that we want to occur regardless of whether or not an exception has been thrown.

Dictionary Mapping
Unlike JavaScript, Python does not have switch/case statements. Python can handle switch/case logic in if/else statements, but for very long sets of conditions, it may be worthwhile to use dictionary mapping instead.

IMPORTANT Python 3.10 has introduced match/case statements which function very similarly to switch/case statements in JavaScript. 

// JavaScript
let dog = "cuddly";
let owner;

switch (dog) {
  case "hungry":
    owner = "Refilling food bowl.";
    break;
  case "thirsty":
    owner = "Refilling water bowl.";
    break;
  case "playful":
    owner = "Playing tug-of-war.";
    break;
  case "cuddly":
    owner = "Snuggling.";
    break;
  default:
    owner = "Reading newspaper.";
    break;
}

This switch/case statement takes the status of the dog as a string and sets the state of the owner accordingly.

Let's take a look at how we might do that with an if/elif/else statement in Python:

# Python
dog = "cuddly"

if dog == "hungry":
    owner = "Refilling food bowl."
elif dog == "thirsty":
    owner = "Refilling water bowl."
elif dog == "playful":
    owner = "Playing tug-of-war."
elif dog == "cuddly":
    owner = "Snuggling."
else:
    owner = "Reading newspaper."
As you can see, there is some repeated code in dog ==, but the code is still more concise than with a true switch/case statement in JavaScript.


Now let's look at how we would handle this with dictionary mapping. Copy and paste the following code into the Python shell:

dog = "cuddly"

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = dict_map.get(dog, "Reading newspaper.")

The .get method returns the value associated with the key if it exists in the dictionary, 
and if not, it returns the default value specified. 