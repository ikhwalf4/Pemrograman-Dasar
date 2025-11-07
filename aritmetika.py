# Ikhwal Fauzi
# D0425002
# Program Aritmatika Sederhana

def tambah(a, b):
    return a + b  
def kurang(a, b):
    return a - b
def kali(a, b):
    return a * b
def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Tidak bisa dibagi dengan nol!"

print("--- Program Aritmatika Sederhana ---")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Pilih operasi (1-4): ")

try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
except ValueError:
    print("Input tidak valid! Harap masukkan angka.")
    exit()

if pilihan == '1':
    print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
elif pilihan == '2':
    print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
elif pilihan == '3':
    print(f"Hasil: {angka1} x {angka2} = {kali(angka1, angka2)}")
elif pilihan == '4':
    print(f"Hasil: {angka1} ÷ {angka2} = {bagi(angka1, angka2)}")
