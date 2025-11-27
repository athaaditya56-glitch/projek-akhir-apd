from auth import login
from admin import admin_menu
from inventory import menu_inventory
from pembeli import menu_pembeli

def main():
    print("=== SISTEM PENJUALAN TOKO FURNITURE ===\n")

    while True:
        print("Menu Utama")
        print("1. Login")
        print("2. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "2":
            print("Program selesai.")
            break

        elif pilihan == "1":
            user = login()

            if not user:
                print("Sisa percobaan habis. Login gagal.\n")
                continue

            role = user["role"]

            if role == "admin":
                admin_menu()
            elif role == "inventory":
                menu_inventory()
            elif role == "pembeli":
                menu_pembeli()
            else:
                print("Ada yang error.\n")

            print("Logout berhasil.\n")

        else:
            print("Pilihan tidak valid.\n")


if __name__ == "__main__":
    main()
