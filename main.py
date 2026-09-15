# ===================================
# [SISTEM PEMINJAMAN BUKU PERPUSTAKAAN]
# ===================================
# Developed by. Fransiskus B S
# JCDS - 34


# /************************************/

from datetime import date, timedelta, datetime

# /===== Data Model =====/
# Create your data model here
data_buku = [
    {"id_buku" : 1, "judul_buku" : "Laskar Pelangi", "stock" : 2},
    {"id_buku" : 2, "judul_buku" : "Learn English Practically", "stock" : 1},
    {"id_buku" : 3, "judul_buku" : "Malin Kundang", "stock" : 1},
    {"id_buku" : 4, "judul_buku" : "Biografi Pahlawan Nasional: Sutan Syahrir", "stock" : 3},
    {"id_buku" : 5, "judul_buku" : "Peristiwa Rengasdengklok", "stock" : 2},
    {"id_buku" : 6, "judul_buku" : "Kamus Besar Bahasa Indonesia", "stock" : 1},
    {"id_buku" : 7, "judul_buku" : "Kamus Inggris-Indonesia", "stock" : 1},
    {"id_buku" : 8, "judul_buku" : "Kamus Indonesia-Inggris", "stock" : 2},
    {"id_buku" : 9, "judul_buku" : "R.A Kartini", "stock" : 2},
    {"id_buku" : 10, "judul_buku" : "Atlas Indonesia dan Dunia", "stock" : 1},
    ]

data_peminjaman = [
    {
        "id_peminjaman": 1,
        "nama_peminjam": "Andi",
        "judul_buku": "Laskar Pelangi",
        "tanggal_pinjam": "07-09-2026",
        "tanggal_kembali": "21-09-2026",
        "status": "Dipinjam"
    },
    {
        "id_peminjaman": 2,
        "nama_peminjam": "Budi",
        "judul_buku": "Learn English Practically",
        "tanggal_pinjam": "05-09-2026",
        "tanggal_kembali": "20-09-2026",
        "status": "Dipinjam"
    },
    {
        "id_peminjaman": 3,
        "nama_peminjam": "Dewi",
        "judul_buku": "Malin kundang",
        "tanggal_pinjam": "01-09-2026",
        "tanggal_kembali": "08-09-2026",
        "status": "Dikembalikan"
    },
    {
        "id_peminjaman": 4,
        "nama_peminjam": "Sinta",
        "judul_buku": "Biografi Pahlawan Nasional: Sutan Syahrir",
        "tanggal_pinjam": "09-09-2026",
        "tanggal_kembali": "21-09-2026",
        "status": "Dipinjam"
    },
    {
        "id_peminjaman": 5,
        "nama_peminjam": "Carol",
        "judul_buku": "Peristiwa Rengasdengklok",
        "tanggal_pinjam": "20-08-2026",
        "tanggal_kembali": "07-09-2026",
        "status": "Dikembalikan"
    }
]


# READ

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
                        f"{data['id_peminjaman']:<5}|"
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

# SEARCH

