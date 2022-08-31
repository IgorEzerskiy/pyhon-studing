from curses.ascii import islower, isspace, isupper
import string

print("---Создаем пароль---\n", 'Пароль должен содержать: латинские буквы верхнего и нижнего регистров, цифры и символ "_". \n', "Пароль не должен привышать 8 символов и содержать пробелы. \n")

password=str(input("Введите ваш пароль: "))
count_num=0
count_probel=0
count_riska=0
count_latina_up=0
count_latina_down=0
count_rus=0
string_up=string.ascii_uppercase
string_low=string.ascii_lowercase
start_up=-1
start_low=-1

if len(password)>8:
    print("Пароль привышает 8 символов!!!")
    exit()

for k in password:
    if k.isupper()==True:
        while True:
            start_up=string_up.find(k,start_up+1)
            if start_up == -1:
                break
            count_latina_up+=1
    elif k.islower()==True:
        while True:
            start_low=string_low.find(k,start_low+1)
            if start_low == -1:
                break
            count_latina_down+=1

for i in password:
    if i.isdigit()==True:
        count_num+=1
    if i.isspace()==True:
        count_probel+=1
    if i=="_":
        count_riska+=1

count_rus=count_latina_up+count_latina_down+count_num+count_riska+count_probel
  
if count_latina_up<1:
    print("Добавьте в пароль символ верхнего регистра!!!")
if count_latina_down<1:
    print("Добавьте в пароль символ нижнего регистра!!!")
if count_num<1:
    print("Добавьте в пароль цыфры!!!")
if count_probel>0:
    print("Удалите пробле!!!")
if count_riska<0:
    print('Введите символ "_"')
if count_rus!=len(password):
    print("Пароль содержит символы кирилицы!!!")
