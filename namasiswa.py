print("=== NILAI SISWA ===")

nama = input("Nama siswa: ")
nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
    print("Predikat A")
elif nilai >= 80:
    print("Predikat B")
elif nilai >= 75:
    print("Predikat C")
else:
    print("Predikat D")

print("Nama:", nama)