# main.py
# Integrasi semua modul CLI Sistem Penjualan Furniture

from auth import login
from admin import admin_menu
from inventory import menu_inventory
from pembeli import menu_pembeli

def main():
    print("=== SISTEM PENJUALAN TOKO FURNITURE ===\n")

    while True:
        user = login()
        if not user:
            print("Gagal login 3 kali. Program ditutup.")
            break

        role = user["role"]

        if role == "admin":
            admin_menu()
        elif role == "inventory":
            menu_inventory()
        elif role == "pembeli":
            menu_pembeli()
        else:
            print("Role tidak dikenal.")
        # setelah logout, kembali ke login
        print("\nLogout berhasil.\n")

if __name__ == "__main__":
    main()
