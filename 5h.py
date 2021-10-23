# write a python program to reverse a string ."1234abcd"

str="1234abcd"
reverse_string=""
b=[]
count=len(str)
while count>0:
    reverse_string+=str[count-1]
    count=count-1
print(reverse_string)

