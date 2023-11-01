# Muhammad Arya Fayyadh Razan
# Ammar Nabil Fauzan
# Oktaria Indi Cahyani
# Kami dari kelompok 6 A1 APD yeay!

# Membuat variabel tuple berisi username admin dan passwordnya
data_admin = "haia", "haia"

# Membuat variabel dictionary yang nantinya diisi dengan username sebagai key dan password sebagai value
data_users = {}

def register():
    print("===== REGISTRASI AKUN =====")
    # Input username ke variabel username dan password ke variabel password
    username = str(input("Username : "))
    password = str(input("Password : "))
    # Input username sebagai key dan password sebagai value di dalam variabel dictionary bernama data_users
    data_users[username] = password
    print("Registrasi berhasil.")

def login():
    print("===== LOGIN AKUN =====")
    # Variabel percobaan login
    coba = 0
    max_coba = 3

    # Variabel admin sebelum inputan username dan password disetting False
    admin = False

    # Input username dan password
    # Jika variabel coba kurang dari maks coba login dan variabel admin menjadi True, maka langsung ke bagian menu admin
    # Jika variabel coba kurang dari maks coba login dan variabel admin masih False, maka langsung ke bagian menu user
    # Jika variabel coba lebih dari maks coba login dan variabel admin masih False, maka program akan berhenti
    while coba < max_coba:
        username = input("Username: ")
        password = input("Password: ")

        # Login sebagai admin
        if (username, password) == data_admin:
            print("Selamat datang, Admin!")
            # Variabel admin menjadi True
            admin = True
            return True, admin

        # Login sebagai user
        elif username in data_users and data_users[username] == password:
            print(f"Selamat datang, {username}!")
            # Variabel admin tetap False
            return True, admin

        # Variabel coba ditambah 1
        coba += 1
        sisa_coba = max_coba - coba
        print(f"(!) Username atau password salah. Sisa percobaan : {sisa_coba}")

    print("Anda telah melebihi batas maksimal percobaan login.")
    print("Program dihentikan.")
    exit()

def main():
    while True:
        print(f"\n{'PLAYLIST MUSIK':^40}")
        print("=====[ MENU AKUN ]=====")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            register()
        elif pilihan == "2":
            login()
        elif pilihan == "3":
            exit()
        else:
            print("(!) Pilihan tidak tersedia.")

