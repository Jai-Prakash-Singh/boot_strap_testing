import math 


def input_any_choice_to_print_area():

    answer = True

    print "choice     Find"
    print "1.         Area of Square"
    print "2.         Area of rectangle"
    print "3.         Area of triangle"

    while answer:	
	your_choice = raw_input("enter your choice")
	
	try:
	    your_choice = int(your_choice)

	    if your_choice == 1:
	        side = int(raw_input("enter the side for square: "))
	        print "The area of square is: %s " %(side * side)
		answer = False 
	    elif your_choice == 2:
	        length = int(raw_input("enter a length for rectangle: "))
		breadth = int(raw_input("enter the breadth of rectangle: "))
		print "The area of rectangle  is: %s " %(length* breadth)
		answer = False
	    elif your_choice == 3:
                x = int(input("enter first side of triangle"))
		y = int(input("enter second side of triangle"))
		z = int(input("enter third side of triangle"))
		s = (x+y+z)/2
		A = ((s-x)*(s-y)*(s-z))**0.5
		print"Area=",A
		answer = False
	    else:
	       print "Try again"
	        	        
	except:
	    print "please enter the integer number between 1 -3 "



def reverse_of_input():
    # 3. Write a program to input any number and to find reverse of that number.
    num = int(raw_input("enter a number to reverse: "))
    revnum  = 0

    while (num > 0):
        revnum = revnum*10  +  num%10
	num = num /10

    print "Reverse number is %s" %(revnum)



def factor_of_number():
    number =int(raw_input("enter a number: "))
    

    factor_list = []

    for i in range(1, number):
        mod_num = number % i 
        if (mod_num == 0):
	    quotent = number / i
	    if quotent not in factor_list:
	        factor_list.extend([i, quotent])

    print factor_list




def armstrong_num():
    num = int(raw_input("enter a number for armstrong: "))
    copy_num = str(num)[:]

    length = len(str(num))
    if length == 1:
        print "this numbser is armstrong  because it only one digint number "
    elif length == 2:
        print " this is not a armstrong number because it is a 2 digit number "
    else :
        result = 0
	
	while num:
	    result +=  math.pow(num%10, length)
	    num = num/10

	if result  ==  int(copy_num):
	    print "yes it is a armstrong number"
	else:
	    print "no this number is not a armstrong number"
        print 



def check_prime_number():
    realnum = int(raw_input("enter a number: "))
    sqr_num = int(realnum**0.5)

    if realnum == 2:
        print "yes it is a primen number"
 
    else:
        num = 2
        loop = True

        while loop and (num <= sqr_num):
	    if (realnum % num) == 0:
	        print "no it not a prime number"
                loop = False
	    num += 1

	if loop is  True:
	    print "Yes it is a prime number"



def prime_number():
    realnum = int(raw_input("enter a number: "))

    for i in xrange(1, realnum):
        if all(i%m!=0 for m in xrange(2, i)):
	    print i



 
def decimal_to_binary():
    decimal_number = int(raw_input("enter decimal number to convert it into binary: "))

    print "Your number is %i " %(decimal_number)
    binary_list = []

    while decimal_number:
        binary_mod  = decimal_number % 2
	decimal_number = decimal_number / 2 
	binary_list.append(binary_mod)
	

    binary_list.reverse()
    print binary_list



def binary_to_decimal():
    l = int(raw_input("enter binary number like 111100: "))
    print "your printed  binary number is %i" %(l)

    sum_bin = 0 
    index = 0 

    while l :
        last_num = l % 10
	sum_bin += last_num * 2**index
	l  = l / 10
	index += 1

    print "now decimal number is %i" %(sum_bin)


def diff_list_tup():
    a = tuple(range(1000))
    b = list(range(1000))

    a.__sizeof__() # 8024
    b.__sizeof__() # 9088

    #Permitted operations

    b    = [1,2]   
    b[0] = 3       # [3, 2]

    a    = (1,2)
    #a[0] = 3       # Error

    # id
    a     = (1,2)
    b     = [1,2]  

    id(a)          # 140230916716520
    id(b)          # 748527696

    a   += (3,)    # (1, 2, 3)
    b   += [3]     # [1, 2, 3]

    id(a)          # 140230916878160
    id(b)          # 748527696
    
    #Usage

    a    = (1,2)
    b    = [1,2] 

    c = {a: 1}     # OK
    #c = {b: 1}     # Erro
   


def  reverse_of_n_num():
    forward_number_list = []
    for i in range(0, 10):
        forward_number_list.append(int(raw_input("enter the number %i: " %(i))))

    for i in range(10, 0, -1):
        print forward_number_list[i-1]


if __name__== "__main__":
    #Write a program to input n numbers and to reverse the set of numbers without using functions.
    reverse_of_n_num()     

    #Differentiate between tuple and list.
    #diff_list_tup()

    #Write a program to input two complex numbers and to implement multiplication of the given complex
    #numbers.
    # ft = in * 0.083333

    #Write a program to convert binary to decimal.
    #binary_to_decimal()


    #Write a program to convert decimal number to binary.
    #decimal_to_binary()

    #Write a program to find all prime numbers up to given number
    #check_prime_number()
    #prime_number()

    #11. Write a program to input any number and to check whether given number is Armstrong or not 
    #.(Armstrong 1,153,etc. 13 =1 , 13+53 +33 =153)
    #armstrong_num()

    #10. Write program to input any number and to print all factors of that number.
    #factor_of_number()

    # 3. Write a program to input any number and to find reverse of that number.
    #reverse_of_input()

    #input_any_choice_to_print_area()
    


