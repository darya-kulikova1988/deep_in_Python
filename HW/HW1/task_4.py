# 4. Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:

from random import randint 
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 10
num = None

num = int(randint(LOWER_LIMIT, UPPER_LIMIT))
# print(num)

while count > 0:
    print("try ", count)
    count -= 1

    print('Input number between', LOWER_LIMIT, 'and', UPPER_LIMIT, ': ')
    num_1 = int(input())
    # if num != num_1:
    #     print('You are wrong')
    if num < num_1:
        print('You are wrong, the number is smaller')
    elif num > num_1:
        print('You are wrong, the number is bigger')
    else:
        print('You are right!!! Number was input ', num)
        break

else:
    print('Исчерпаны все попытки, сожалею')
    quit()
