# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain" agar dono 
# numbers even (2 se divide hote hain) nahi toh print kare "Dono numbers even nahi hai"
# Question (Part 2)
# def check_numbers(ankita,pooja):
#    print(ankita,"dono even hai")
#    print(pooja,"dono even nahi hai")

# check_numbers("4","3")

    


# Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko arguments ki tarah le aur fir 
# check kare ki same index waale dono integers even hain ya nahi. Yeh check karne ke liye pichle Part 1
#  mein likhe check_numbers function ka use karo. Agar aapne apne function ko [2, 6, 18, 10, 3, 75] aur 
#  [6, 19, 24, 12, 3, 87] Toh usko yeh output deni chaiye
def check_number(num1,num2):
   i=0
   while i<len(num1):
      if num1[i]%2==0 and num2[i]%2==0:
         print("dono even hai")
      else:
         print("dono even nahi hai")
      i=i+1
check_number([2,6,18,10,3,75],[6,19,24,12,3,87])
