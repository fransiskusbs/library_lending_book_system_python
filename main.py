# ===================================
# [LIBRARY LENDING BOOK SYSTEM]
# ===================================
# Developed by. Fransiskus B S
# JCDS - 34


# /************************************/

# /===== Data Model =====/
# Create your data model here
data_peminjaman = [
    {
        "id": 1,
        "nama_peminjam": "Andi",
        "judul_buku": "Laskar Pelangi",
        "tanggal_pinjam": "07-09-2026",
        "tanggal_kembali": "14-09-2026",
        "status": "Dipinjam"
    },
    {
        "id": 2,
        "nama_peminjam": "Budi",
        "judul_buku": "Bumi Manusia",
        "tanggal_pinjam": "05-09-2026",
        "tanggal_kembali": "12-09-2026",
        "status": "Dipinjam"
    },
    {
        "id": 3,
        "nama_peminjam": "Dewi",
        "judul_buku": "Negeri 5 Menara",
        "tanggal_pinjam": "01-09-2026",
        "tanggal_kembali": "08-09-2026",
        "status": "Dikembalikan"
    },
    {
        "id": 4,
        "nama_peminjam": "Sinta",
        "judul_buku": " ",
        "tanggal_pinjam": " ",
        "tanggal_kembali": " ",
        "status": " "
    },
    {
        "id": 5,
        "nama_peminjam": "Carol",
        "judul_buku": " ",
        "tanggal_pinjam": " ",
        "tanggal_kembali": " ",
        "status": " "
    }
]


# /===== Feature Program =====/
# Create your feature program here
def read():
    print("\n==========================================")
    print("        DATA PEMINJAMAN BUKU")
    print("==========================================")

    if len(data_peminjaman) == 0:
        print("Belum ada data peminjaman buku.")
        return

    print("-" * 100)
    print(
        f"{'ID':<5}"
        f"{'Nama Peminjam':<20}"
        f"{'Judul Buku':<25}"
        f"{'Tgl Pinjam':<15}"
        f"{'Tgl Kembali':<15}"
        f"{'Status':<15}"
    )
    print("-" * 100)

    for data in data_peminjaman:
        print(
            f"{data['id']:<5}"
            f"{data['nama_peminjam']:<20}"
            f"{data['judul_buku']:<25}"
            f"{data['tanggal_pinjam']:<15}"
            f"{data['tanggal_kembali']:<15}"
            f"{data['status']:<15}"
        )

    print("-" * 100)
    return

def create():
    print("\n==========================================")
    print("          TAMBAH PEMINJAMAN")
    print("==========================================")

    nama_peminjam = input("Nama peminjam     : ")
    judul_buku = input("Judul buku        : ")
    tanggal_pinjam = input("Tanggal pinjam    : ")
    tanggal_kembali = input("Tanggal kembali   : ")

    # Membuat ID otomatis
    if len(data_peminjaman) == 0:
        id_baru = 1
    else:
        id_baru = data_peminjaman[-1]["id"] + 1

    data_baru = {
        "id": id_baru,
        "nama_peminjam": nama_peminjam,
        "judul_buku": judul_buku,
        "tanggal_pinjam": tanggal_pinjam,
        "tanggal_kembali": tanggal_kembali,
        "status": "Dipinjam"
    }

    data_peminjaman.append(data_baru)

    print("\nData peminjaman berhasil ditambahkan.")
    print(f"ID Peminjaman : {id_baru}")
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
            print("Input yang Anda masukkantidak valid !")
            print("Silahkan masukkan angka 1-5!")


if __name__ == "__main__":
    main()