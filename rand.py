# Rand val maker of lenth 64 for easy implementation into base64
# This is good for password generation as well

import sys
from random import randint 

# List of values
alphanum = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
             'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F',
             'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
             'W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','-','_']

def rand():
        """ This will generate a random string of a provided length"""
        length = int(input('How long of a value? As an int. '))
        listOfValues = []
        for i in range(0,length):
                listOfValues.append(alphanum[randint(0,63)])
        stringOfValues=''.join(listOfValues)
        print(stringOfValues)

if __name__ == '__main__':
        sys.exit(rand())

        
