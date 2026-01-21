import logic
import gui
c=0
f=1
sel=0
while sel!=4:
    f=1
    print('Программа "Персональный бюджет"')

    base = []
    try:
        with open('budget.csv', 'r') as f:
            for row in f:
                row = row.replace('\n', '')
                row = row.split(',')
                base.append(row)
        if len(base)==0:
            print('Ошибка: файл пуст')
            f=0
            break
        else:
            base.pop(0)
            print(f'Загружено {len(base)} записей')
    except (FileNotFoundError,IOError):
        print('Ошибка: файл не найден')
        f=0
        break

    if f!=0:
        sel=gui.menu()
        if sel==None:
            print('Ошибка: неправильный выбор отчета')
            f=0
        if f!=0 and sel==1:
            try:
                n = int(input('\n''Пожалуйста, введите число дней для сортировки поступлений: '))
            except ValueError:
                print('Ошибка: Введите число!')
                f=0
            if f!=0 and int(n)<=0:
                print('Ошибка: Введите натуральное число!')
                f=0

    if f!=0 and sel==1:

        base1=[i for i in base if i[2]=='INCOME']
        finalsorted=[]
        sortedtimes=logic.datesort(base1)                        # создание списка с отсорт. датами, сортировка записей в основном списке
                                                                 # соответствии с ним, затем - сортировка сумм
        logic.datesort2(sortedtimes,base1,finalsorted)
        logic.sumsort(finalsorted)



        print('\n',f'1) Список всех поступлений, отсортированный по дате и сумме по убыванию, за прошедшие {n} дней ')
        final2=[]
        for i in range(len(finalsorted)):
            final2.append(finalsorted[i])
            c+=1
            if c+1>n:
                break

        gui.outputmenu(final2)


    if f!=0 and sel==2:
            catglist={i[3] for i in base} #список с существующими категориями

            catg=input('\n''Пожалуйста, укажите категорию для сортировки поступлений (из TRANSPORTATION, ADVANCE, FOOD, SALARY, GIFT, ENTERTAINMENT): ')
            if catg not in catglist:
                print(('Ошибка: категории не существует, либо введено число'))
                f = 0
            else:
                base2 = [i for i in base if i[3] == catg and i[2]=='EXPENSE']
                if len(base2)==0:
                    print('Нет затрат по данной категории')
                    sel=gui.menu()
                else:
                    finalsorted=[]
                    sortedtimes=logic.datesort(base2)
                    logic.datesort2(sortedtimes, base2, finalsorted)    #сортировка дат (как с первым отчетом), затем сортировка по контрагентам и суммам
                    logic.cagentsort(finalsorted)
                    logic.sumsort(finalsorted)

                    print('\n''2) Список всех затрат, отсортированный по дате (по убыванию), контрагенту (по возрастанию), сумме (по убыванию) ')

                    gui.outputmenu(finalsorted)


    if f!=0 and sel==3:
            base3=[i for i in base if i[2]=='EXPENSE']
            base3times = []
            valtimes=logic.times(base3,0000,2370)
            if valtimes!=None:
                for i in range(len(base3)):
                    if (base3[i][1] in valtimes):
                        base3times.append(base3[i])
                print('\n','3) Список всех затрат, которые были понесены в определённом промежутке за все даты, отсортированный по сумме (убывание) и контрагенту (возрастание)')

                finalsorted=logic.sumsort2(base3times)
                logic.cagentsort(finalsorted)
                gui.outputmenu(finalsorted)







