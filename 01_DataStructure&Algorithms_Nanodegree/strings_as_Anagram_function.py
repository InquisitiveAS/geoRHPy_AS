__author__ = "Abhishek S Shinde"
__copyright__ = "EXDAS"
__contact__ = "arabhishek1091@gmail.com"

"""
Exceptions: No punctuation, No numbers, No special character
A function which takes two strings and returns True or False   
"""

def anagram_checker(userString1,userString2):
    
    if len(userString1) != len(userString2):
        #Clean the strings
        clean_str1 = userString1.lower()
        clean_str2 = userString2.lower()
        
        if sorted(clean_str1) == sorted(clean_str2):
            return True
    else:
        
        return False


#UserCases:
print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")
