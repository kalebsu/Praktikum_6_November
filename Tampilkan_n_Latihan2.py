import random
# n untuk menampung list data
n=int(input("Masukkan jumlah n: "))

# nilai i = 0 karena array dihitung dari angka 0 bukan 1
i=0

# mengeluarkan nilai acak dari angka 0 - 0.5
x=random.uniform(0,0.5)

#logika
while i<n:
  print(x)
  x +=0.01
  i +=1