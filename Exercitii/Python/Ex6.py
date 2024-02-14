# Se citesc două numere cifre nenule și distincte. Afișați cele două numere
# care pot fi formate cu acestea. Pentru 3 și 5, se va afișa 35 și 53.

def cifra_nenula_dif(n, m):
    return n.isdigit() and 1<=int(n)<=9 and n!=m;
while(True):
    n=input('Introduceti prima cfra:');
    if cifra_nenula_dif(n, ''):
        break;
    else:
        print('Introduceti o cifra nenula!');
while(True):
    m=input('Introduceti a doua cifra:')
    if cifra_nenula_dif(n, m):
        break;
    else:
        print('Cifrele trebuie sa fie nenule si diferite!');
numar1=n+m;
numar2=m+n;
print('Toate numerele formate cu cifrele', f"{n} si {m}", 'sunt:', numar1, numar2);
