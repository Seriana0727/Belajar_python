def hitung_diskon(harga_awal, persentase_diskon):
    harga_akhir = harga_awal - (harga_awal * persentase_diskon / 100)
    return harga_akhir

harga_awal = 100000
persentase_diskon = 20

print("Harga Awal: Rp", harga_awal)
print("Diskon:", persentase_diskon, "%")

hasil = hitung_diskon(harga_awal, persentase_diskon)

print("Harga Setelah Diskon: Rp", hasil)