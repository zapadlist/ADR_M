# This is my shoping list
shoplist = ['apples', 'mango', 'carrot', 'bananas']

print('I must ', len(shoplist), 'buy.')

print('Items:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nAlso I need to buy rice.')
shoplist.append('rice')
print('Now my shoplist is:', shoplist)

print('I need to sort my list')
shoplist.sort()
print('My sorted list looks like that:', shoplist)

print('Firstly, I need to buy', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print("I've bought", olditem)
print('Now my shoplist is:', shoplist)