'''
Implementación de Diffie-Hellman vulnerable a Pohlig-Hellman.

Se genera un número primo vulnerable, siendo p - 1 un número liso, en este caso 389-liso.

La función discrete_log de la librería sympy ejecuta el algoritmo Pohlig-Hellman entre otros, y puede tardar un par de minutos en obtener el resultado. Si intentamos utilizar esta función con un primo seguro no lo obtendremos nunca.

Autor: Daysapro.
'''

from random import choice
from sympy import isprime
from sympy.ntheory import discrete_log
from secrets import randbelow

def generate_vulnerable_prime(n):
    primes = [2, 3, 4, 17, 169, 277, 389]
    i = 1
    while True:
        i *= choice(primes)
        if isprime(i + 1) and i > 2**n:
            return i + 1

def generate_private_key(n):
    return randbelow(2**n)

def generate_public_key(private_key, g, p):
    return pow(g, private_key, p)

p = 3714892429
g = 2212633605
A = 3298958249

a2 = discrete_log(p, A, g)
print("La clave recuperada del logaritmo discreto es: {a2}".format(a2=a2))
