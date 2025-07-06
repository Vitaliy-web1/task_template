print('Программа для оценивания')
print('Введите вашу оценку')
grade = float(input())

if 4.5 <= grade <= 5:
    star = ('⭐⭐⭐⭐⭐')
    print('Введите оценку:', grade)
    print('отлично', star)

elif 3.5 <= grade < 4.5:
    star = ('⭐⭐⭐⭐')
    print('Введите оценку:', grade)
    print('хорошо', star)

elif 2.5 <= grade < 3.5:
    star = ('⭐⭐⭐')
    print('Введите оценку:', grade)
    print('нормально', star)

elif 1.5 <= grade < 2.5:
    star = ('⭐⭐')
    print('Введите оценку:', grade)
    print('плохо', star)

elif 0 <= grade < 1.5:
    star = ('⭐')
    print('Введите оценку:', grade)
    print('ужасно', star)

if grade > 5:
    print('Такой оценки не существует')
