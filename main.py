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
        "tanggal_kembali": "21-09-2026",
        "status": "Dipinjam"
    },
    {
        "id": 2,
        "nama_peminjam": "Budi",
        "judul_buku": "Learn English Practically",
        "tanggal_pinjam": "05-09-2026",
        "tanggal_kembali": "20-09-2026",
        "status": "Dipinjam"
    },
    {
        "id": 3,
        "nama_peminjam": "Dewi",
        "judul_buku": "Malin kundang",
        "tanggal_pinjam": "01-09-2026",
        "tanggal_kembali": "08-09-2026",
        "status": "Dikembalikan"
    },
    {
        "id": 4,
        "nama_peminjam": "Sinta",
        "judul_buku": "Biografi Pahlawan Nasional: Sutan Syahrir",
        "tanggal_pinjam": "09-09-2026",
        "tanggal_kembali": "21-09-2026",
        "status": "Dipinjam"
    },
    {
        "id": 5,
        "nama_peminjam": "Carol",
        "judul_buku": "Peristiwa Rengasdengklok",
        "tanggal_pinjam": "20-08-2026",
        "tanggal_kembali": "07-09-2026",
        "status": "Dikembalikan"
    }
]

# ==========================================
# READ
# ==========================================
def read():
    while True:
        print("\n==========================================")
        print("        DATA PEMINJAMAN BUKU")
        print("==========================================")
        print("1. Tampilkan Semua Data")
        print("2. Cari Data")
        print("3. Kembali")

        input_read = input("Masukkan pilihan menu: ")

        if input_read == "1":
            if len(data_peminjaman) == 0:
                print("Data peminjaman masih kosong.")
            else:
                print("-" * 126)
                print(
                    f"{'ID':<5}|"
                    f"{'Nama Peminjam':<20}|"
                    f"{'Judul Buku':<50}|"
                    f"{'Tgl Pinjam':<15}|"
                    f"{'Tgl Kembali':<15}|"
                    f"{'Status':<15}|"
                    )
                print("-" * 126)
                
                for data in data_peminjaman:
                    print(
                        f"{data['id']:<5}|"
                        f"{data['nama_peminjam'].title():<20}|"
                        f"{data['judul_buku'].title():<50}|"
                        f"{data['tanggal_pinjam']:<15}|"
                        f"{data['tanggal_kembali']:<15}|"
                        f"{data['status'].title():<15}|"
                        )
                print("-" * 126)

        elif input_read == "2":
            search()

        elif input_read == "3":
            break

        else:
            print("Input yang Anda masukkan tidak valid !")
            print("Masukkan angka 1-3 !")

# ==========================================
# SEARCH
# ==========================================
def search():
    keyword = input("Masukkan kata kunci : ").lower()

    found = False

    print("-"*126)
    print(
        f"{'ID':<5}|"
        f"{'Nama Peminjam':<20}|"
        f"{'Judul Buku':<50}|"
        f"{'Tgl Pinjam':<15}|"
        f"{'Tgl Kembali':<15}|"
        f"{'Status':<15}|"
        )
    print("-" * 126)
    for data in data_peminjaman:
        if (keyword in data["nama_peminjam"].lower()
                or keyword in data["judul_buku"].lower()
                or keyword in data["status"].lower()):
            found = True
            print(
                f"{data['id']:<5}|"
                f"{data['nama_peminjam'].title():<20}|"
                f"{data['judul_buku'].title():<50}|"
                f"{data['tanggal_pinjam']:<15}|"
                f"{data['tanggal_kembali']:<15}|"
                f"{data['status'].title():<15}|"
                )
            print("-" * 126)

    if found == False:
        print("Data tidak ditemukan")

# ==========================================
# CREATE
# ==========================================
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

    while True:
        konfirmasi = input("Anda yakin untuk menyimpan data ini? (y/n) : ").lower()

        if konfirmasi == "y":
            data_baru = {
                    "id": id_baru,
                    "nama_peminjam": nama_peminjam,
                    "judul_buku": judul_buku,
                    "tanggal_pinjam": tanggal_pinjam,
                    "tanggal_kembali": tanggal_kembali,
                    "status": "Dipinjam"}
            data_peminjaman.append(data_baru)
            print("\nData peminjaman berhasil ditambahkan.")
            print(f"ID Peminjaman : {id_baru}")
            return
        elif konfirmasi == "n":
            print("Data batal ditambahkan !")
            break
        else:
            print("Input yang Anda masukkan tidak valid (y atau n)!")

