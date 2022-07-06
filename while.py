#!/usr/bin/env python3

number = 23
running = True # Мы присвоили значение True чтобы включить цикл, но условия могут быть и другими

while running:
	guess = int(input('Введите целое число: '))
	
	if guess == number:
		print('Поздравляю вы угадали')
		running = False # Это останавливает цикл
	elif guess < number:
		print('Нет, загаданное число немного больше этого.')
	else:
		print('Нет, загаданное число немного меньше этого.')
		
else:
	print('Цикл while окончен.')
	# Здесь можете выполнить все что вам еще нужно
	
print('Завершение')