berat = float (input("masukan berat badan anda (kg) : "))
tinggi_cm = float (input("masukan tinggi badan anda (cm) : "))

tinggi = tinggi_cm / 100
bmi = berat / (tinggi * tinggi)

print ("BMI anda adalah : ", round (bmi, 2))
if bmi < 18.5 :
    print (" kategori : kurus")
elif 18.5 <= bmi < 25 :
    print ("kategori : normal")
elif 25<= bmi <30:
    print("kategori : gemuk (overweight)")
else :
    print ("kategori : obesitas")