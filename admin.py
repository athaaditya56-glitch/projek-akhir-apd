# admin.py
# Modul untuk CRUD user dan melihat penjualan (data berasal dari kasir)

from auth import USERS

# sales_history tidak disimpan di sini, tetapi dipanggil dari kasir.py

def admin_menu():
    while True:
        print("=== MENU ADMIN ===")
        print("1. Lihat daftar user")
        print("2. Tambah user")
        print("3. Hapus user")
        print("4. Lihat riwayat penjualan")
        print("5. Kembali")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            list_user()
        elif pilihan == "2":
            add_user()
        elif pilihan == "3":
            delete_user()
        elif pilihan == "4":
            # view_sales(sales_history)
            print("Sales History belum ada")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.\n")


def list_user():
    print("\n=== DAFTAR USER ===")
    for u, info in USERS.items():
        print(f"{u} - role: {info['role']}")
    print()


def add_user():
    print("\n=== TAMBAH USER ===")
    username = input("Username baru: ").strip()

    if username in USERS:
        print("User sudah ada.\n")
        return

    password = input("Password: ").strip()
    role = input("Role (admin/inventory/kasir): ").strip()

    if role not in ["admin", "inventory", "kasir"]:
        print("Role tidak valid.\n")
        return

    USERS[username] = {"password": password, "role": role}
    print("User berhasil ditambahkan.\n")


def delete_user():
    print("\n=== HAPUS USER ===")
    username = input("Username yang dihapus: ").strip()

    if username not in USERS:
        print("User tidak ditemukan.\n")
        return

    if username == "admin":
        print("User admin utama tidak boleh dihapus.\n")
        return

    del USERS[username]
    print("User berhasil dihapus.\n")


def view_sales(sales_history):
    print("\n=== RIWAYAT PENJUALAN ===")
    if not sales_history:
        print("Belum ada transaksi.\n")
        return

    for s in sales_history:
        print(s)
    print()
