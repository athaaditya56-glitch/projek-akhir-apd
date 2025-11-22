from prettytable import PrettyTable

inventory = [
    {"nama": "Vas Bunga", "harga": 80000, "stok": 50},
    {"nama": "Rak Dinding", "harga": 90000, "stok": 30},
    {"nama": "Meja", "harga": 150000, "stok": 20},
]

def lihat_daftar_barang():
    print("\n=========== DAFTAR BARANG ===========")
    if not inventory:
        print("Belum ada barang di inventory.\n")
        return

    table = PrettyTable()
    table.field_names = ["No", "Nama Barang", "Harga", "Stok"]

    for i, barang in enumerate(inventory, start=1):
        harga_format = f"{barang['harga']:,}"
        table.add_row([i, barang["nama"], harga_format, barang["stok"]])

    print(table)
    print()

def tambah_barang_baru():
    print("\n=== TAMBAH BARANG BARU ===")
    nama = input("Nama barang : ").strip()

    if not nama.replace(" ", "").isalpha():
        print("Input harus berupa huruf.\n")
        return

    try:
        harga = int(input("Harga       : "))
        stok = int(input("Stok        : "))
    except ValueError:
        print("Input harus berupa angka.\n")
        return

    if harga <= 0 or stok < 0:
        print("Harga harus > 0 dan stok >= 0.\n")
        return

    inventory.append({"nama": nama, "harga": harga, "stok": stok})
    print(f"Barang '{nama}' berhasil ditambahkan.\n")

def tambah_stok():
    print("\n=== TAMBAH STOK BARANG ===")
    if not inventory:
        print("Belum ada barang, tidak bisa menambah stok.\n")
        return

    lihat_daftar_barang()

    try:
        nomor = int(input("Pilih nomor barang yang akan ditambah stok: "))
    except ValueError:
        print("Input harus angka.\n")
        return

    if nomor < 1 or nomor > len(inventory):
        print("Nomor barang tidak valid.\n")
        return

    barang = inventory[nomor - 1]

    try:
        tambahan = int(input(f"Tambahkan stok untuk '{barang['nama']}' sebanyak: "))
    except ValueError:
        print("Jumlah stok harus berupa angka.\n")
        return

    if tambahan <= 0:
        print("Jumlah tambahan harus lebih dari 0.\n")
        return

    barang["stok"] += tambahan
    print(f"Stok '{barang['nama']}' sekarang: {barang['stok']}\n")

def menu_inventory():
    while True:
        print("=== MENU INVENTORY ===")
        print("1. lihat daftar barang")
        print("2. tambah barang baru")
        print("3. tambah stok")
        print("4. logout")

        pilihan = input("Masukkan pilihan (1-4): ").strip()

        if pilihan == "1":
            lihat_daftar_barang()
        elif pilihan == "2":
            tambah_barang_baru()
        elif pilihan == "3":
            tambah_stok()
        elif pilihan == "4":
            print("Logout...\n")
            break
        else:
            print("Pilihan tidak valid\n")

def main():
    while True:
        print("=== PILIH ROLE ===")
        role = input("Masukkan role (inventory) atau 'keluar' untuk exit: ").lower().strip()

        if role == "keluar":
            print("Program selesai.")
            break

        if role == "inventory":
            password = input("Masukkan password: ").strip()
            if password == "inv123":
                print("Login berhasil!\n")
                menu_inventory()
            else:
                print("Password salah!\n")
        else:
            print("Pilihan tidak valid\n")

if __name__ == "__main__":
    main()