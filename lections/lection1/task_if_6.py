
color = input('your favourite color: ')
match color:
    case 'red' | 'orange':
        print('you like bright')
    case 'green':
        print('you like grass')
    case'blue':
        print('you like ocean')
    case _:
        print('i dont understand')
