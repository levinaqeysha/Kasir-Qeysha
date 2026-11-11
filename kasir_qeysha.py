print("================================")
print("     APLIKASI KASIR RESTORAN")
print("================================")

total = 0

while True:
    print("\nDAFTAR MENU MAKANAN")
    print("1. Nasi Goreng  - Rp25.000")
    print("2. Mie Ayam     - Rp15.000")
    print("3. Ayam Geprek  - Rp20.000")
    print("4. Sate Ayam    - Rp30.000")
    print("5. Bakso        - Rp18.000")
    print("0. Selesai Memilih")

    pilihan = int(input("\nPilih menu (0-5): "))

    if pilihan == 0:
        break

    elif pilihan == 1:
        nama = "Nasi Goreng"
        harga = 25000
    elif pilihan == 2:
        nama = "Mie Ayam"
        harga = 15000
    elif pilihan == 3:
        nama = "Ayam Geprek"
        harga = 20000
    elif pilihan == 4:
        nama = "Sate Ayam"
        harga = 30000
    elif pilihan == 5:
        nama = "Bakso"
        harga = 18000
    else:
        print("Pilihan tidak tersedia!")
        continue

    jumlah = int(input("Masukkan jumlah pesanan: "))
    subtotal = harga * jumlah
    total += subtotal

    print("Menu       :", nama)
    print("Subtotal   : Rp", subtotal)
    print("Berhasil ditambahkan!")

# Menghitung diskon
if total > 200000:
    diskon = 20
else:
    diskon = 0

potongan = total * diskon / 100
total_bayar = total - potongan

# Struk pembayaran
print("\n================================")
print("       STRUK PEMBAYARAN")
print("================================")
print("Total Belanja : Rp", total)
print("Diskon        :", diskon, "%")
print("Potongan      : Rp", potongan)
print("--------------------------------")
print("Total Bayar   : Rp", total_bayar)
print("================================")
print("       TERIMA KASIH!")
print("================================")