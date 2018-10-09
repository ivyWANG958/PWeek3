 # ex1 Rock Paper Scissors

print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors':2, 'paper':3}
    user_a = str(input('user a : '))
    user_b = str(input('user b : '))
    a = game_dict.get(user_a)
    b = game_dict.get(user_b)
    dif = a - b

    if dif in [-1,2]:
        print('user a wins')
        if str(input("do you want to contine? yes or no\n")) == 'yes':
            continue
        else:
            print("game over")
            break
    elif dif in [-2,1]:
        print('user b wins')
        if str(input("do you want to contine? yes or no\n")) == 'yes':
            continue 
        else:
            print("game over")
            break
    else:
        print("tie, please continue")
        print('')

    #? have to input with '' ( i.e. 'paper', 'yes')

