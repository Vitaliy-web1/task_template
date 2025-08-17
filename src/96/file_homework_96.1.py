tickets = {}
ticket_counter = 1  
    
print('Добро пожаловать на сайт ОАО "Российские железные дороги"')
while True:
    choice = input('\nВведите 1, чтобы приобрести билет на поезд\nВведите 2, чтобы просмотреть все билеты\nВведите 3, чтобы выйти\nВаш выбор: ')
    
    if choice == '1':
        print('\n=== Процесс покупки билета ===')
        route = input('Укажите маршрут следования (Например: Москва - Владивосток): ')
        
        name = input('Введите Фамилию и инициалы пассажира (Фамилия И.О.): ')
        if not name:
            print('Ошибка: Поле <Пассажир> не может быть пустым')
            continue
        
        passport = input('Введите серию и номер паспорта пассажира (XX XX XXXXXX): ')
        if not passport:
            print('Ошибка: Поле <Паспорт> не может быть пустым')
            continue
        
        place = input('Введите номер места в вагоне: ')
        if place in tickets:
            print(f'Ошибка: Место №{place} уже занято')
            continue

        ticket_number = f"РИ20{str(ticket_counter).zfill(5)} {passport.replace(' ', '')[:6]}"
        
        tickets[place] = {
            'ticket_number': ticket_number,
            'route': route,
            'name': name,
            'passport': passport,
            'place': place
        }
        
        ticket_counter += 1
        print(f'\nБилет №{ticket_number} успешно оформлен на место №{place}!')
    
    elif choice == '2':
        print('\n=== Список оформленных билетов ===')
        if not tickets:
            print('Нет оформленных билетов')
        else:
            for place, ticket in tickets.items():
                print(f"\n* * * Место №{place} * * *")
                print(f"Билет № {ticket['ticket_number']}")
                print(f"Маршрут: {ticket['route']}")
                print(f"Пассажир: {ticket['name']}")
                print(f"Паспорт: {ticket['passport']}")
    
    elif choice == '3':
        print('\nСпасибо за использование нашей системы. До свидания!')
        break
    
    else:
        print('\nОшибка: Неверный ввод. Пожалуйста, выберите 1, 2 или 3')
