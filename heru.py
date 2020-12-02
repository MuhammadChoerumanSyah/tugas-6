#penggunaan end
print('A', end='')
print('B', end='')
print('C', end='')
print()
print('X')
print('Y')
print('z')

#penggunaan separator

w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep='+')
print(w, x, y, z, sep='-')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='/')
print(w, x, y, z, sep='*')
print(w, x, y, z, sep='=')
print(w, x, y, z, sep='----')

print('{0:8} | {1:9}'.format('Nama orang','Jumlah'))
print('{0:8} | {1:9}'.format('Khabib',80.))
print('{0:8} | {1:9}'.format('Ronaldo',75))

