# write a python function to check whether string in pangram or not.
def var_numbers():
    str= "The quick brown fox jumps over the lazy dog"
    b="a b c d e f g h i j k l m n o p q r s t u v w x y z"
    a=True

    for i in b:
        if i not in str:
            a=False
    if (a==True):
        print("yes")
    else:
        print("no")
var_numbers()












