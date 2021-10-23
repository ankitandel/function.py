# Write a Python function that takes a number as a parameter and check the
# number is prime or not.Note : A prime number (or a prime) is a natural number
# greater than 1 and that has no positive divisors other than 1 and itself.

def number(n):
    if n%2!=0 or n==2:
        print("it is prime number")
    else:
        print("it is not prime number")
number(4)
