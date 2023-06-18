#program to find fibonacci series using recursive function

def fibonacci_series(first, second, last_num, series):
    if (series + first) <= last_num:   
        series = first + second
        print(series, end = ' ')
        first = second
        second = series
        return fibonacci_series(first, second, last_num, series)
        
 


while True:
    first = 0
    second = 1
    series = 0
    last_num = int(input('\n\nEnter the Number till what you want the series:'))
    print('The Fibonacci series upto the given number is:')
    print(first, end = ' ')
    print(second, end = ' ')
    fibonacci_series(first, second, last_num, series)

    print('\n------------------------------------------------------------------------------------')
    ans = str(input('\n\t\tWish to continue(Y/N)?:')) 
    print('\n------------------------------------------------------------------------------------')

    if str.upper(ans) == 'Y':
        continue
    
    else:
        break