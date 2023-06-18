#program to find the sum of odd, even or simple integere number in given range using recursive function



def sum_simple(init, end):

    if init > end:
        return 0

    else:
        return init + sum_simple((init+1), end)

def sum_even_odd(init, end):

    if init > end:
        return 0

    else:
        return init + sum_even_odd((init+2), end)


def findsum(init, end, _type):

    if str.lower(_type) == 'even':

        if init % 2 == 0:
            total = sum_even_odd(init, end)
            print('\t\tThe Sum of all the even number in given range is:', total)

        else:
            init = init + 1
            total = sum_even_odd(init, end)
            print('\t\tThe Sum of all the even number in given range is:', total)


    elif str.lower(_type) == 'odd':

        if init % 2 != 0:
            total = sum_even_odd(init, end)
            print('\t\tThe Sum of all the odd number in given range is:', total)

        else:
            init = init + 1
            total = sum_even_odd(init, end)
            print('\t\tThe Sum of all the odd number in given range is:',total)


    elif str.lower(_type) == 'simple':
        total = sum_simple(init, end)
        print('\t\tThe Sum of all the integer number in given range is:',total)

    else: 
        print('\t\tEnter the right choice')


while True:
    
    print('\n\t\t\t    PROGRAM TO FIND SUM OF THE NUMBERs')
    start_num=int(input('\t\tEnter the starting number from where you want the sum?:'))
    last_num=int(input('\t\tEnter till which number you want the sum?:'))
    _type=str(input('\t\tEnter the type of sum you want (Odd/ Even /Simple):'))
    print('------------------------------------------------------------------------------------')

    findsum(start_num, last_num, _type)

    print('------------------------------------------------------------------------------------')
    ans = str(input('\n\t\tWish to continue(Y/N)?:'))
    print('\n------------------------------------------------------------------------------------')


    if str.upper(ans) == 'Y':

        continue
    
    else:

        break