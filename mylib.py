while True: 
    name = input('Кто разработал Пайтон? : ').lower() 
    if name == "гвидо": 
        print('Правильно!') 
        break 
    elif name == "россум": 
        print('Правильно!') 
        break 
    elif name == 'гвидо ван россум': 
        print('Правильно!') 
        break 
    else: 
        print("Попробуй ещё раз") 
        continue