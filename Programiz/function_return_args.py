def get_add(p, q):
    result = p + q # Here the result is local to this function only, we can make it global but it's not a best practice
    # print(f'the addition of {p} and {q} is {result}')
    return result # return result is a keyword that returns the value of the variable result to the function that called it
def main():
    a = 8 
    b = 10
    store = get_add(a,b) # Here we are storing the value returned by the function get_add in the variable store 
    print(f'the addition of {a} and {b} is {store}')
    return None
main()
# variables in a function although they have the same name, they're different







def multi_num(value):
    result = value*10
    return result
def main():
    output = multi_num(10)
    print(f'The value of a is {output}')
    return None
main()

