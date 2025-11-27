import json
import os
from prettytable import PrettyTable

DATA_FILE = "data.json"

barang = []
keranjang = []


# ===============================
# LOAD DATA (sesuai format INVENTORY)
# ===============================
def load_data():
    global barang

    if not os.path.exists(DATA_FILE):
        # jika tidak ada file → buat file inventory kosong
        default_data = {"inventory": {}}
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4, ensure_ascii=False)
        barang = []
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, dict) or "inventory" not in data:
            raise ValueError("FORMAT FILE SALAH")

        # ubah dari bentuk kategori menjadi list tunggal
        barang = []
        for kategori, items in data["inventory"].items():
            for item in items:
                # tambahkan kategori ke item
                item_copy = item.copy()
                item_copy["kategori"] = kategori
                barang.append(item_copy)

    except Exception:
        print("File data.json rusak → dibuat ulang.")
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({"inventory": {}}, f, indent=4, ensure_ascii=False)
        barang = []


# ===============================
# SAVE DATA (kembalikan ke format INVENTORY)
# ===============================
def save_data():
    invent = {}

    for b in barang:
        kategori = b["kategori"]
        if kategori not in invent:
            invent[kategori] = []

        # buang id jika tidak perlu, atau gunakan jika ingin
        item_simpan = {
            "nama": b["nama"],
            "harga": b["harga"],
            "stok": b["stok"]
        }

        invent[kategori].append(item_simpan)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({"inventory": invent}, f, indent=4, ensure_ascii=False)


# ===============================
# TAMPIL DATA
# ===============================
def tampil_barang():
    print("\n DAFTAR BARANG ")
    if barang == []:
        print("Belum ada barang.")
        return

    for i, b in enumerate(barang, start=1):
        print(f"{i}. {b['nama']} ({b['kategori']}) - Rp{b['harga']} | Stok: {b['stok']}")
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
        nomor = int(input("Masukkan nomor barang: "))
        jumlah = int(input("Masukkan jumlah: "))
    except:
        print("Input harus angka.")
        return

    if not (1 <= nomor <= len(barang)):
        print("Nomor tidak valid.")
        return

    barang_ditemukan = barang[nomor - 1]

    if jumlah > barang_ditemukan["stok"]:
        print("Stok tidak cukup.")
        return

    keranjang.append({
        "nama": barang_ditemukan["nama"],
        "harga": barang_ditemukan["harga"],
        "jumlah": jumlah,
        "kategori": barang_ditemukan["kategori"]
    })

    print("Barang berhasil ditambahkan.")


# ===============================
# UBAH JUMLAH
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

    # cari barang asli
    barang_asli = next(
        (b for b in barang if b["nama"] == item["nama"] and b["kategori"] == item["kategori"]),
        None
    )

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

    # cek stok
    for item in keranjang:
        b = next(
            (x for x in barang if x["nama"] == item["nama"] and x["kategori"] == item["kategori"]),
            None
        )
        if b is None:
            print(f"Barang {item['nama']} tidak ditemukan.")
            return
        if item["jumlah"] > b["stok"]:
            print(f"Stok tidak cukup untuk {item['nama']}.")
            return

    # kurangi stok
    for item in keranjang:
        for b in barang:
            if b["nama"] == item["nama"] and b["kategori"] == item["kategori"]:
                b["stok"] -= item["jumlah"]
                break

    save_data()

    # nota
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
# MENU UTAMA (7 MENU)
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


load_data()