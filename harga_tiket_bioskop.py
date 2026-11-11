umur = int(input("masukan umur anda : "))
hari = input("masukan hari (Senin-Minggu) : ").lower()

harga = 50000

if umur < 12 or umur> 60 :
    harga = harga * 0.5
    print ("Diskon 50% diberikan")

if hari == "sabtu" or hari == "minggu" :
    harga = harga + 15000
    print ("Biaya tambahan weekend : Rp15.000")

print ("Total yang harus anda bayar : Rp",int(harga))     
