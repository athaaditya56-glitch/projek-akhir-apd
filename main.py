# main.py
# Integrasi semua modul CLI Sistem Penjualan Furniture

from auth import login
from admin import admin_menu
# from inventory import inventory_menu
# from kasir import kasir_menu, sales_history

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
        # elif role == "inventory":
        #     # inventory_menu()
        # elif role == "kasir":
        #     # kasir_menu()
        # else:
        #     print("Role tidak dikenal.")

        # setelah logout, kembali ke login
        print("\nLogout berhasil.\n")

if __name__ == "__main__":
    main()
