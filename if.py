#Оператор if используется для проверки условий: если1 условие верно2
#выражений (называемый «if-блок»), иначе3
#выполняется другой блок выражений (называемый «else-блок»). Блок «else» является необязательным.
#Пример: (сохраните как if.py)
number = 23
guess = int(input('Введите целое число : '))
if guess == number:
    print('Поздравляю, вы угадали,') # Начало нового блока
    print('(хотя и не выиграли никакого приза!)') # Конец нового блока
elif guess < number:
    print('Нет, загаданное число немного больше этого.') # Ещё один блок
# Внутри блока вы можете выполнять всё, что угодно ...
else:
    print('Нет, загаданное число немного меньше этого.')
# чтобы попасть сюда, guess должно быть больше, чем number
print('Завершено')
# Это последнее выражение выполняется всегда после выполнения оператора if