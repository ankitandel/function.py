# add_numbers naam ka function likhiye jo do numbers ko arguments ke tarah le aur fir unka sum print karta
# hai. Arguments ka naam number1 aur number2 hona chahiye.

# def add_number(num1,num2):
#     print(num1+num2)
# add_number(56,12)


# add_numbers_list naam ka function likhiye jo do integers ki 2 lists leta ho aur fir same position wale 
# integers ka sum print karta ho. Same position waale 2 integers ka sum karne ke liye Part 1 mein di gayi 
# add_numbers waale function ka use karo. Jaise agar hum iss function ko [50, 60, 10] aur [10, 20, 13]
# denge ko woh yeh print karega
def add_number(num1,num2):
    i=0
    while i<len(num1):
        print(num1[i]+num2[i])
        i=i+1
add_number([50,60,10],[10,20,13])
