from auth import USERS
from inventory import lihat_daftar_barang
from prettytable import PrettyTable
import inquirer

def admin_menu():
    while True:
        try:
            pilihan = inquirer.list_input(
                "=== MENU ADMIN ===",
                choices=[
                    ("CRUD User", "crud"),
                    ("Lihat stok barang", "stok"),
                    ("Logout", "logout")
                ]
            )
        except Exception:
            print("Terjadi kesalahan input.\n")
            continue

        if pilihan == "crud":
            crud_user()
        elif pilihan == "stok":
            lihat_daftar_barang()
        elif pilihan == "logout":
            break

def crud_user():
    while True:
        try:
            pilihan = inquirer.list_input(
                "=== CRUD USER ===",
                choices=[
                    ("Lihat user", "list"),
                    ("Tambah user", "add"),
                    ("Hapus user", "delete"),
                    ("Kembali", "back")
                ]
            )
        except Exception:
            print("Input tidak valid.\n")
            continue

        if pilihan == "list":
            lihat_user()
        elif pilihan == "add":
            tambah_user()
        elif pilihan == "delete":
            hapus_user()
        elif pilihan == "back":
            break


def lihat_user():
    print("\n=== DAFTAR USER ===")

    if not USERS:
        print("Belum ada user yang terdaftar.\n")
        return

    table = PrettyTable(["Username", "Role"])
    for u, info in USERS.items():
        table.add_row([u, info['role']])

    print(table)
    print()



def tambah_user():
    print("\n=== TAMBAH USER ===")
    try:
        username = input("Username baru: ").strip()

        if username in USERS:
            print("User sudah ada.\n")
            return

        password = input("Password: ").strip()
        role = input("Role (admin/inventory/pembeli): ").strip()
    except Exception:
        print("Input error.\n")
        return

    if role not in ["admin", "inventory", "pembeli"]:
        print("Role tidak valid.\n")
        return

    USERS[username] = {"password": password, "role": role}
    print("User berhasil ditambahkan.\n")


def hapus_user():
    print("\n=== HAPUS USER ===")
    try:
        username = input("User yang ingin dihapus: ").strip()
    except Exception:
        print("Input error.\n")
        return

    if username not in USERS:
        print("User tidak ditemukan.\n")
        return

    if username == "admin":
        print("User admin utama tidak boleh dihapus.\n")
        return

    # Konfirmasi
    try:
        confirm = input(f"Apakah anda yakin ingin menghapus '{username}'? (ya/tidak): ").strip().lower()
    except Exception:
        print("Input error.\n")
        return

    if confirm != "ya":
        print("Penghapusan dibatalkan.\n")
        return

    del USERS[username]
    print("User berhasil dihapus.\n")
