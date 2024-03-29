def hash(s):
    s=s[1]
    p=67
    m=10**9 + 9
    for i in range(len(s)):
        h+=A.find(s[i])*p**i
    h=h%m
    return h
A='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЭЮЯ'
a=A.lower()
A='*'+A+a+''
a=open('students.csv',encoding='utf8').readlines()
shapka=a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')
f=open('students_with_hash.csv','w',encoding='utf8')
f.write(shapka)
for x in a:
