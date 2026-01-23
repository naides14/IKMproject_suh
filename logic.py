import heap

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
    heap.pyr(xnew)
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

def daynumber(date): #возвращение номера дня по дате
    d=int(date[0:2])
    m=int(date[3:5])
    y=int(date[6:10])
    a=(14-m)//12
    b=y+4800-a
    c=m+12*a-3
    daynum=d+(((153*c+2)//5)+365*b+(b//4)-(b//100)+(b//400)-32045)
    return daynum

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
    heap.pyr(sums)
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
    if int(b)>int(e) or int(b)<0 or int(e)<0 or int(e)>2359 or len(b)>4 or len(e)>4 or int(b[2])>5 or int(e[2])>5:
        print('|ОШИБКА|: неправильное время')
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
        heap.pyr(times)
        validtimes = []
        tsorted = []
        for i in times:
            if i>=int(b) and i<=int(e):
                validtimes.append(i)
        for i in validtimes:
            i = str(i)
            if 9>=int(i)>=0:
                i='000'+i
            if i[0]!='0':
                i='0'+i
            if 59>=int(i)>=0:
                i='00'+i
            i = i[0:2] + ':' + i[2:4]
            tsorted.append(i)
    return tsorted