def search():
    while True:
        print("\n==========================================")
        print("     PENCARIAN DATA PEMINJAMAN BUKU")
        print("==========================================")
        print("1. Berdasarkan status (dipinjam / dikembalikan)")
        print("2. Berdasarkan nama peminjam dan judul buku")
        print("3. Kembali")

        input_search = input("Masukkan pilihan menu : ").lower()

        if input_search == "1":
            while True:
                print("\n==========================================")
                print("     PENCARIAN DATA PEMINJAMAN BUKU")
                print("==========================================")
                print("1. Dipinjam")
                print("2. Dikembalikan")
                print("3. Kembali")

                status_cari = input("Masukkan pilihan menu : ")

                if status_cari == "1":
                    keyword = 'dipinjam'
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
                        if (keyword in data["status"].lower()):
                            cari = True
                            print(
                                f"{data['id_peminjaman']:<5}|"
                                f"{data['nama_peminjam'].title():<20}|"
                                f"{data['judul_buku'].title():<50}|"
                                f"{data['tanggal_pinjam']:<15}|"
                                f"{data['tanggal_kembali']:<15}|"
                                f"{data['status'].title():<15}|"
                                )
                            print("-" * 126)

                elif status_cari == "2":
                    keyword = 'dikembalikan'
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
                        if (keyword in data["status"].lower()):
                            cari = True
                            print(
                                f"{data['id_peminjaman']:<5}|"
                                f"{data['nama_peminjam'].title():<20}|"
                                f"{data['judul_buku'].title():<50}|"
                                f"{data['tanggal_pinjam']:<15}|"
                                f"{data['tanggal_kembali']:<15}|"
                                f"{data['status'].title():<15}|"
                                )
                            print("-" * 126)
                elif status_cari == "3":
                    break
                else:
                    print("Input yang Anda masukkan tidak valid !")
                    print("Masukkan angka 1-3 !")

        elif input_search == "2":

            keyword_cari = input("Masukkan nama peminjam atau judul buku : ").lower()

            cari = False

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
                if (keyword_cari in data["nama_peminjam"].lower()
                        or keyword_cari in data["judul_buku"].lower()):
                    cari = True
                    print(
                        f"{data['id_peminjaman']:<5}|"
                        f"{data['nama_peminjam'].title():<20}|"
                        f"{data['judul_buku'].title():<50}|"
                        f"{data['tanggal_pinjam']:<15}|"
                        f"{data['tanggal_kembali']:<15}|"
                        f"{data['status'].title():<15}|"
                        )
                    print("-" * 126)

            if cari == False:
                print("Data tidak ditemukan")

        elif input_search == "3":
            break
        else:
            print("Input yang Anda masukkan tidak valid !")
            print("Masukkan angka 1-3 !")


# CREATE

def create():
    print("\n==========================================")
    print("       TAMBAH DATA PEMINJAMAN BUKU")
    print("==========================================")

    nama_peminjam = input("Nama peminjam     : ")

    # Menampilkan Daftar Buku
    print("\n============================DAFTAR BUKU============================")

    for buku in data_buku:
        print(
            f"{buku["id_buku"]:<5}|"
            f"{buku["judul_buku"]:<50}|"
            f"Stock : {buku["stock"]}"
        )
    print("-"*67)

    #Memilih buku berdasarkan id_buku
    while True:
        input_id_buku = input("Masukkan ID buku : ")

        if input_id_buku.isdigit():
            cari_id_buku = int(input_id_buku)
        else:
            print("ID buku harus berupa angka !")
            continue

        # Mencari buku
        buku_ditemukan = None

        for buku in data_buku:
            if buku["id_buku"] == cari_id_buku:
                buku_ditemukan = buku
                break

        # Validasi ID buku
        if buku_ditemukan is None:
            print("ID buku tidak ditemukan !")
            continue

        # Validasi stock
        if buku_ditemukan["stock"] <= 0:
            print("Stock buku sedang habis !")
            continue
        break

    # Mengambil judul otomatis berdasarkan ID
    judul_buku = buku_ditemukan["judul_buku"]
    print(f"Buku yang dipilih : {judul_buku}")

    # Tanggal pinjam dan tanggal pengembalian
    tanggal_pinjam = date.today()
    tanggal_kembali = tanggal_pinjam + timedelta(days=7)

    tanggal_pinjam = tanggal_pinjam.strftime("%d-%m-%Y")
    tanggal_kembali = tanggal_kembali.strftime("%d-%m-%Y")

    # Membuat ID peminjaman
    id_baru = 1

    for data in data_peminjaman:
        if data["id_peminjaman"] == id_baru:
                    id_baru += 1
        else:
            break

    print(f"Nama peminjam : {nama_peminjam}")
    print(f"Tanggal pinjam    : {tanggal_pinjam}")
    print(f"Tanggal kembali   : {tanggal_kembali}")

    # Konfirmasi    
    while True:
        konfirmasi = input("Anda yakin untuk menyimpan data ini? (y/n) : ").lower()

        if konfirmasi == "y":
            data_baru = {
                    "id_peminjaman": id_baru,
                    "nama_peminjam": nama_peminjam,
                    "judul_buku": judul_buku,
                    "tanggal_pinjam": tanggal_pinjam,
                    "tanggal_kembali": tanggal_kembali,
                    "status": "Dipinjam"}
            data_peminjaman.append(data_baru)

            # Mengurangi stock buku
            buku_ditemukan["stock"] -= 1

            # Mengurutkan ID peminjaman
            data_peminjaman.sort(key=lambda data: data['id_peminjaman'])
            print("\nData peminjaman berhasil ditambahkan.")
            return
        
        elif konfirmasi == "n":
            print("Data batal ditambahkan !")
            break

        else:
            print("Input yang Anda masukkan tidak valid (y atau n)!")

