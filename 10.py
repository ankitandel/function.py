# write a python function to check whether a number falls in a given range.
def number(n):
    if n in range(6,20):
        print(n,"it is in the range")
    else:
        print(n,"the number is outside the given range")
number(13)