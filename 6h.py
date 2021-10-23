# write a pyhton function that accepts a string and calculate the number of upper case letters and lower 
# case letters .sample string:
# 'The quick Brow Fox',Expected output :no,of upper case charactor:3, no,lower case charactor:12
def countcharactor( string):
    upper=0
    lower=0
    for ch in string:
        if ch.islower():
            lower+=1
        elif ch.isupper():
            upper+=1
    print("lower",lower)
    print("upper",upper)
countcharactor('The quick Brow Fox')


