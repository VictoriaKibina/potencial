a=open('students.csv',encoding='utf8').readlines()
a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')
    if a[i][-1]=='None':
        a[i][-1]=0
    else:
        a[i][-1]=int(a[i][-1])
a.sort(key=lambda x:-x[-1])
for i in range(1,len(a)):
    value=a[i][-1]
    info=a[i]
    j=i-1
    while j>=0 and a[j][-1] < value:
        a[j+1]=a[j]
        j-=1
    a[j+1]=a[i]

k=0
print('10 класс')
for x in a:
    if '10' in x[3]:
        f,i,o=x[1].split()
        name=f'{i[0]}. {f}'
        k+=1
        print(f'{k} место: {name}')
        if k==3:
            break