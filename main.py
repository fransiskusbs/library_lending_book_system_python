# ===================================
# [LIBRARY LENDING BOOK SYSTEM]
# ===================================
# Developed by. Fransiskus B S
# JCDS - 34


# /************************************/

# /===== Data Model =====/
# Create your data model here
data = [] # Example data model


# /===== Feature Program =====/
# Create your feature program here
def read():
    """Function for read the data
    """
    return

def create():
    """Function for create the data
    """
    return

def update():
    """Function for update the data
    """
    return

def delete():
    """Function for delete the data
    """
    return

# /===== Main Program =====/
# Create your main program here
def main():
    while True:

        print("\n=========================================")
        print("   SISTEM PEMINJAMAN BUKU PERPUSTAKAAN")
        print("=========================================")
        print("1. Tampilkan Data Peminjaman")
        print("2. Tambah Data Peminjaman")
        print("3. Ubah Data Peminjaman")
        print("4. Hapus Data Peminjaman")
        print("5. Keluar Program")
        print("=========================================")

        input_user = input("Pilih Menu (1-5): ")
        if input_user == "1":
            read()
        elif input_user == "2":
            create()
        elif input_user == "3":
            update()
        elif input_user == "4":
            delete()
        elif input_user == "5":
            print("\nTerima kasih telah menggunakan sistem peminjaman buku !")
            break
        else:
            print("Input yang Anda masukkan tidak valid !")
            print("Silahkan masukkan angka 1-5!")


if __name__ == "__main__":
    main()