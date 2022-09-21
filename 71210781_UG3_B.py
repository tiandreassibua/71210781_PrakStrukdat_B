input_range = int(input("Masukan range data: "))
data = dict()

for x in range(input_range):
    if x % 2 ==0:
        n = x
        fak = 1
        for y in range(1, n + 1):
            fak *= y
        data[x] = fak
print(data)
cari = int(input("Data ditampilkan: "))
if cari in data.keys():
    print(str(cari)+'! adalah',data[cari])
else:
    print("Data tidak ditemukan")