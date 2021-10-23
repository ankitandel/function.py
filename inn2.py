# Ek perfect() naam ka function define kijiye jo ki ek parameter lega aur uss parameter ko hume check karana hai ki vo perfect number
#  hain ya nahi. Iske baad uss function ko use karke ek program likhiye jo ki 1 se 1000 tak sabhi perfect numbers ko print kare.
# [ hum ek aise integer number ko perfect number kahenge jo ki uske sabhi factors ( including 1 & excluding itself) ka sum uss number
#  ke barabar hota hai. Example:- Expected Output :- 

def ek_perfect(num):
    sum=0
    i=1
    while i<num:

        if num%i==0:
            sum=sum+i
        i=i+1

    if num==sum:
        print("perfect number",num)
    else:
        print("not perfect",num)
    
ek_perfect(6)

