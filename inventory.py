import json
from prettytable import PrettyTable
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"inventory": {}}

    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def input_tidak_kosong(pesan):
    while True:
        data = input(pesan).strip()
        if data == "":
            print("Input tidak boleh kosong.\n")
        else:
            return data

def format_rp(n):
    return f"{n:,}"

def pilih_kategori(inventory, maksud="memilih"):
    if not inventory:
        print("Belum ada kategori.\n")
        return None

    print("\nDaftar kategori:")
    kategori_list = list(inventory.keys())
    for i, k in enumerate(kategori_list, start=1):
        print(f"{i}. {k}")

    nomor_input = input_tidak_kosong(f"Pilih nomor kategori untuk {maksud} (0 = batal): ")
    try:
        nomor = int(nomor_input)
    except ValueError:
        print("Input harus angka.\n")
        return None

    if nomor == 0:
        return None
    if nomor < 1 or nomor > len(kategori_list):
        print("Nomor kategori tidak valid.\n")
        return None

    return kategori_list[nomor - 1]

def lihat_daftar_barang(data):
    inventory = data["inventory"]

    print("\n==== DAFTAR BARANG (PER KATEGORI) ====")
    if not inventory:
        print("Belum ada kategori.\n")
        return

    for kategori, daftar in inventory.items():
        print(f"\n------------- {kategori} -------------")
        if not daftar:
            print("(Belum ada barang di kategori ini)")
            continue

        table = PrettyTable()
        table.field_names = ["No", "Nama Barang", "Harga", "Stok"]
        for i, barang in enumerate(daftar, start=1):
            table.add_row([i, barang["nama"], format_rp(barang["harga"]), barang["stok"]])
        print(table)
    print()

def tambah_kategori(data):
    inventory = data["inventory"]

    print("\n=== TAMBAH KATEGORI ===")
    nama = input_tidak_kosong("Nama kategori baru: ")

    if not nama.replace(" ", "").isalpha():
        print("Kategori harus berupa huruf.\n")
        return
    if nama in inventory:
        print("Kategori sudah ada.\n")
        return

    inventory[nama] = []
    save_data(data)
    print(f"Kategori '{nama}' berhasil ditambahkan.\n")

def hapus_kategori(data):
    inventory = data["inventory"]

    print("\n=== HAPUS KATEGORI ===")
    kategori = pilih_kategori(inventory, "dihapus")
    if kategori is None:
        print("Batal menghapus kategori.\n")
        return

    if inventory[kategori]:
        confirm = input_tidak_kosong(f"Kategori '{kategori}' berisi barang. Hapus semua? (ya/tidak): ").lower()
    else:
        confirm = input_tidak_kosong(f"Yakin ingin menghapus kategori '{kategori}'? (ya/tidak): ").lower()

    if confirm != "ya":
        print("Batal menghapus kategori.\n")
        return

    del inventory[kategori]
    save_data(data)
    print(f"Kategori '{kategori}' berhasil dihapus.\n")

def tambah_barang_baru(data):
    inventory = data["inventory"]

    print("\n=== TAMBAH BARANG BARU ===")
    kategori = pilih_kategori(inventory, "menambah barang ke")
    if kategori is None:
        print("Batal menambah barang.\n")
        return

    nama = input_tidak_kosong("Nama barang: ")
    if not nama.replace(" ", "").isalpha():
        print("Nama barang harus huruf.\n")
        return

    try:
        harga = int(input_tidak_kosong("Harga: "))
        stok = int(input_tidak_kosong("Stok: "))
    except ValueError:
        print("Harga & stok harus angka.\n")
        return

    if harga <= 0 or stok < 0:
        print("Harga harus >0 dan stok ≥ 0.\n")
        return

    inventory[kategori].append({"nama": nama, "harga": harga, "stok": stok})
    save_data(data)
    print(f"Barang '{nama}' berhasil ditambahkan ke kategori '{kategori}'.\n")

def tambah_stok(data):
    inventory = data["inventory"]

    print("\n=== TAMBAH STOK BARANG ===")
    kategori = pilih_kategori(inventory, "menambah stok")
    if kategori is None:
        print("Batal.\n")
        return

    daftar = inventory[kategori]
    if not daftar:
        print("Tidak ada barang di kategori ini.\n")
        return

    table = PrettyTable()
    table.field_names = ["No", "Nama Barang", "Harga", "Stok"]
    for i, barang in enumerate(daftar, start=1):
        table.add_row([i, barang["nama"], format_rp(barang["harga"]), barang["stok"]])
    print(table)

    try:
        nomor = int(input_tidak_kosong("Pilih nomor barang: "))
    except ValueError:
        print("Input harus angka.\n")
        return

    if nomor < 1 or nomor > len(daftar):
        print("Nomor tidak valid.\n")
        return

    barang = daftar[nomor - 1]

    try:
        tambahan = int(input_tidak_kosong("Tambah stok sebanyak: "))
    except ValueError:
        print("Input harus angka.\n")
        return

    if tambahan <= 0:
        print("Harus lebih dari 0.\n")
        return

    barang["stok"] += tambahan
    save_data(data)
    print(f"Stok baru '{barang['nama']}': {barang['stok']}\n")

def menu_inventory():
    data = load_data()

    while True:
        print("=== MENU INVENTORY ===")
        print("1. Lihat daftar barang")
        print("2. Tambah kategori")
        print("3. Hapus kategori")
        print("4. Tambah barang baru")
        print("5. Tambah stok")
        print("6. Logout")

        pilihan = input_tidak_kosong("Masukkan pilihan (1-6): ")

        if pilihan == "1":
            lihat_daftar_barang(data)
        elif pilihan == "2":
            tambah_kategori(data)
        elif pilihan == "3":
            hapus_kategori(data)
        elif pilihan == "4":
            tambah_barang_baru(data)
        elif pilihan == "5":
            tambah_stok(data)
        elif pilihan == "6":
            print("Logout...\n")
            break
        else:
            print("Pilihan tidak valid.\n")