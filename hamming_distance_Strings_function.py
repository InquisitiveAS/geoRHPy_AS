__author__ = "Abhishek S Shinde"
__copyright__ = "EXDAS"
__contact__ = "arabhishek1091@gmail.com"

"""
In information theory, the Hamming distance between two strings of equal length is the 
number of positions at which the corresponding symbols are different. 
Hamming distance is a metric for comparing two binary data strings. While comparing two 
binary strings of equal length, Hamming distance is the number of bit positions in which the
two bits are different. The Hamming distance between two strings, a and b is denoted as d(a,b)
"""
def hammingDistance(userString1,userString2):
    
    if len(userString1) == len(userString2):
        count = 0
        
        # != is the symbol we use for the not equal operator.
        for i in range(len(userString1)):
            if  userString1[i] != userString2[i]:
                count +=1
        
        return count
    return None




#User Cases
print ("Pass" if (10 == hammingDistance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
print ("Pass" if  (1 == hammingDistance('shove','stove')) else "Fail")
print ("Pass" if  (None == hammingDistance('Slot machines', 'Cash lost in me')) else "Fail")
print ("Pass" if  (9 == hammingDistance('A gentleman','Elegant men')) else "Fail")
print ("Pass" if  (2 == hammingDistance('0101010100011101','0101010100010001')) else "Fail")