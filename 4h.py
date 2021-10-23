# write a python program to print the even numbers from a given list.[1,2,3,4,5,6,7,8,9]

def is_even_num(b):
    i=0
    while i<=len(b):
        if i%2==0:
            print("even number",i,end="")
        else:
            print("odd number",i)
        i=i+1
b=[1,2,3,4,5,6,7,8,9]            
is_even_num(b)
