def get_add(p, q):
    aresult = p + q
    print(f'the addition of {p} and {q} is {aresult}')
    return None
def get_sub(x, y):
    bresult = x - y
    print(f'the subtraction of {x} and {y} is {bresult}')
    return None
def main():
    a = 8 
    b = 10
    get_add(a,b)
    get_sub(a,b)
if __name__ == "__main__":
    main()


'''
print('This is from script1:', __name__)
'''