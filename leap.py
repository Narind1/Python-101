#wap to check leap year by using function days in month
def is_leap(n): 
    return (n % 4 == 0) and (n % 100 != 0) or (n % 400 == 0)

def days_in_month(year, month):
    list_31 = [1,3,5,7,8,10,12]
    list_30 = [4,6,9,11]
    if month in list_31 :
        return 31
    elif month in list_30 :
        return 30
    elif is_leap(year) and month == 2:
        return 29
    else:
        return 28

x = int(input('Enter any year: '))
y  = int(input('Enter a month: '))

print(days_in_month(x,y))