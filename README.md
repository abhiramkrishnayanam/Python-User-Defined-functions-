# Python-User-Defined-functions-

## Python User-Defined Functions Overview
### Function Basics
Functions in Python are blocks of code designed to perform specific tasks and can be reused across different parts of a program.

Basic Syntax:
```
def function_name(parameters):
    # Function body
    return result  # Optional
Defining a Function:
```
### Defining a Function 
```
def function_name(parameters):
    """ Optional docstring to describe the function."""
    # Code to execute
    return result  # Optional
```
### Explanation:
def: Starts the function definition.
function_name: Name of the function, describing its purpose.
parameters: Variables or placeholders for data the function will use.
return: Provides output to the caller; if omitted, None is returned by default.

## Calling a Function

Functions are called by their name, followed by parentheses. Arguments (if any) are placed within the parentheses.
```function_name(arguments)
```

### Function Arguments Python functions support several types of arguments to provide flexibility:

Positional Arguments: Based on their position in the function definition.
Syntax: 
```def function_name(param1, param2):
    # Code using param1 and param2
```

### Keyword Arguments: Named arguments that can be specified in any order.

Syntax:
 ```
def function_name(param1=value1, param2=value2):
    # Code using param1 and param2
```
### Default Parameters: Provide default values if no argument is given.
Syntax:

```def function_name(param1=default_value):
    # Code using param1
```
### Variable-Length Arguments:

*args: Allows for any number of positional arguments (gathered into a tuple).
**kwargs: Allows for any number of keyword arguments (gathered into a dictionary).

```
def function_name(*args, **kwargs):
    # Code that processes args and kwargs
```
### Return Values

The return statement outputs data from the function to the caller.
```
def function_name(parameters):
    # Code processing
    return result
```

[User defined functions assignment.pdf](https://github.com/user-attachments/files/17598092/User.defined.functions.assignment.pdf)


