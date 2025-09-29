#Funções Primitivas Recursivas:
def s(x: int): # função sucessor
    return x + 1
def z(x: int): # função zero
    return 0
def u(i: int, z: list): # função projeção
    return z[i-1]


#Criando novas funções:

def add(x: int, y: int): # função adição
    if y == 0:
        print ('add ({}, 0) = {}'.format(x,x))
        return x
    else:
        print ('add ({}, {}) = s (add ({},{})'.format(x,y,x,y-1))
        return s(add(x,y-1))

def sg(x: int): # função sinal (signal) de x: retorna 0 se x = 0 e 1 em todos os outros casos.
    if x == 0:
        print ('sg (0) = z (0) = 0')
        return z(x)
    else:
        print ('sg ({}) = s (z ({}))'.format(x, x))
        return s(z(x))

def nsg (x: int): # função sinal 'barrado'
    if x == 0:
        return s(z(x))
    else:
        return z(x)

def a(x: int): # função antecessor
    if x <= 0:
        return z(x)
    else:
        return x-1

def sub(x: int, y: int): # função subtração própria
    if y <= 0:
        print ('sub ({}, 0) = {}'.format(x,x))
        return x
    else:
        print ('sub ({}, {}) = a (sub ({}, {})'.format(x,y,x,y-1))
        return a(sub(x,y-1))

def dabs(x: int, y: int): # função valor absoluto da diferença entre x e y: f(x,y) = |x-y|
    print ('|{}-{}| = add ((sub ({},{}), sub {}, {}))'.format(x, y, x, y, y, x))
    return add(sub(x,y), sub(y,x))

def m(x: int, y: int): # função multiplicação
    if y == 0:
        print ('m ({},0) = z ({}) = 0'.format(x,x))
        return z(x)
    else:
        print ('m ({}, {}) = add (m ({}, {}), {})'.format (x, y, x, y-1, x))
        return add(m(x,y-1),x)

def mod(x: int, y: int): # função 'mod': f(x,y) = y mod x
    if y == 0:
        print ('0 mod {} = z ({}) = 0'.format(x,x))
        return z(x)
    else:
        print ('{} mod {} = m (s (mod{}, {})), sg (dabs ({},s (mod ({}, {})))))'.format(y, x, x, y-1, x, x, y-1))
        return m(s(mod(x,y-1)), sg(dabs(x,s(mod(x,y-1)))))

def _min (x: int, y: int): # função min
    print ('min ({}, {}) = sub ({}, sub ({}, {}))'.format (x, y, x, x, y))
    return sub (x, sub (x, y))

def _max (x: int, y: int): # função max
    print ('max ({}, {}) = add ({}, sub ({}, {}))'.format (x, y, x, x, y))
    return add (x, sub (x,y))

def eq(x: int, y: int): # função 'testa igual': retorna 1 se os argumentos forem iguais, e 0 em todos os outros casos
    print ('eq ({}, {}) = nsg ( dabs ({}, {}))'.format (x, y, x, y))
    return nsg( dabs (x, y))
print(mod(2,2))