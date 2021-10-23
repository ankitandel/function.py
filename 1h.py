# write a python function to sum all the numbers in a list.[8,2,3,0,7]

def add_number():
    num=[8,2,3,0,7]
    sum=0
    i=0
    while i<len(num):
        sum=sum+num[i]
        i=i+1
    print(sum)
add_number()

# def var(num1,num2):
#     a=num1+num2
#     return a
# var(8,2)
