from prettytable import PrettyTable

# DATA BARANG


barang = [
    # A. Ruang Tamu
    {"id": 1, "nama": "Sofa", "harga": 3000000, "stok": 5, "kategori": "Ruang Tamu"},
    {"id": 2, "nama": "Meja Tamu", "harga": 1500000, "stok": 8, "kategori": "Ruang Tamu"},
    {"id": 3, "nama": "Rak TV", "harga": 2000000, "stok": 6, "kategori": "Ruang Tamu"},

    # B. Kamar Tidur
    {"id": 4, "nama": "Ranjang", "harga": 3500000, "stok": 4, "kategori": "Kamar Tidur"},
    {"id": 5, "nama": "Lemari Pakaian", "harga": 2700000, "stok": 5, "kategori": "Kamar Tidur"},
    {"id": 6, "nama": "Meja Rias", "harga": 1800000, "stok": 7, "kategori": "Kamar Tidur"},

    # C. Ruang Makan
    {"id": 7, "nama": "Meja Makan", "harga": 2500000, "stok": 3, "kategori": "Ruang Makan"},
    {"id": 8, "nama": "Kursi Makan", "harga": 400000, "stok": 20, "kategori": "Ruang Makan"},
    {"id": 9, "nama": "Rak Buffet", "harga": 1500000, "stok": 5, "kategori": "Ruang Makan"},

    # D. Dapur
    {"id": 10, "nama": "Kabinet Dapur", "harga": 3000000, "stok": 4, "kategori": "Dapur"},
    {"id": 11, "nama": "Kitchen Island", "harga": 2800000, "stok": 2, "kategori": "Dapur"},
    {"id": 12, "nama": "Rak Piring", "harga": 700000, "stok": 10, "kategori": "Dapur"},

    # E. Ruang Kerja
    {"id": 13, "nama": "Meja Kerja", "harga": 1800000, "stok": 6, "kategori": "Ruang Kerja"},
    {"id": 14, "nama": "Kursi Kerja", "harga": 1200000, "stok": 10, "kategori": "Ruang Kerja"},
    {"id": 15, "nama": "Rak Buku", "harga": 900000, "stok": 12, "kategori": "Ruang Kerja"},

    # F. Outdoor / Taman
    {"id": 16, "nama": "Kursi Taman", "harga": 500000, "stok": 8, "kategori": "Outdoor"},
    {"id": 17, "nama": "Meja Taman", "harga": 700000, "stok": 6, "kategori": "Outdoor"},
    {"id": 18, "nama": "Bangku Panjang", "harga": 900000, "stok": 5, "kategori": "Outdoor"},

    # G. Dekorasi
    {"id": 19, "nama": "Lampu Meja", "harga": 300000, "stok": 10, "kategori": "Dekorasi"},
    {"id": 20, "nama": "Pigura Foto", "harga": 150000, "stok": 25, "kategori": "Dekorasi"},
    {"id": 21, "nama": "Tanaman Hias", "harga": 250000, "stok": 15, "kategori": "Dekorasi"},

    # H. Penyimpanan
    {"id": 22, "nama": "Rak Dinding", "harga": 400000, "stok": 12, "kategori": "Penyimpanan"},
    {"id": 23, "nama": "Box Organizer", "harga": 100000, "stok": 40, "kategori": "Penyimpanan"},
    {"id": 24, "nama": "Lemari Kabinet", "harga": 2200000, "stok": 5, "kategori": "Penyimpanan"}
]

keranjang = []


# FUNGSI TAMPIL DATA BARANG

def lihat_barang_tersedia():
    print(" DAFTAR BARANG ")
    for b in barang:
        print(f"{b['id']}. {b['nama']} ({b['kategori']}) - Rp{b['harga']} | Stok: {b['stok']}")
    print()


def lihat_keranjang():
    print(" KERANJANG ")
    if not keranjang:
        print("Keranjang kosong.")
        return

    i = 1
    for item in keranjang:
        print(f"{i}. {item['nama']} - Rp{item['harga']} x {item['jumlah']}")
        i += 1
    print()


# FUNGSI KERANJANG

def tambah():
    print(" TAMBAH BARANG KE KERANJANG ")
    lihat_barang_tersedia()

    try:
        id_barang = int(input("Masukkan no barang: "))
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Input harus angka.")
        return

    found = next((b for b in barang if b["id"] == id_barang), None)

    if not found:
        print("Barang tidak ditemukan.")
        return

    if jumlah > found["stok"]:
        print("Stok tidak mencukupi!")
        return

    keranjang.append({
        "id": found["id"],
        "nama": found["nama"],
        "harga": found["harga"],
        "jumlah": jumlah
    })

    print("Barang berhasil ditambahkan.")


def ubah():
    print(" UBAH DATA DI KERANJANG ")
    lihat_keranjang()

    if not keranjang:
        return

    try:
        idx = int(input("Pilih nomor barang: ")) - 1
        jumlah_baru = int(input("Jumlah baru: "))
    except ValueError:
        print("Input harus angka.")
        return

    if idx < 0 or idx >= len(keranjang):
        print("Pilihan tidak valid.")
        return

    barang_asli = next(b for b in barang if b["id"] == keranjang[idx]["id"])

    if jumlah_baru > barang_asli["stok"]:
        print("Stok tidak cukup.")
        return

    keranjang[idx]["jumlah"] = jumlah_baru
    print("Jumlah berhasil diubah.")


def hapus():
    print(" HAPUS BARANG ")
    lihat_keranjang()

    if not keranjang:
        return

    try:
        idx = int(input("Pilih nomor yang ingin dihapus: ")) - 1
    except ValueError:
        print("Input harus angka.")
        return

    if idx < 0 or idx >= len(keranjang):
        print("Pilihan tidak valid.")
        return

    keranjang.pop(idx)
    print("Barang dihapus.")


# CETAK NOTA + CHECKOUT

def cetak_nota():
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


def checkout():
    print(" CHECKOUT ")

    if not keranjang:
        print("Keranjang masih kosong.")
        return

    # Kurangi stok
    for item in keranjang:
        barang_asli = next(b for b in barang if b["id"] == item["id"])
        barang_asli["stok"] -= item["jumlah"]

    cetak_nota()
    print("Checkout selesai. Terima kasih!")

    keranjang.clear()


# MENU UTAMA

def menu_keranjang():
    while True:
        print(" MENU KERANJANG ")
        print("1. Tambah barang")
        print("2. Ubah jumlah barang")
        print("3. Hapus barang")
        print("4. Kembali")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            ubah()
        elif pilihan == "3":
            hapus()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")


def menu_pembeli():
    while True:
        print(" MENU PEMBELI ")
        print("1. Lihat barang")
        print("2. Keranjang")
        print("3. Checkout")
        print("4. Keluar")

        p = input("Pilih: ")

        if p == "1":
            lihat_barang_tersedia()
        elif p == "2":
            menu_keranjang()
        elif p == "3":
            checkout()
        elif p == "4":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")
