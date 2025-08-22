print('Рады приветствовать Вас, в магазине NSK_store! \nПриятных покупок)')

order = {}
shop_mobile = ['iPhone XS', 'Samsung S10']
countries = ['Беларусь', 'Россия', 'Украина', 'Молдова']
ukraine_cities = ['Киев', 'Харьков', 'Львов']

print('\nУ нас в магазине 2 телефона:')
print('  1.', shop_mobile[0])
print('  2.', shop_mobile[1])

# Выбор телефона
while True:
    try:
        phone_choice = int(input('  Ваш выбор: > '))
        if phone_choice in (1, 2):
            order['Товар'] = shop_mobile[phone_choice - 1]
            break
        else:
            print('Пожалуйста, введите 1 или 2')
    except ValueError:
        print('Введите число (1 или 2)')

print(f"\nВы выбрали {order['Товар'].lower()}. Выберите страну доставки:")
for i, country in enumerate(countries, 1):
    print(f"  {i}. {country}")

# Выбор страны
while True:
    try:
        country_choice = int(input('  > '))
        if 1 <= country_choice <= 4:
            order['Страна'] = countries[country_choice - 1]
            break
        else:
            print('Пожалуйста, введите число от 1 до 4')
    except ValueError:
        print('Введите число от 1 до 4')

# Ввод имени
order['Имя'] = input('\nВаше имя: > ')

# Выбор города (особая логика для Украины)
if order['Страна'] == 'Украина':
    print('\nВыберите город:')
    for i, city in enumerate(ukraine_cities, 1):
        print(f"  {i}. {city}")
    
    while True:
        try:
            city_choice = int(input('  > '))
            if 1 <= city_choice <= 3:
                order['Город'] = ukraine_cities[city_choice - 1]
                break
            else:
                print('Пожалуйста, введите число от 1 до 3')
        except ValueError:
            print('Введите число от 1 до 3')
else:
    order['Город'] = 'столица'  # Для других стран

# Вывод заказа
print('\nВаш заказ:')
for key, value in order.items():
    print(f"{key} – {value}")




