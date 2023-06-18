# program to find factorial of the given number using recursive function
def recursive_factorial(n):

    if n == 0:
        return 1
    
    else:
        return n * recursive_factorial(n-1)

while True:

    num = int(input('\nEnter the Number:'))

    if num < 0:
        print("Factorial doesn't exist")

    else:
        print('Factorial of ', num,' is:= ', recursive_factorial(num))
    
    print('--------------------------------------------------------------------------------------')
    ans = str(input('\n\t\tWish to continue(Y/N)?:'))
    print('\n------------------------------------------------------------------------------------')

    if str.upper(ans) == 'Y':
        continue
    
    else:
        break
    

