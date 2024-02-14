# Scrieţi un program care tipăreşte tabla înmulţirii cu un număr natural între
# 2 şi 9 (numărul va fi citit de la tastatură).

print('Introduceti un numar din intervalul [2, 9]:');
n=int(input('n='))
if 2<=n<=9:
    print('Tabla inmultirii pentru numarul {n} este:');
    for i in range(1, 11):
        print('{} x {} = {}'.format(n, i, n*i));
else:
    print('Numarul introdus este gresit, incearca din nou!');
