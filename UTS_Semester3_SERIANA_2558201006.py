nama = input ("Silahkan masukan nama mahasiswa : ")

while True:
    tugas = float(input("Masukan nilai tugas (0-100) : "))
    if 0 <= tugas <= 100:
        break
    else :
        print("Nilai yang anda masukan tidak sesuai!!. silahkan input ulang.")

while True:
    UTS = float(input("Masukan nilai UTS (0-100) : "))
    if 0 <= UTS <= 100:
        break
    else :
        print ("Nilai yang anda masukan tidak sesuai!!. silahkan input ulang.")

while True:
    UAS = float (input("Masukan nilai UAS (0-100) : "))
    if 0 <= UAS <= 100:
        break
    else :
        print ("Nilai yang anda masukan tidak sesuai!!. silahkan input ulang.")

Nilai_akhir = (tugas * 0.30) + (UTS * 0.30) + (UAS * 0.40)
if Nilai_akhir >= 85:
    Nilai_huruf = "A"

elif Nilai_akhir >= 70:
    Nilai_huruf = "B"

elif Nilai_akhir >= 55:
    Nilai_huruf = "C"

else:
    Nilai_huruf = "D"

if Nilai_huruf != "D":
    status = "LULUS!!"

else :
    status ="TIDAK LULUS!!"    

print("\n=== HASIL NILAI MAHASISWA ===")
print("Nama Mahasiswa :", nama)
print("Nilai Tugas    :", tugas)
print("Nilai UTS      :", UTS)
print("Nilai UAS      :", UAS)
print("Nilai Akhir    :", Nilai_akhir)
print("Nilai Huruf    :", Nilai_huruf)
print("Status         :", status)
