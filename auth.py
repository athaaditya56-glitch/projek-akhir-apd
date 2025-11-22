# auth.py
# Modul autentikasi dengan batas percobaan 3 kali

USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "inv": {"password": "inv123", "role": "inventory"},
    "kasir": {"password": "kasir123", "role": "kasir"},
}

def login(max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        user = USERS.get(username)

        if user and user["password"] == password:
            print("Login berhasil!\n")
            return {"username": username, "role": user["role"]}

        attempts += 1
        print(f"Login gagal. Percobaan {attempts}/{max_attempts}.\n")

    print("Batas login tercapai. Aplikasi keluar.")
    return None
