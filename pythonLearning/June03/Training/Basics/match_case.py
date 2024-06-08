print('Match Case')
choice = int(input('Enter a number[1-5]: '))
match choice:
    case 1:
        print('One')
    case 2:
        print('Two')
    case 3:
        print('Three')
    case 4:
        print('Four')
    case 5:
        print('Five')
    case _:
        print('None')