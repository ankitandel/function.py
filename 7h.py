# write a python program to execute a string containing python code.
str="ankita"
var=""
b=[]
count=len(str)
while count>0:
    var+=str[count+1]
    count=count+1
print(var)


