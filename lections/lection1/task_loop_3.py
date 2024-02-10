min_limit = 0
max_limit = 10
while True:
    print('Input number between', min_limit, 'and', max_limit, ': ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('You are wrong')
    else:
        break
print('Number was input ', num)

