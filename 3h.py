# write a python function that takes a list and returns a new list with unique elements of the first list.
# list=[1,2,3,3,3,4,5]

def unique_list(list_):
    x=[]
    i=0
    while i<len(list_):
        if list_[i] not in x:
            x.append(list_[i])
        i=i+1    
    print(x)
list_1=[1,1,2,3,3,3,4,4,5]    
unique_list(list_1)
