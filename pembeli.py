import json
import os
from prettytable import PrettyTable

DATA_FILE = "data.json"

barang = []
keranjang = []


# ===============================
# LOAD DATA
# ===============================
def load_data():
    global barang

    # Jika file belum ada → buat file baru dengan format benar
    if not os.path.exists(DATA_FILE):
        default_data = {
            "barang": [
                {"id": 1, "nama": "Sofa", "harga": 3000000, "stok": 5, "kategori": "Ruang Tamu"},
                {"id": 2, "nama": "Meja Tamu", "harga": 1500000, "stok": 4, "kategori": "Ruang Tamu"},
                {"id": 3, "nama": "Lemari", "harga": 2000000, "stok": 3, "kategori": "Kamar Tidur"},
            ]
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4, ensure_ascii=False)
        
        barang = default_data["barang"].copy()
        return

    # Jika file ada → baca isinya
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Validasi format
        if isinstance(data, dict) and "barang" in data and isinstance(data["barang"], list):
            barang = data["barang"].copy()
        else:
            raise ValueError("FORMAT DATA SALAH")

    except Exception:
        # Jika file rusak → reset default minimal
        default_data = {"barang": []}
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4, ensure_ascii=False)
        barang = []
        print("File data.json rusak → dibuat ulang.")


# ===============================
# SAVE DATA
# ===============================
def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({"barang": barang}, f, indent=4, ensure_ascii=False)


# ===============================
# TAMPIL DATA
# ===============================
def tampil_barang():
    print("\n DAFTAR BARANG ")
    if barang == []:
        print("Belum ada barang.")
        return

    for b in barang:
        print(f"{b['id']}. {b['nama']} ({b['kategori']}) - Rp{b['harga']} | Stok: {b['stok']}")
    print()


def tampil_keranjang():
    print("\n KERANJANG ")
    if keranjang == []:
        print("Keranjang kosong.")
        return

    for i, item in enumerate(keranjang, start=1):
        print(f"{i}. {item['nama']} - Rp{item['harga']} x {item['jumlah']}")
    print()


# ===============================
# TAMBAH BARANG KE KERANJANG
# ===============================
def tambah_barang():
    print("\n TAMBAH BARANG KE KERANJANG ")
    tampil_barang()

    try:
        id_barang = int(input("Masukkan no barang: "))
        jumlah = int(input("Masukkan jumlah: "))
    except:
        print("Input harus angka.")
        return

    # Cari barang
    barang_ditemukan = next((b for b in barang if b["id"] == id_barang), None)

    if barang_ditemukan is None:
        print("Barang tidak ditemukan.")
        return

    if jumlah > barang_ditemukan["stok"]:
        print("Stok tidak cukup.")
        return

    keranjang.append({
        "id": barang_ditemukan["id"],
        "nama": barang_ditemukan["nama"],
        "harga": barang_ditemukan["harga"],
        "jumlah": jumlah
    })

    print("Barang berhasil ditambahkan.")


# ===============================
# UBAH JUMLAH BARANG
# ===============================
def ubah_jumlah():
    print("\n UBAH JUMLAH BARANG ")
    tampil_keranjang()

    if keranjang == []:
        return

    try:
        nomor = int(input("Pilih nomor barang: "))
        jumlah_baru = int(input("Jumlah baru: "))
    except:
        print("Input harus angka.")
        return

    if not (1 <= nomor <= len(keranjang)):
        print("Nomor tidak valid.")
        return

    item = keranjang[nomor - 1]

    barang_asli = next((b for b in barang if b["id"] == item["id"]), None)

    if barang_asli is None:
        print("Barang asli tidak ditemukan.")
        return

    if jumlah_baru > barang_asli["stok"]:
        print("Stok tidak mencukupi.")
        return

    keranjang[nomor - 1]["jumlah"] = jumlah_baru
    print("Jumlah berhasil diubah.")


# ===============================
# HAPUS BARANG
# ===============================
def hapus_barang():
    print("\n HAPUS BARANG ")
    tampil_keranjang()

    if keranjang == []:
        return

    try:
        nomor = int(input("Pilih nomor yang ingin dihapus: "))
    except:
        print("Input harus angka.")
        return

    if not (1 <= nomor <= len(keranjang)):
        print("Nomor tidak valid.")
        return

    del keranjang[nomor - 1]
    print("Barang dihapus.")


# ===============================
# CHECKOUT
# ===============================
def checkout():
    print("\n CHECKOUT ")

    if keranjang == []:
        print("Keranjang kosong.")
        return

    # Cek stok dulu
    for item in keranjang:
        b = next((x for x in barang if x["id"] == item["id"]), None)
        if b is None:
            print(f"Barang {item['nama']} tidak ditemukan.")
            return
        if item["jumlah"] > b["stok"]:
            print(f"Stok tidak cukup untuk {item['nama']}.")
            return

    # Kurangi stok
    for item in keranjang:
        for b in barang:
            if b["id"] == item["id"]:
                b["stok"] -= item["jumlah"]
                break

    save_data()

    # Tampilkan nota
    print("\n NOTA PEMBELIAN ")
    table = PrettyTable()
    table.field_names = ["No", "Nama", "Harga", "Jumlah", "Subtotal"]

    total = 0
    for i, item in enumerate(keranjang, start=1):
        subtotal = item["harga"] * item["jumlah"]
        total += subtotal
        table.add_row([i, item["nama"], f"Rp{item['harga']}", item["jumlah"], f"Rp{subtotal}"])

    print(table)
    print(f"TOTAL : Rp{total}")
    print("Terima kasih sudah membeli!")

    keranjang.clear()


# ===============================
# MENU UTAMA
# ===============================
def menu_pembeli():
    while True:
        print("\n MENU UTAMA ")
        print("1. Lihat barang")
        print("2. Tambah barang ke keranjang")
        print("3. Lihat keranjang")
        print("4. Ubah jumlah barang")
        print("5. Hapus barang")
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


# Load data saat import
load_data()
