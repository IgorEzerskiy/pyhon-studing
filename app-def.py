import math

PI=math.pi

def radius():
    n=float(input('Введите радиус цилиндра в см: '))
    n/=2
    return n
def heihht():
    m=float(input('Введите висоту цилиндра в см: '))
    return m

def volume():
    r=radius()
    h=heihht()
    s=PI*r**2
    v=s*h
    return v

print('Объем цилиндра - ', format(volume(), '.2f'), 'см3')

def massa(g):
    n=float(input('Удельный вес г/см3: '))
    return g*n/1000
print('Вес цилиндра - ', format(massa(volume()), '.2f'), 'кг')