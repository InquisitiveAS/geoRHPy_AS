__author__ = "Abhishek S Shinde"
__copyright__ = "EXDAS"
__contact__ = "arabhishek1091@gmail.com"

def reverse_String(userString):

    resultantString = ""
    
    for i in range(len(userString)):
        #Error:'str' object has no attribute 'append'
        #Error: resultantString.append(userString[(len(userString)-1)- i])
        resultantString += userString[(len(userString)-1)-i]
        
    return resultantString


#UserCases:
print(reverse_String("water"))
print ("Pass" if ('retaw' == reverse_String('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == reverse_String('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == reverse_String('The house code is: 2343')) else "Fail")
