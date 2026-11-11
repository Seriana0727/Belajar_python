
def tentukan_kategori(usia):
    if usia <= 5:
        return "Balita"
    elif usia <= 11:
        return "Anak-anak"
    elif usia <= 17:
        return "Remaja"
    elif usia <= 59:
        return "Dewasa"
    else:
        return "Lansia"


nama = input("Masukkan nama: ")

while True:
    usia = int(input("Masukkan usia: "))

    if usia >= 0:
        break
    else:
        print("Usia tidak valid! Silakan masukkan ulang.")

kategori = tentukan_kategori(usia)

print("\n=== HASIL KATEGORI USIA ===")
print("Nama     :", nama)
print("Usia     :", usia, "tahun")
print("Kategori :", kategori)
