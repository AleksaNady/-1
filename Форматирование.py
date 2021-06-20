name = 'leo'
age = 30

hello_str = 'Hello, ' + name + ' you ' + str(age) + ' лет'
print(hello_str)

#s строка, d число
hello_str = 'Hello, %s you %d лет'% (name, age)
print(hello_str)

hello_str = 'Hello, {} you {} лет'.format(name, age)
print(hello_str)