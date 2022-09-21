import json

n_emp = int(input("Masukan jumlah karyawan baru: "))
for i_emp in range(1, n_emp+1):
    nama = input("Masukan nama: ")
    list_emp = list()
    list_kolega = list()
    alamat = input("Masukan alamat: ")
    dict_alamat = dict()
    dict_kolega = dict()
    n_kol = int(input("Masukan jumlah kolega: "))
    for i_kol in range(1, n_kol+1):
        kolega = input(f"Masukan nama kolega ke-{i_kol}: ")
        list_kolega.append(kolega)
    dict_alamat["Alamat"] = alamat
    dict_kolega["Kolega"] = list_kolega
    list_emp.append(dict_alamat)
    list_emp.append(dict_kolega)
    with open('karyawan.json','r') as file:
        data = json.load(file)
        data[nama] = list_emp
    with open('karyawan.json','w') as file:
        json.dump(data, file)
    print("=== Data berhasil ditambahkan ===")