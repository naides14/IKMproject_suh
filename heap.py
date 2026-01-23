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