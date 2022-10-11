i=0
max=1000
a=""

f=open('id.txt', 'w')

while i<max:
    a=str(i)+"-kharkiv \n"
    f.write(a)
    print(a)
    i=i+1

f.close()
