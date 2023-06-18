#program to find the prime number using recursive function

import math

def findprime(init_num, last_num):
    if init_num <= last_num:
        if init_num == 2:
            print(init_num, end = ' ')
            return findprime((init_num + 1), last_num)

        x = math.sqrt(init_num)
        y = x - math.floor(x)
        if y == 0:
            return findprime((init_num + 1), last_num)
        
        elif init_num % 2 == 0:
            return findprime((init_num + 1), last_num)
    
        else:
            i = 3
            x = math.floor(math.sqrt(init_num))
            while i < (x+2):
                if init_num % i == 0:
                    return findprime((init_num + 1), last_num)

                else:
                    i = i + 2
                    continue 

            else:
                print(init_num, end = ' ')
                return findprime((init_num + 1), last_num)
    
                
while True:
    begin_num = int(input('\nEnter the number from where you want to find the prime number:'))
    end_num = int(input('Enter the range till which you want to find the prime number:'))

    if begin_num < 0 or end_num < 2 or begin_num>= end_num:
        print('\t\t!!!Invalid Input!!!')   


    #print('The prime number present between the given range is:')
    findprime(begin_num, end_num)

    print('\n------------------------------------------------------------------------------------')
    ans = str(input('\n\t\tWish to continue(Y/N)?:'))
    print('\n------------------------------------------------------------------------------------')

    if str.upper(ans) == 'Y':

        continue
    
    else:

        break
