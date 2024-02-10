# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

min_limit = 0
max_limit = 100000

while True:
    print('Input number between', min_limit, 'and', max_limit, ': ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('You are wrong')
    else:
        break

if num % num == 0 and num % 1 == 0:
    print('Number is simple')
else:
    print('Number is complex')