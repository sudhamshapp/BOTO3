'''
def get_result(random):
    result = random + 10
    print(f'your result is {result}')
    return None
def main():
    # global number
    number = int(input('enter a number: '))
    get_result(number) #if we pass a variable while calling, is called arguments
    return None
main()
'''

'''
a = eval(input('enter a number: '))
b = eval(input('enter a number: '))
aresult = a + b
print(f'your result is {aresult}')
bresult = a - b
print(f'your result is {bresult}')
'''

def get_add(p, q):
    aresult = p + q
    print(f'the addition of {p} and {q} is {aresult}')
    return None
def get_sub(x, y):
    bresult = x - y
    print(f'the subtraction of {x} and {y} is {bresult}')
    return None
def main():
    a = eval(input('enter a number: '))
    b = eval(input('enter a number: '))
    get_add(a, b)
    get_sub(a, b)
    return None
main()


