a=open('students.csv',encoding='utf8').readlines()
a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')

for i in range(len(a)):
    if 'Хадаров Владимир' in a[i][1]:
        print(f'Ты получил:{a[i][4]}, за проект - {a[i][2]}')
d={}
for i in range(len(a)):
    if a[i][4]!='None':
        clas=a[i][3]
        score = int(a[i][4])
        if clas not in d:
            d[clas]=[score]
        else:
            d[clas]+=[score]
for clas in d:
    d[clas]=round(sum(d[clas])/len(d[clas]),3)
for i in range(len(a)):
    if a[i][4] == 'None':
        a[i][4]=str(d[a[i][3]])
f=open('students.csv','w',encoding='utf')
f.writelines('id,Name,titleProject_id,class,score\n')
for x in a:
    f.writelines(','.join(x)+'\n')
f.close()
