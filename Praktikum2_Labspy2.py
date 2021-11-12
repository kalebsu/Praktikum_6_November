a, b, c=(
    int(input('Masukkan Nilai a:')),
    int(input('masukkan Nilai b:')),
    int(input('Masukkan Nilai c:'))
)

if a>b and a>c:
    print('Nilai terbesar adalah A:' ,a)
elif b>a and b>c:
    print('Nilai terbesar adalah B:' ,b)
else:
    print('Nilai terbesar adalah C:' ,c)
