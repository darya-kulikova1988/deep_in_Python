year = int(input('input year in format yyyy: '))
if year % 4 != 0:
    print('Simple')
elif year % 100 == 0:
    if year % 400 == 0:
        print('leap year')
    else:
        print('simple')
else:
    print('leap year')
