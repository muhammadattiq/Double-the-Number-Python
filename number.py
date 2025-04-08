## This Prgram will double the number which is given by user in input box, and it will double it till 100 ##

number = int(input("please enter a number to double it : "))

for i in range(1,100):
    number = number*2
    print(number, " ")
    if(number>100):
        break