from prettytable import PrettyTable

inventory = {
    "Dekorasi": [
        {"nama": "Vas Bunga", "harga": 80000, "stok": 50},
        {"nama": "Lukisan", "harga": 120000, "stok": 15}
    ],
    "Elektronik": [
        {"nama": "Kipas Angin", "harga": 180000, "stok": 10},
        {"nama": "Dispenser", "harga": 90000, "stok": 18}
    ]
}

def input_tidak_kosong(pesan):
    while True:
        data = input(pesan).strip()
        if data == "":
            print("Input tidak boleh kosong.\n")
        else:
            return data

def format_rp(n):
    return f"{n:,}"

def pilih_kategori(maksud="memilih"):
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

def lihat_daftar_barang():
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

def tambah_kategori():
    print("\n=== TAMBAH KATEGORI ===")
    nama = input_tidak_kosong("Nama kategori baru: ")

    if not nama.replace(" ", "").isalpha():
        print("Kategori harus berupa huruf.\n")
        return
    if nama in inventory:
        print("Kategori sudah ada.\n")
        return

    inventory[nama] = []
    print(f"Kategori '{nama}' berhasil ditambahkan.\n")

def hapus_kategori():
    print("\n=== HAPUS KATEGORI ===")
    kategori = pilih_kategori("dihapus")
    if kategori is None:
        print("Batal menghapus kategori.\n")
        return

    daftar = inventory[kategori]

    if daftar:
        confirm = input_tidak_kosong(f"Kategori '{kategori}' berisi barang. Hapus semua? (y/n): ").lower()
        if confirm != "y":
            print("Batal menghapus kategori.\n")
            return
    else:
        confirm = input_tidak_kosong(f"Yakin ingin menghapus kategori '{kategori}'? (y/n): ").lower()
        if confirm != "y":
            print("Batal menghapus kategori.\n")
            return

    del inventory[kategori]
    print(f"Kategori '{kategori}' berhasil dihapus.\n")

def tambah_barang_baru():
    print("\n=== TAMBAH BARANG BARU ===")
    kategori = pilih_kategori("menambah barang ke")
    if kategori is None:
        print("Batal menambah barang.\n")
        return

    nama = input_tidak_kosong("Nama barang: ")
    if not nama.replace(" ", "").isalpha():
        print("Nama barang harus huruf.\n")
        return

    harga_input = input_tidak_kosong("Harga       : ")
    stok_input = input_tidak_kosong("Stok        : ")

    try:
        harga = int(harga_input)
        stok = int(stok_input)
    except ValueError:
        print("Harga & stok harus angka.\n")
        return

    if harga <= 0 or stok < 0:
        print("Harga harus >0 dan stok >=0.\n")
        return

    inventory[kategori].append({"nama": nama, "harga": harga, "stok": stok})
    print(f"Barang '{nama}' berhasil ditambahkan ke kategori '{kategori}'.\n")

def tambah_stok():
    print("\n=== TAMBAH STOK BARANG ===")
    kategori = pilih_kategori("menambah stok")
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

    nomor_input = input_tidak_kosong("Pilih nomor barang: ")
    try:
        nomor = int(nomor_input)
    except ValueError:
        print("Input harus angka.\n")
        return

    if nomor < 1 or nomor > len(daftar):
        print("Nomor tidak valid.\n")
        return

    barang = daftar[nomor - 1]

    tambahan_input = input_tidak_kosong(f"Tambah stok untuk '{barang['nama']}' sebanyak: ")
    try:
        tambahan = int(tambahan_input)
    except ValueError:
        print("Input harus angka.\n")
        return

    if tambahan <= 0:
        print("Harus lebih dari 0.\n")
        return

    barang["stok"] += tambahan
    print(f"Stok baru '{barang['nama']}': {barang['stok']}\n")

def menu_inventory():
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
            lihat_daftar_barang()
        elif pilihan == "2":
            tambah_kategori()
        elif pilihan == "3":
            hapus_kategori()
        elif pilihan == "4":
            tambah_barang_baru()
        elif pilihan == "5":
            tambah_stok()
        elif pilihan == "6":
            print("Logout...\n")
            break
        else:
            print("Pilihan tidak valid.\n")

def main():
    while True:
        print("=== PILIH ROLE ===")
        role = input_tidak_kosong("Masukkan role (inventory) atau 'keluar': ").lower()

        if role == "keluar":
            print("Program selesai.")
            break

        if role == "inventory":
            password = input_tidak_kosong("Masukkan password: ")
            if password == "inv123":
                print("Login berhasil!\n")
                menu_inventory()
            else:
                print("Password salah!\n")
        else:
            print("Role tidak valid.\n")

main()