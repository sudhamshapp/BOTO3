# the name variable accepts, whatever the value sent as an argument during the function call 
def greet(name):
    print("Hello", name)
greet('sudhamsh')    # here sudhamsh is the argument

# Passing multiple Arguments to a Function

def add_numbers(num1, num2):
    result =  num1 + num2
    print(result)
number1 = 5
number2 = 7
add_numbers(number1, number2)    


# Return Value from a function
# However, it's best to find sum inside the function and print the result somewhere else using the return statement.

def add_numbers(num1, num2):
    result =  num1 + num2
    # print(result)
    return result
number1 = 5
number2 = 7
output = add_numbers(number1, number2)    
print(output)



# when the return statement is encountered, immediately the function stops executing, then
def greet(name):
    print("Hello", name)
    return
    print('How do you do') # this won't get executed because it's after the return statement
greet('sudhamsh')


def greet():
    name = 'sudhamsh'
    return name
greet()
