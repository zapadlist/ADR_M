#!/usr/bin/env python3

while True:
	s = input('Введите что-нибудь: ')
	if s == 'выход':
		break
	else:
		print('Вы не угадали')
	print('Длина строки:', len(s))
	if len(s) < 3:
		print('Слишком мало')
		continue
	
print('Завершение')