# ==========================================
# UPDATE
# ==========================================
def update():
    print("\n==========================================")
    print("        UBAH DATA PEMINJAMAN")
    print("==========================================")

    if len(data_peminjaman) == 0:
        print("Belum ada data peminjaman.")
        return

    try:
        input_update = int(input("Masukkan ID peminjaman : "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    data_ditemukan = None

    for data in data_peminjaman:
        if data["id"] == input_update:
            data_ditemukan = data
            break

    if data_ditemukan is None:
        print("Data dengan ID tersebut tidak ditemukan.")
        return

    print("\nData saat ini:")
    print(f"Nama Peminjam   : {data_ditemukan['nama_peminjam']}")
    print(f"Judul Buku      : {data_ditemukan['judul_buku']}")
    print(f"Tanggal Pinjam  : {data_ditemukan['tanggal_pinjam']}")
    print(f"Tanggal Kembali : {data_ditemukan['tanggal_kembali']}")
    print(f"Status          : {data_ditemukan['status']}")

    print("\nMasukkan data baru:")

    nama_baru = input("Nama peminjam baru   : ")
    judul_baru = input("Judul buku baru      : ")
    tanggal_pinjam_baru = input("Tanggal pinjam baru  : ")
    tanggal_kembali_baru = input("Tanggal kembali baru : ")

    print("\nStatus:")
    print("1. Dipinjam")
    print("2. Dikembalikan")

    pilihan_status = input("Pilih status (1/2) : ")

    if pilihan_status == "1":
        status_baru = "Dipinjam"
    elif pilihan_status == "2":
        status_baru = "Dikembalikan"
    else:
        print("Pilihan status tidak valid.")
        return

    while True:
        konfirmasi = input(
            "\nApakah kamu yakin ingin mengubah data ini? (y/n) : ").lower()

        if konfirmasi == "y":
            data_ditemukan["nama_peminjam"] = nama_baru
            data_ditemukan["judul_buku"] = judul_baru
            data_ditemukan["tanggal_pinjam"] = tanggal_pinjam_baru
            data_ditemukan["tanggal_kembali"] = tanggal_kembali_baru
            data_ditemukan["status"] = status_baru

            print("Data berhasil diubah.")
            break
        elif konfirmasi == "n":
            print("Data batal diubah !")
            break
        else:
            print("Input yang Anda masukkan tidak valid (y atau n)!")

# ==========================================
# DELETE
# ==========================================
def delete():
    print("\n==========================================")
    print("         HAPUS DATA PEMINJAMAN")
    print("==========================================")

    if len(data_peminjaman) == 0:
        print("Belum ada data peminjaman.")
        return

    try:
        id_cari = int(input("Masukkan ID peminjaman : "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    data_ditemukan = None

    for data in data_peminjaman:
        if data["id"] == id_cari:
            data_ditemukan = data
            break

    if data_ditemukan is None:
        print("Data dengan ID tersebut tidak ditemukan.")
        return

    print("\nData yang akan dihapus:")
    print(f"ID              : {data_ditemukan['id']}")
    print(f"Nama Peminjam   : {data_ditemukan['nama_peminjam']}")
    print(f"Judul Buku      : {data_ditemukan['judul_buku']}")
    print(f"Tanggal Pinjam  : {data_ditemukan['tanggal_pinjam']}")
    print(f"Tanggal Kembali : {data_ditemukan['tanggal_kembali']}")
    print(f"Status          : {data_ditemukan['status']}")

    while True:
        konfirmasi = input(
            "\nApakah kamu yakin ingin menghapus data ini? (y/n) : ").lower()

        if konfirmasi == "y":
            data_peminjaman.remove(data_ditemukan)
            print("Data berhasil dihapus.")
            break
        elif konfirmasi == "n":
            print("Data batal dihapus !")
            break
        else:
            print("Input yang Anda masukkan tidak valid (y atau n)!")

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