# UPDATE

def update():
    print("\n==========================================")
    print("       UBAH DATA PEMINJAMAN BUKU")
    print("==========================================")

    if len(data_peminjaman) == 0:
        print("Belum ada data peminjaman.")
        return

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
            f"{data['id_peminjaman']:<5}|"
            f"{data['nama_peminjam'].title():<20}|"
            f"{data['judul_buku'].title():<50}|"
            f"{data['tanggal_pinjam']:<15}|"
            f"{data['tanggal_kembali']:<15}|"
            f"{data['status'].title():<15}|"
            )
    print("-" * 126)

    while True:
        input_update = input("Masukkan ID peminjaman : ")

        if  input_update.isdigit():
            input_update = int(input_update)
            break
        else:
            print("ID harus berupa angka.")

    data_ditemukan = None

    for data in data_peminjaman:
        if data["id_peminjaman"] == input_update:
            data_ditemukan = data
            break

    if data_ditemukan is None:
        print("Data dengan ID tersebut tidak ditemukan.")
        return

    judul_lama = data_ditemukan["judul_buku"]
    status_lama = data_ditemukan["status"]

    print("\nData saat ini:")
    print(f"Nama Peminjam   : {data_ditemukan['nama_peminjam']}")
    print(f"Judul Buku      : {data_ditemukan['judul_buku']}")
    print(f"Tanggal Pinjam  : {data_ditemukan['tanggal_pinjam']}")
    print(f"Tanggal Kembali : {data_ditemukan['tanggal_kembali']}")
    print(f"Status          : {data_ditemukan['status']}")

    print("\nMasukkan data baru:")

    nama_baru = input("Nama peminjam baru   : ")
    nama_diubah = nama_baru.strip() != ""

    print("\n============================DAFTAR BUKU============================")
    
    for buku in data_buku:
        print(
            f"{buku['id_buku']:<5}|"
            f"{buku['judul_buku']:<50}|"
            f"Stock : {buku['stock']}"
        )
    print("-"*67)

    judul_diubah = False

    while True:
        input_judul_baru = input("Judul buku baru (berdasarkan ID buku): ")

        if input_judul_baru.strip() == "":
            judul_baru = data_ditemukan["judul_buku"]
            buku_baru = None
            break

        if input_judul_baru.isdigit():
            id_buku_baru = int(input_judul_baru)
        else:
            print("ID buku harus berupa angka !")
            continue

        buku_baru = None

        for buku in data_buku:
            if buku["id_buku"] == id_buku_baru:
                buku_baru = buku
                break

        if buku_baru is None:
            print("ID buku tidak ditemukan !")
            continue

        if buku_baru["judul_buku"] == judul_lama:
            judul_baru = judul_lama
            break

        if buku_baru["stock"] <= 0:
            print("Stock buku sedang habis !")
            continue

        judul_baru = buku_baru["judul_buku"]
        judul_diubah = True
        break

    tanggal_pinjam_baru = input_tanggal("Tanggal pinjam baru (DDMMYYYY) : ", data_ditemukan["tanggal_pinjam"])
    tanggal_diubah = tanggal_pinjam_baru != data_ditemukan["tanggal_pinjam"]

    tanggal_obj = datetime.strptime(tanggal_pinjam_baru, "%d-%m-%Y")
    tanggal_kembali_obj = tanggal_obj + timedelta(days=7)
    tanggal_kembali_baru = tanggal_kembali_obj.strftime("%d-%m-%Y")

    if nama_baru.strip() == "":
        nama_baru = data_ditemukan["nama_peminjam"]

    if judul_baru.strip() == "":
        judul_baru = data_ditemukan["judul_buku"]

    if nama_diubah or judul_diubah or tanggal_diubah:
        status_baru = "Dipinjam"
    else:
        print("\nStatus:")
        print("1. Dipinjam")
        print("2. Dikembalikan")

        while True:
            pilihan_status = input("Pilih status (1/2) : ")

            if pilihan_status == "":
                status_baru = data_ditemukan["status"]
                break
            elif pilihan_status == "1":
                status_baru = "Dipinjam"
                break
            elif pilihan_status == "2":
                status_baru = "Dikembalikan"
                break
            else:
                print("Pilihan status yang anda masukkan tidak valid.")
                print("Masukkan angka 1-2 !")
                

    if status_lama == "Dipinjam" and status_baru == "Dikembalikan":
        tanggal_kembali_baru = datetime.today().strftime("%d-%m-%Y")
    else:
        tanggal_kembali_baru = tanggal_kembali_obj.strftime("%d-%m-%Y")
        

    print(f"Nama Peminjam : {nama_baru}")
    print(f"Judul Buku : {judul_baru}")
    print(f"Tanggal Pinjam    : {tanggal_pinjam_baru}")
    print(f"Tanggal Kembali   : {tanggal_kembali_baru}")


    while True:
        konfirmasi = input(
            "\nApakah kamu yakin ingin mengubah data ini? (y/n) : ").lower()

        if konfirmasi == "y":

            # Jika buku berubah
            if judul_baru != judul_lama:

                # Mengembalikan stock buku lama
                for buku in data_buku:
                    if buku["judul_buku"] == judul_lama:
                        buku["stock"] += 1
                        break
                # Mengurangi stock buku baru jika statusnya dipinjam
                if status_baru == "Dipinjam":
                    buku_baru["stock"] -= 1

            # Jika buku tidak berubah
            else:

                # Status berubah dari Dipinjam menjadi Dikembalikan
                if status_lama == "Dipinjam" and status_baru == "Dikembalikan":
                    for buku in data_buku:
                        if buku["judul_buku"] == judul_lama:
                            buku["stock"] += 1
                            break

                # Status berubah dari Dikembalikan menjadi Dipinjam
                elif status_lama == "Dikembalikan" and status_baru == "Dipinjam":
                    for buku in data_buku:
                        if buku["judul_buku"] == judul_lama:
                            buku["stock"] -= 1
                            break

            data_ditemukan["nama_peminjam"] = nama_baru

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


