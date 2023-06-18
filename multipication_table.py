#program to print multiplication table of a given range using recursive function

def table(multiplicant, multiplier, rnge):

    if(multiplicant <= rnge):
        ans = multiplicant * multiplier
        print(multiplicant, '*', multiplier, ' = ', ans)

        if multiplier < 10:
            table(multiplicant, (multiplier+1), rnge)
    
        elif multiplier == 10:
            multiplier = 0
            print('--------------------------------------------------------------------')
            table((multiplicant+1), (multiplier+1), rnge)

        else:
            return 

while True:
    
    multiplier = 1
    multiplicant = int(input('Enter the Number from where you want to start the Multiplication Table?:'))
    rnge = int(input('Enter the range till which you want the Multiplication Table?:'))
    
    ans = table(multiplicant, multiplier, rnge)
    

    ans1 = str(input('\n\t\tWish to continue(Y/N)?:'))
    print('\n------------------------------------------------------------------------------------')


    if str.upper(ans1) == 'Y':

        continue
    
    else:

        break

