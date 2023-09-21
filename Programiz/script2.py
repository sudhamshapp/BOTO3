import script1
# print(dir(script1))
def get_mul(s, t):
    mresult = s * t
    print(f'the addition of {s} and {t} is {mresult}')
    return None
def main():
    a =8
    b = 10
    get_mul(a, b)
    script1.get_add(a, b)
    script1.get_sub(a, b)
    return None
if __name__ == "__main__":
    main()


'''
import script1
print('This is from script2: ', __name__)
'''
# what's the advantage of writing this means, when we're trying to import this code into another scripts at that time, you're avoiding the execution of main block
# in case, if we won't write this logic, unnecessarily you're gonna to execute your logic in another scripts 