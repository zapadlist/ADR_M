#!/usr/bin/env python3

x = 50

def func(x):
	print('x равен', x)
	x = 2
	print('Замена локального х на', x)
	
func(x)
print('x по прежнему', x)