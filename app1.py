i=0
max=10000
a=""

f=open('id.txt', 'w')

while i<max:
    a=str(i)+"-kyiv \n"
    f.write(a)
    print(a)
    i=i+1

f.close()
