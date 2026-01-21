
def heap(a,i,m):
    l=i*2+1
    r=l+1
    if l>=m:
        return
    k=l
    if r<m and a[r]>a[l]:
        k=r
    if a[i]<a[k]:
        j=a[i]
        a[i]=a[k]
        a[k]=j
        heap(a,k,m)

def uporheap(a,m):                                           #сортировка кучей
    for g in range(m//2,-1,-1):
        heap(a,g,m)

def pyr(a):
    m=len(a)
    uporheap(a,m)
    while m>1:
        temp=a[0]
        a[0]=a[m-1]
        a[m-1]=temp
        m=m-1
        heap(a,0,m)

def days(specbase):
    temp = []
    daylist=[]
    for i in range(len(specbase)):
        temp.append(int(specbase[i][0]))

    for i in temp:
        daylist.append[i[6:8]]
    print(daylist)

def datesort(specbase): #взятие дат из основного списка, сортировка и возвращение списка отсортированных дат в исходном формате
    x=[]
    xnew=[]
    xdone=[]
    for i in range(len(specbase)):
        x.append(specbase[i][0])

    for i in x:
        i = i.replace('.', '')
        i = i[4:8] + i[2:4] + i[0:2]
        i=int(i)
        xnew.append(i)
    pyr(xnew)
    for i in xnew:
        i=str(i)
        i=i[6:8]+'.'+i[4:6]+'.'+i[0:4]
        xdone.append(i)
    return xdone[::-1]

def datesort2(stimes,specbase,finsort): #сопоставление дат из списка дат с датами из основного списка и сортировка
    for i in range(len(stimes)):
        for j in range(len(specbase)):
            if stimes[i]==specbase[j][0]:
                finsort.append(specbase[j])
                specbase.pop(j)
                break
    return finsort
def sumsort(x):
    for i in range(len(x)-1): #СОРТИРОВКА ПО СУММЕ ЕСЛИ ДАТЫ В ЗАПИСЯХ РАВНЫ (отчет 1)
        if x[i][0]==x[i+1][0] and int(x[i][4])<int(x[i+1][4]):
            temp=x[i]
            x[i]=x[i+1]
            x[i+1]=temp
        if x[i][0]==x[i+1][0] and x[i][5]==x[i+1][5] and int(x[i][4])<int(x[i+1][4]): #СОРТИРОВКА ЕСЛИ ДАТЫ И КОНТРАГЕНТЫ РАВНЫ (отчет 2)
            temp=x[i]
            x[i]=x[i+1]
            x[i+1]=temp
    return x

def sumsort2(specbase): #получение сумм из основного списка, их сортировка, расположение записей основного списка в соответствии с отсортированными суммами
    finsort=[]
    sums=[]
    for i in range(len(specbase)):
        sums.append(int(specbase[i][4]))
    pyr(sums)
    sums=sums[::-1]
    for i in range(len(sums)):
        for j in range(len(specbase)):
            if str(sums[i])==specbase[j][4]:
                finsort.append(specbase[j])
                specbase.pop(j)
                break
    return finsort

def cagentsort(x):
    for i in range(len(x)-1):  # СОРТИРОВКА ПО КОНТРАГЕНТУ ЕСЛИ ДАТЫ В ЗАПИСЯХ РАВНЫ
        if x[i][0] == x[i + 1][0] and len(x[i][5]) > len(x[i + 1][5]):
            temp = x[i+1]
            x[i+1] = x[i]
            x[i] = temp
        elif int(x[i][4]) == int(x[i + 1][4]) and len(x[i][5]) > len(x[i + 1][5]): #ЕСЛИ СУММЫ РАВНЫ
            temp = x[i + 1]
            x[i + 1] = x[i]
            x[i] = temp
    return x

def times(specbase,b,e): # получение времени из основного списка, его сортировка и преобразование в исходный формат
    if b>e or b<0 or e<0 or e>2359 or len(str(b))>4 or len(str(e))>4:
        print('Ошибка: неправильное время')
        return
    else:
        x = []
        times = []
        for i in range(len(specbase)):
            x.append(specbase[i][1])
        for i in x:
            i = i.replace(':', '')
            i = int(i)
            times.append(i)
        pyr(times)
        rtimes = []
        xdone = []
        for i in times:
            if i>=int(b) and i<=int(e):
                rtimes.append(i)
        for i in rtimes:
            i = str(i)
            if 9>=int(i)>=0:
                i='000'+i
            if i[0]!='0':
                i='0'+i
            if 59>=int(i)>=0:
                i='00'+i
            i = i[0:2] + ':' + i[2:4]
            xdone.append(i)
    return xdone




