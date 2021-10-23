# write a python program to access a function inside a python.
def sqr(n):
    return(n**2)


user=int(input("Enter the number  "))    
i=1
while i<=user:
    print(i,sqr(i))
    i=i+1
    


