from prettytable import PrettyTable

# DATA BARANG
barang = [
    {"id": 1, "nama": "Sofa", "harga": 3000000, "stok": 5, "kategori": "Ruang Tamu"},
    {"id": 2, "nama": "Meja Tamu", "harga": 1500000, "stok": 8, "kategori": "Ruang Tamu"},
    {"id": 3, "nama": "Rak TV", "harga": 2000000, "stok": 6, "kategori": "Ruang Tamu"},
    {"id": 4, "nama": "Ranjang", "harga": 3500000, "stok": 4, "kategori": "Kamar Tidur"},
    {"id": 5, "nama": "Lemari Pakaian", "harga": 2700000, "stok": 5, "kategori": "Kamar Tidur"},
    {"id": 6, "nama": "Meja Rias", "harga": 1800000, "stok": 7, "kategori": "Kamar Tidur"},
    {"id": 7, "nama": "Meja Makan", "harga": 2500000, "stok": 3, "kategori": "Ruang Makan"},
    {"id": 8, "nama": "Kursi Makan", "harga": 400000, "stok": 20, "kategori": "Ruang Makan"},
    {"id": 9, "nama": "Rak Buffet", "harga": 1500000, "stok": 5, "kategori": "Ruang Makan"},
    {"id": 10, "nama": "Kabinet Dapur", "harga": 3000000, "stok": 4, "kategori": "Dapur"},
    {"id": 11, "nama": "Kitchen Island", "harga": 2800000, "stok": 2, "kategori": "Dapur"},
    {"id": 12, "nama": "Rak Piring", "harga": 700000, "stok": 10, "kategori": "Dapur"},
    {"id": 13, "nama": "Meja Kerja", "harga": 1800000, "stok": 6, "kategori": "Ruang Kerja"},
    {"id": 14, "nama": "Kursi Kerja", "harga": 1200000, "stok": 10, "kategori": "Ruang Kerja"},
    {"id": 15, "nama": "Rak Buku", "harga": 900000, "stok": 12, "kategori": "Ruang Kerja"},
    {"id": 16, "nama": "Kursi Taman", "harga": 500000, "stok": 8, "kategori": "Outdoor"},
    {"id": 17, "nama": "Meja Taman", "harga": 700000, "stok": 6, "kategori": "Outdoor"},
    {"id": 18, "nama": "Bangku Panjang", "harga": 900000, "stok": 5, "kategori": "Outdoor"},
    {"id": 19, "nama": "Lampu Meja", "harga": 300000, "stok": 10, "kategori": "Dekorasi"},
    {"id": 20, "nama": "Pigura Foto", "harga": 150000, "stok": 25, "kategori": "Dekorasi"},
    {"id": 21, "nama": "Tanaman Hias", "harga": 250000, "stok": 15, "kategori": "Dekorasi"},
    {"id": 22, "nama": "Rak Dinding", "harga": 400000, "stok": 12, "kategori": "Penyimpanan"},
    {"id": 23, "nama": "Box Organizer", "harga": 100000, "stok": 40, "kategori": "Penyimpanan"},
    {"id": 24, "nama": "Lemari Kabinet", "harga": 2200000, "stok": 5, "kategori": "Penyimpanan"}
]

keranjang = []

# FUNGSI TAMPIL DATA
def tampil_barang():
    print(" DAFTAR BARANG ")
    for b in barang:
        print(f"{b['id']}. {b['nama']} ({b['kategori']}) - Rp{b['harga']} | Stok: {b['stok']}")
    print()

def tampil_keranjang():
    print(" KERANJANG ")
    if keranjang == []:
        print("Keranjang kosong.")
        return
    
    i = 1
    for item in keranjang:
        print(f"{i}. {item['nama']} - Rp{item['harga']} x {item['jumlah']}")
        i += 1
    print()

# FUNGSI KERANJANG
def tambah_barang():
    print(" TAMBAH BARANG KE KERANJANG ")
    tampil_barang()

    try:
        id_barang = int(input("Masukkan no barang: "))
        jumlah = int(input("Masukkan jumlah: "))
    except:
        print("Input harus angka.")
        return

    # Cari barang
    barang_ditemukan = None
    for b in barang:
        if b["id"] == id_barang:
            barang_ditemukan = b
            break
    
    if barang_ditemukan == None:
        print("Barang tidak ditemukan.")
        return

    if jumlah > barang_ditemukan["stok"]:
        print("Stok tidak mencukupi!")
        return

    keranjang.append({
        "id": barang_ditemukan["id"],
        "nama": barang_ditemukan["nama"],
        "harga": barang_ditemukan["harga"],
        "jumlah": jumlah
    })

    print("Barang berhasil ditambahkan.")

def ubah_jumlah():
    print(" UBAH JUMLAH BARANG ")
    tampil_keranjang()

    if keranjang == []:
        return

    try:
        nomor = int(input("Pilih nomor barang: "))
        jumlah_baru = int(input("Jumlah baru: "))
    except:
        print("Input harus angka.")
        return

    if nomor < 1 or nomor > len(keranjang):
        print("Pilihan tidak valid.")
        return

    # Cari barang untuk cek stok
    barang_asli = None
    for b in barang:
        if b["id"] == keranjang[nomor-1]["id"]:
            barang_asli = b
            break

    if jumlah_baru > barang_asli["stok"]:
        print("Stok tidak cukup.")
        return

    keranjang[nomor-1]["jumlah"] = jumlah_baru
    print("Jumlah berhasil diubah.")

def hapus_barang():
    print(" HAPUS BARANG ")
    tampil_keranjang()

    if keranjang == []:
        return

    try:
        nomor = int(input("Pilih nomor yang ingin dihapus: "))
    except:
        print("Input harus angka.")
        return

    if nomor < 1 or nomor > len(keranjang):
        print("Pilihan tidak valid.")
        return

    del keranjang[nomor-1]
    print("Barang dihapus.")

# CHECKOUT
def checkout():
    print(" CHECKOUT ")

    if keranjang == []:
        print("Keranjang masih kosong.")
        return

    # Kurangi stok barang
    for item in keranjang:
        for b in barang:
            if b["id"] == item["id"]:
                b["stok"] -= item["jumlah"]
                break

    # Cetak nota
    print(" NOTA PEMBELIAN ")
    table = PrettyTable()
    table.field_names = ["No", "Nama Barang", "Harga", "Jumlah", "Subtotal"]

    total = 0
    i = 1

    for item in keranjang:
        subtotal = item["harga"] * item["jumlah"]
        total += subtotal
        table.add_row([i, item["nama"], f"Rp{item['harga']}", item["jumlah"], f"Rp{subtotal}"])
        i += 1

    print(table)
    print(f"TOTAL BAYAR : Rp{total}")
    print("Checkout selesai. Terima kasih!")

    keranjang.clear()

# MENU UTAMA
def menu_pembeli():
    while True:
        print(" MENU UTAMA ")
        print("1. Lihat barang")
        print("2. Tambah barang ke keranjang")
        print("3. Lihat keranjang")
        print("4. Ubah jumlah barang")
        print("5. Hapus barang dari keranjang")
        print("6. Checkout")
        print("7. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            tampil_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            tampil_keranjang()
        elif pilihan == "4":
            ubah_jumlah()
        elif pilihan == "5":
            hapus_barang()
        elif pilihan == "6":
            checkout()
        elif pilihan == "7":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")
