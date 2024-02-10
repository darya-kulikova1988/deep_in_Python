min_limit = 0
max_limit = 10
count = 3
num = None

while count > 0:
    print("try ", count)
    count -= 1

    print('Input number between', min_limit, 'and', max_limit, ': ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('You are wrong')
    else:
        break

else:
    print('Исчерпаны все попытки, сожалею')
    quit()

print('Number was input ', num)

