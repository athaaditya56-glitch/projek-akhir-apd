import json
import os
from prettytable import PrettyTable

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

def menu_pembeli():
    data = load_data()
    inventory = data["inventory"]

    while True:
        print("\n=== MENU PEMBELI ===")
        print("1. Lihat barang")
        print("2. Beli barang")
        print("3. Keluar")

        pilihan = input_tidak_kosong("Pilih menu (1-3): ")

        if pilihan == "1":
            print("\n=== DAFTAR BARANG ===")
            for kategori, daftar in inventory.items():
                print(f"\n--- {kategori} ---")
                table = PrettyTable()
                table.field_names = ["No", "Nama", "Harga", "Stok"]
                for i, barang in enumerate(daftar, start=1):
                    table.add_row([i, barang["nama"], format_rp(barang["harga"]), barang["stok"]])
                print(table)

        elif pilihan == "2":
            kategori = input_tidak_kosong("Masukkan kategori: ")
            if kategori not in inventory:
                print("Kategori tidak ditemukan.\n")
                continue

            daftar = inventory[kategori]
            if not daftar:
                print("Kategori kosong.\n")
                continue

            table = PrettyTable()
            table.field_names = ["No", "Nama", "Harga", "Stok"]
            for i, barang in enumerate(daftar, start=1):
                table.add_row([i, barang["nama"], format_rp(barang["harga"]), barang["stok"]])
            print(table)

            try:
                nomor = int(input_tidak_kosong("Pilih nomor barang: "))
                jumlah = int(input_tidak_kosong("Jumlah beli: "))
            except ValueError:
                print("Input harus angka.\n")
                continue

            if nomor < 1 or nomor > len(daftar):
                print("Nomor tidak valid.\n")
                continue
            if jumlah <= 0:
                print("Jumlah harus >0.\n")
                continue

            barang = daftar[nomor - 1]

            if barang["stok"] < jumlah:
                print("Stok tidak mencukupi.\n")
                continue

            barang["stok"] -= jumlah
            save_data(data)

            total = barang["harga"] * jumlah
            print(f"Berhasil membeli {jumlah} {barang['nama']}. Total: Rp{format_rp(total)}\n")

        elif pilihan == "3":
            print("Keluar dari menu pembeli.\n")
            break
        else:
            print("Pilihan tidak valid.\n")