from capitalize.capitalize import capitalize

'''
if capitalize('hello') != 'Hello':
   raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')
'''
assert capitalize('hello') == 'Hello'
assert capitalize('') == ''

#print('Все тесты пройдены!')
