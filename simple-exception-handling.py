# Errors are of two types: 1) syntax error 2) runtime error
# whenever we get the exceptions we can handle with try and except block
import sys
try:
    import boto3
except Exception as e:
    print(e)
    sys.exit() #it stops the execution of the program
# print(dir(boto3))
# print(dir(boto3.exceptions)) # these are list of available exceptions in boto3
print(dir(boto3.exceptions.botocore.exceptions))

