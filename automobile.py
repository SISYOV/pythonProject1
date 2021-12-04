while True:
    print('enter automobile model')
    automobile = input()
    if automobile in ['mondeo', 'focus', 'kuga']:
        print('ford')
    elif automobile in ['tipo', 'panda', '500']:
        print('fiat')
    elif automobile in ['clio', 'megan', 'duster']:
        print('renault')
    elif automobile == 'exit':
        break
    else:
        print('model of car not exist')
