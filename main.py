# user_name = input('Ваше имя: ')
# greetings = lambda user_name : print(f'Приветствую, {user_name}!')
#
# greetings (user_name)


# a = int(input('Введите первое целое число: '))
# b = int(input('Введите второе целое число: '))
# result = lambda a, b : print(f'Результат: {2.4 * a ** 2 + (b - a / 2)}')
#
# result (a, b)




import time
import random

characters = [['Майор Гром', 2000, 400],
              ['Сергей Разумовский', 1000, 200],
              ['Птица', 5000, 600],
              ['Дима Дубин', 1000, 200],
              ['Юля', 1000, 200]]

a = random.randint(0, 4)
b = random.randint(1, 3)
c = random.randint(1, 3)

start_game = lambda characters : print('Приветствую вас! Подбираем персонажа...')
character = lambda characters : print(f'Ваш персонаж: Имя: {characters [a][0]}, здоровье: {characters [a][1]}, урон: {characters [a][2]}')

start_game (characters)

time.sleep(3)

character (characters)