# INPUT TANGGAL

def input_tanggal(pesan, tanggal_lama):
    while True:
        tanggal = input(pesan)

        # Kalau kosong atau hanya spasi, gunakan tanggal lama
        if tanggal.strip() == "":
            return tanggal_lama

        # Harus terdiri dari 8 angka
        if not tanggal.isdigit() or len(tanggal) != 8:
            print("Format tanggal harus DDMMYYYY. Contoh: 15092026")
            continue

        try:
            tanggal_obj = datetime.strptime(tanggal, "%d%m%Y")

            if tanggal_obj.year != 2026:
                print("Tahun harus 2026.")
                continue

            # Tanggal tidak boleh sebelum hari ini
            if tanggal_obj.date() < datetime.today().date():
                print("Tanggal pinjam yang anda masukkan tidak boleh sebelum hari ini !")
                continue
            return tanggal_obj.strftime("%d-%m-%Y")

        except ValueError:
            print("Tanggal yang dimasukkan tidak valid.")

# DELETE

def delete():
    print("\n==========================================")
    print("        HAPUS DATA PEMINJAMAN BUKU")
    print("==========================================")

    if len(data_peminjaman) == 0:
        print("Belum ada data peminjaman.")
        return

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
            f"{data['id_peminjaman']:<5}|"
            f"{data['nama_peminjam'].title():<20}|"
            f"{data['judul_buku'].title():<50}|"
            f"{data['tanggal_pinjam']:<15}|"
            f"{data['tanggal_kembali']:<15}|"
            f"{data['status'].title():<15}|"
            )
    print("-" * 126)

    try:
        id_cari = int(input("Masukkan ID peminjaman : "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    data_ditemukan = None

    for data in data_peminjaman:
        if data["id_peminjaman"] == id_cari:
            data_ditemukan = data
            break

    if data_ditemukan is None:
        print("Data dengan ID tersebut tidak ditemukan.")
        return

    print("\nData yang akan dihapus:")
    print(f"ID              : {data_ditemukan['id_peminjaman']}")
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

            # Mengurutkan kembali ID mulai dari 1
            for i, data in enumerate(data_peminjaman, start=1):
                data["id_peminjaman"] = i

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
        print("1. Tampilkan Data Peminjaman Buku")
        print("2. Tambah Data Peminjaman Buku")
        print("3. Ubah Data Peminjaman Buku")
        print("4. Hapus Data Peminjaman Buku")
        print("5. Keluar")
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