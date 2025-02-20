# Mengimpor modul PrettyTable untuk membuat tampilan tabel yang rapi dan terformat
from prettytable import PrettyTable
# Mengimpor modul datetime untuk bekerja dengan tanggal dan waktu
from datetime import datetime
# Mengimpor modul timedelta untuk melakukan operasi dan perhitungan selisih waktu
from datetime import timedelta
# Mengimpor modul sys untuk berinteraksi dengan interpreter Python dan sistem
import sys

# Menggunakan Dictionary dalam List
kendaraan = [
    {
        "plat": "B 0106 LOV",
        "jenis": "Motor",
        "merek": "Beat",
        "status_pajak": True,
        "masa_berlaku": "2024-11-13",
        "harga_pajak": 500000,
    },
    {
        "plat": "BE 0726 MLU",
        "jenis": "Motor",
        "merek": "Ninja",
        "status_pajak": False,
        "masa_berlaku": "2023-01-23",
        "harga_pajak": 1350000,
    },
    {
        "plat": "D 2456 FX",
        "jenis": "Mobil",
        "merek": "Avanza",
        "status_pajak": True,
        "masa_berlaku": "2025-12-20",
        "harga_pajak": 1200000,
    },
    {
        "plat": "DE 8262 FG",
        "jenis": "Mobil",
        "merek": "Pajero Sport",
        "status_pajak": False,
        "masa_berlaku": "2022-12-20",
        "harga_pajak": 4250000,
    },
    {
        "plat": "Y 0282 NAB",
        "jenis": "Yacht",
        "merek": "Lurssen",
        "status_pajak": False,
        "masa_berlaku": "2017-10-03",
        "harga_pajak": 12200000,
    },
    {
        "plat": "A 9876 ZYX",
        "jenis": "Pesawat",
        "merek": "Boeing 77",
        "status_pajak": True,
        "masa_berlaku": "2030-12-25",
        "harga_pajak": 21550000,
    },
    {
        "plat": "F 1123 ABC",
        "jenis": "Kapal Laut",
        "merek": "Titanic",
        "status_pajak": True,
        "masa_berlaku": "2035-12-12",
        "harga_pajak": 15200000,
    },
    {
        "plat": "G 2211 RRT",
        "jenis": "Roket",
        "merek": "SpaceX",
        "status_pajak": True,
        "masa_berlaku": "2050-01-01",
        "harga_pajak": 78700000,
    }
]

penyewaan=[]

header_kendaraan = ["Plat", "Jenis", "Merek", "Status Pajak", "Masa Berlaku", "Harga Pajak"]
header_penyewaan = ["Plat", "Jenis", "Merek", "Nama Penyewa", "Tanggal Sewa", "Tanggal Kembali"]

# HELPER START
def validate_plat(): # Fungsi untuk memvalidasi format plat kendaraan sesuai ketentuan yang berlaku
    while True: # Membuat perulangan tak terbatas untuk memastikan input plat sesuai kriteria
        # Meminta input plat kendaraan dan mengubahnya menjadi huruf kapital
        plat = input("Masukkan plat kendaraan (Ketik 'Y' untuk menampilkan ketentuan plat): ").upper()
        # Memecah plat menjadi list berdasarkan spasi
        plat_list = plat.split(" ")
        # Pesan kesalahan standar untuk format plat yang tidak sesuai
        error_message = "Format salah. Pastikan plat memiliki format 'B 1234 ABC'."
        # Jika pengguna klik 'Y;, akan menampilkan panduan ketentuan plat kendaraan
        if (plat == 'Y'):
            print("Ketentuan plat kendaraan:\n")
            print("1. Kendaraan terdiri dari tiga bagian yang dipisahkan oleh spasi (Contoh: 'B 1234 ABC')")
            print("2. Bagian pertama terdiri dari 1 s/d 2 huruf")
            print("3. Bagian kedua terdiri dari 1 s/d 4 digit angka")
            print("4. Bagian ketiga terdiri dari 1 s/d 3 huruf\n")
            continue
        # Validasi jumlah bagian plat (harus tepat 3 bagian)
        if len(plat_list) != 3:
            print(error_message)
            continue
        # Validasi bagian pertama: 1-2 karakter alfabet
        if not (plat_list[0].isalpha() and 1 <= len(plat_list[0]) <= 2):
            print(error_message)
            continue
        # Validasi bagian kedua: 1-4 digit angka
        if not (plat_list[1].isdigit() and 1 <= len(plat_list[1]) <= 4):
            print(error_message)
            continue
        # Validasi bagian ketiga: 1-3 karakter alfabet
        if not (plat_list[2].isalpha() and 1 <= len(plat_list[2]) <= 3):
            print(error_message)
            continue
        # Mengembalikan plat yang valid
        return plat

def validate_masa_berlaku(): # Fungsi untuk memvalidasi input masa berlaku dengan format tanggal yang tepat
    while True:
        # Meminta input masa berlaku dari pengguna dengan format yang ditentukan
        masa_berlaku = input("Masukkan masa berlaku baru (format: 'YYYY-MM-DD'): ")
        try: # Blok kode yang mungkin menimbulkan error
            # Menggunakan strptime untuk mengecek apakah tanggal sesuai dengan format 'YYYY-MM-DD'
            datetime.strptime(masa_berlaku, "%Y-%m-%d")
            # Mengembalikan masa berlaku jika format tanggal benar
            return masa_berlaku
        except ValueError: # Menangkap kesalahan jika format tanggal tidak sesuai
            # Menampilkan pesan kesalahan kepada pengguna
            print("Format salah. Pastikan masa berlaku memiliki format 'YYYY-MM-DD'.")
            # Melanjutkan perulangan untuk meminta input ulang
            continue

def validate_tanggal(): # Fungsi untuk memvalidasi input tanggal dengan rentang 1-31
    while True:
        try:
            # Meminta input tanggal dan langsung mengonversi ke integer
            tanggal = int(input("Masukkan tanggal yang ingin dicek (1-31): "))  
            # Memeriksa apakah tanggal berada dalam rentang yang valid (1-31)
            if 1 <= tanggal <= 31:
            # Mengembalikan tanggal jika valid
                return tanggal
            else:
            # Menampilkan pesan kesalahan jika tanggal di luar rentang
                print("Tanggal tidak valid! Masukkan angka antara 1-31.")
        except ValueError: # Menangkap error jika input tidak bisa dikonversi ke integer
            print("Input tidak valid! Masukkan angka.")
            # continue

def lanjutkan(konfirmasi): # Fungsi untuk meminta konfirmasi dari pengguna dengan parameter konfirmasi
    while True:
        # Meminta input dari pengguna dengan pesan konfirmasi sesuai dengan argumennya nanti
        validasi = input(konfirmasi + " (Y/N): ").upper()
        # Jika pengguna memilih 'Y', kembalikan nilai True
        if validasi == "Y":
            return True
        # Jika pengguna memilih 'N', kembalikan nilai False
        elif validasi =='N':
            return False
        # Jika input tidak valid (bukan Y atau N)
        else:
            # Tampilkan pesan kesalahan
            print("Pilihan Tidak Valid.")

def tampilkan_kendaraan(data): # Fungsi untuk menampilkan data kendaraan dalam format tabel
    # Membuat objek PrettyTable untuk membuat tampilan tabel yang terformat
    table = PrettyTable() 
    # Mengatur nama kolom header tabel menggunakan variabel header_kendaraan yang telah didefinisikan sebelumnya
    table.field_names = header_kendaraan
    # Iterasi melalui setiap kendaraan dalam list data
    for kendaraan in data:
        # Menambahkan setiap baris data ke dalam tabel
        # .values() mengambil seluruh nilai dari dictionary kendaraan 
        # dan mengubahnya menjadi baris pada tabel
        table.add_row(kendaraan.values())
    # Mencetak tabel yang telah dibuat
    print(table)

def tampilkan_penyewaan(data): # Fungsi untuk menampilkan data penyewaan kendaraan dalam format tabel
    # Memeriksa apakah list penyewaan kosong
    if not penyewaan:
        # Jika tidak ada data penyewaan, tampilkan pesan
        print("\nTidak ada kendaraan yang sedang disewa.")
    else:
        table = PrettyTable()
        # Mengatur nama kolom header tabel menggunakan variabel header_penyewaan
        table.field_names = header_penyewaan
        # Iterasi melalui setiap data penyewaan
        for sewa in data:
            # Menambahkan setiap baris data ke dalam tabel
            # .values() mengambil seluruh nilai dari dictionary penyewaan
            table.add_row(sewa.values())
        # Menampilkan judul/keterangan tabel
        print("\nBerikut adalah Kendaraan yang telah disewa")
        # Mencetak tabel penyewaan
        print(table)

# def tampilkan_data(data,header_data):
#     if not data:
#         # Jika tidak ada data, tampilkan pesan
#         print("\nTidak ada kendaraan.")
#     else:
#         table = PrettyTable()
#         # Mengatur nama kolom header tabel menggunakan variabel header_penyewaan
#         table.field_names = header_data
#         # Iterasi melalui setiap data penyewaan
#         for sewa in data:
#             # Menambahkan setiap baris data ke dalam tabel
#             # .values() mengambil seluruh nilai dari dictionary penyewaan
#             table.add_row(sewa.values())
#         # Menampilkan judul/keterangan tabel
#         print("\nBerikut adalah data Kendaraan")
#         # Mencetak tabel penyewaan
#         print(table)

# tampilkan_data(kendaraan, header_kendaraan)

def check_status_pajak(masa_berlaku): # Fungsi untuk memeriksa status pajak kendaraan berdasarkan masa berlaku
    # Menggunakan datetime.now() untuk mendapatkan tanggal saat ini
    # .strftime() mengubah tanggal menjadi string dengan format tertentu
    today = datetime.now().strftime("%Y-%m-%d")
    # Memeriksa apakah masa berlaku masih lebih besar (di masa depan) dari tanggal hari ini
    # Membandingkan string tanggal untuk menentukan status pajak
    if(masa_berlaku > today ): 
        # Jika masa berlaku masih di masa depan, kembalikan True (pajak masih aktif)
        return True 
    else:
        # Jika masa berlaku sudah lewat atau sama dengan hari ini, kembalikan False (pajak tidak aktif)
        return False

def plat_exist(plat): # Fungsi untuk memeriksa keberadaan plat kendaraan dalam sistem
    # Menggunakan fungsi any() untuk memeriksa apakah plat sudah ada di list kendaraan
    # Melakukan pencarian di seluruh data kendaraan yang tersimpan
    if any(data["plat"] == plat for data in kendaraan):
        # Jika plat ditemukan di salah satu data kendaraan, kembalikan True
        return True
    else:
        # Jika plat tidak ditemukan di data kendaraan, kembalikan False
        return False
    
    # for data in kendaraan:
    #     if data["plat"] == plat:
    #         return True
    # return False

# Fungsi untuk mencari kendaraan berdasarkan nomor plat
# Parameter default 'data' menggunakan list kendaraan global jika tidak ditentukan
def cari_kendaraan(plat_cari, data = kendaraan):
    for item in data:
        if item["plat"] == plat_cari:
            # Jika plat ditemukan, kembalikan seluruh data kendaraan tersebut
            return item 
    # Jika iterasi selesai dan plat tidak ditemukan
    # Tampilkan pesan bahwa kendaraan tidak ditemukan
    print("Kendaraan dengan plat tersebut tidak ditemukan.")
    # Kembalikan None untuk menandakan pencarian gagal
    return None
    # Bukan return False karena yang di return adalah data, bukan bool
    
# Fungsi untuk mencari data penyewaan kendaraan berdasarkan nomor plat
# Mencari di dalam list penyewaan yang berisi data kendaraan yang sedang disewa
def cari_penyewaan(plat_cari):
    for data in penyewaan:
        # Memeriksa apakah plat pada data penyewaan cocok dengan plat yang dicari
        if data["plat"] == plat_cari: 
            # Jika plat ditemukan, kembalikan seluruh data penyewaan tersebut
            return data 
    # Jika iterasi selesai dan plat tidak ditemukan dalam data penyewaan
    # Tampilkan pesan bahwa kendaraan tidak ditemukan dalam penyewaan
    print("Kendaraan dengan plat tersebut tidak ditemukan")
    # Kembalikan None untuk menandakan pencarian gagal
    return None 

# cari_kendaraan(plat_cari, penyewaan)

def kendaraan_tersedia(): # Fungsi untuk menampilkan data kendaraan yang tersedia dan siap disewakan
    # Membuat list untuk menyimpan nomor plat kendaraan yang sedang disewa
    kendaraan_disewa = []
    # Mengiterasi seluruh data penyewaan untuk mengumpulkan nomor plat kendaraan yang sedang disewa
    for sewa in penyewaan:
        kendaraan_disewa.append(sewa["plat"])
    # Mendapatkan daftar kendaraan yang masih aktif/hidup menggunakan fungsi cari_kendaraan_hidup()
    kendaraan_hidup = cari_kendaraan_hidup()
    # Membuat list untuk menyimpan kendaraan yang tidak sedang disewa
    kendaraan_tidak_disewa = []
    # Mengiterasi seluruh kendaraan yang masih aktif
    for item in kendaraan_hidup:
        # Memeriksa apakah nomor plat kendaraan TIDAK ada dalam list kendaraan yang sedang disewa
        if item["plat"] not in kendaraan_disewa:
            # Jika kendaraan tidak sedang disewa, tambahkan ke list kendaraan tidak disewa
            kendaraan_tidak_disewa.append(item)
    # Mengembalikan list kendaraan yang tersedia (tidak sedang disewa)
    return kendaraan_tidak_disewa
# HELPER END -------------------------------------------------------------------------------------------------------------------------

def get_kendaraan(): # Menampilkan kendaraan
    # Memeriksa apakah list kendaraan kosong
    if not kendaraan:
        # Menampilkan pesan jika list kendaraan kosong
        print("Tidak ada data kendaraan.")
    else:
        # Menampilkan fungsi tampilkan kendaraan
        tampilkan_kendaraan(kendaraan)

def get_kendaraan_by_plat(): # Mencari kendaraan berdasarkan plat
    while True: # Membuat perulangan tak terbatas untuk memastikan input plat sesuai kriteria
        # Menggunakan fungsi validate_plat() untuk memastikan format plat valid
        plat = validate_plat()
        # Menggunakan fungsi cari_kendaraan() untuk menemukan detail kendaraan
        kendaraan = cari_kendaraan(plat)
        if not kendaraan:
        # Jika kendaraan tidak ditemukan, tampilkan konfirmasi lanjut
            # If not untuk cek jika kondisinya False atau tidak
            if not lanjutkan("Apakah Anda masih ingin mencari kendaraan lainnya?"):
                # Jika pengguna memilih tidak lanjut, keluar dari perulangan
                break
            else:
                # Jika pengguna memilih lanjut, kembali ke awal perulangan
                continue
        else:
            # Menampilkan pesan konfirmasi bahwa data kendaraan ditemukan
            print("\nBerikut adalah data kendaraan yang Anda cari")
            tampilkan_kendaraan([kendaraan])
            # Menampilkan konfirmasi untuk melanjutkan pencarian
            if not lanjutkan("Apakah Anda masih ingin mencari kendaraan lainnya?"):
                break
    # return menu_read()

def get_kendaraan_by_jenis(): # Fungsi untuk mendapatkan daftar kendaraan berdasarkan jenis kendaraan
    while True:
        # Meminta pengguna memasukkan jenis kendaraan yang ingin dicari
        jenis_kendaraan = input("Masukkan jenis kendaraan: ")
        # Menggunakan filter untuk menyaring kendaraan berdasarkan jenis
        get_kendaraan = list(filter(lambda x: x['jenis'].upper() == jenis_kendaraan.upper(), kendaraan))
        # Jika tidak ada kendaraan yang sesuai dengan jenis yang dimasukkan
        if not get_kendaraan:
            print("Tidak ada kendaraan dengan jenis", jenis_kendaraan)
        
        else:
            print("\nBerikut adalah daftar kendaraan dengan jenis", jenis_kendaraan)
            tampilkan_kendaraan(get_kendaraan)

        if not lanjutkan("Apakah Anda masih ingin mencari berdasarkan jenis kendaraan?"):
            break

# Fungsi untuk mencari kendaraan dengan pajak aktif (status_pajak = True)
def cari_kendaraan_hidup():
     # Menggunakan fungsi filter untuk menyaring kendaraan dengan status pajak aktif
    return list(filter(lambda x: x['status_pajak'] == True, kendaraan))

    # kendaraan_hidup = []
    # for k in kendaraan:
    #     if k['status_pajak']:
    #         kendaraan_hidup.append(k)
    # return kendaraan_hidup

# def cari_kendaraan(status_pajak=True):
#     return list(filter(lambda x: x['status_pajak'] == status_pajak, kendaraan))

# Fungsi untuk mencari kendaraan dengan pajak aktif (status_pajak = False)
def cari_kendaraan_mati():
     # Menggunakan fungsi filter untuk menyaring kendaraan dengan status pajak mati
    return list(filter(lambda x: x['status_pajak'] == False, kendaraan))

def get_kendaraan_by_status_pajak(): # Fungsi untuk menampilkan kendaraan berdasarkan status pajak
    while True:
        # Meminta pengguna memasukkan status pajak yang diinginkan ('Mati' atau 'Hidup')
        status_pajak = input("Masukkan status pajak 'Mati' atau 'Hidup': ")
        # Jika pengguna memasukkan 'Mati', cari kendaraan dengan pajak mati
        if status_pajak.capitalize() == "Mati": 
            print("\nBerikut adalah Daftar Kendaraan dengan Pajak Mati")
            # Memanggil fungsi untuk mencari kendaraan dengan pajak mati
            get_kendaraan = cari_kendaraan_mati()
        # Jika pengguna memasukkan 'Hidup', cari kendaraan dengan pajak hidup
        elif status_pajak.capitalize() == "Hidup": 
            print("\nBerikut adalah Daftar Kendaraan dengan Pajak Hidup")
            # Memanggil fungsi untuk mencari kendaraan dengan pajak hidup
            get_kendaraan = cari_kendaraan_hidup() 
        else:
            # Jika input tidak valid, berikan pesan kesalahan dan ulangi input
            print("Pilihan tidak valid. Masukkan 'Mati' atau 'Hidup'.")
            continue
        # Jika tidak ada kendaraan yang ditemukan sesuai status pajak
        if not get_kendaraan:
            print("Tidak ada kendaraan dengan status pajak", status_pajak)
        # Menampilkan daftar kendaraan
        else:
            tampilkan_kendaraan(get_kendaraan)

        if not lanjutkan("Apakah Anda ingin mencari berdasarkan status pajak?"):
            break

def cek_gangen_by_datetime(): # Fungsi untuk mengecek kendaraan berdasarkan aturan ganjil-genap menggunakan tanggal hari ini
    # Mengambil tanggal hari ini menggunakan modul datetime
    today = datetime.now() 
    print(f"\nTanggal hari ini: {today.strftime('%Y-%m-%d')}")
    # Jika hari ini genap
    if today.day % 2 == 0:
        print("Hari ini adalah tanggal Genap.")
        filter_jenis = "Genap"
        kendaraan_filtered = list(filter(lambda x: int(x['plat'].split(" ")[1]) % 2 == 0, kendaraan))
    # Jika hari ini ganjil
    else:
        print("Hari ini adalah tanggal Ganjil.")
        filter_jenis = "Ganjil"
        kendaraan_filtered = list(filter(lambda x: int(x['plat'].split(" ")[1]) % 2 != 0, kendaraan))
    if kendaraan_filtered:
        print(f"\nDaftar kendaraan dengan plat {filter_jenis}:")
        tampilkan_kendaraan(kendaraan_filtered)
    else:
        print(f"Tidak ada kendaraan dengan plat {filter_jenis} hari ini.")

def cek_gangen_by_input(): # Fungsi untuk mengecek kendaraan berdasarkan aturan ganjil-genap berdasarkan input tanggal
  while True:
    # Validasi input tanggal (misalnya format angka dan validasi lainnya)
    tanggal = validate_tanggal()
    # Jika tanggal genap, filter kendaraan dengan plat nomor genap
    if tanggal % 2 == 0:
      filter_jenis = "Genap"
      get_kendaraan = list(filter(lambda x: int(x['plat'].split(" ")[1]) % 2 == 0, kendaraan))
     # Jika tanggal ganjil, filter kendaraan dengan plat nomor ganjil
    else:
      filter_jenis = "Ganjil"
      get_kendaraan = list(filter(lambda x: int(x['plat'].split(" ")[1]) % 2 != 0, kendaraan))
    # Menampilkan informasi jenis tanggal (ganjil/genap)
    print(f"\nTanggal {tanggal} adalah tanggal {filter_jenis}.")
    # Jika tidak ada kendaraan yang sesuai dengan aturan ganjil-genap
    if not get_kendaraan:
      print(f"Tidak ada kendaraan dengan plat {filter_jenis}")
    else:
      print(f"\nDaftar kendaraan dengan plat {filter_jenis}:")
      tampilkan_kendaraan(get_kendaraan)

    if not lanjutkan("Apakah Anda masih ingin mencari kendaraan berdasarkan ganjil genap?"):
      break

# Fungsi untuk memberikan menu pilihan pengecekan kendaraan berdasarkan aturan ganjil-genap
def cek_gangen():
    while True:
        try:
            # Menampilkan menu pilihan kepada pengguna
            print("\n|=============== Menu Cek Kendaraan program Ganjil-Genap =====================|")
            print("1. Cek Kendaraan berdasarkan Hari Ini")
            print("2. Cek Kendaraan berdasarkan Tanggal Input")
            print("3. Kembali ke Menu Lihat Daftar Kendaraan")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-3): "))

            if pilihan == 1:
                cek_gangen_by_datetime()
            elif pilihan == 2:
                cek_gangen_by_input()
            elif pilihan == 3:
                menu_read()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        # Menangkap kesalahan jika input bukan angka
        except ValueError:
                print("Pilihan tidak valid. Silakan pilih lagi.")

# Fungsi untuk mengurutkan data kendaraan secara ascending
# Default pengurutan berdasarkan field "harga_pajak"
def bubble_sort_asc(field="harga_pajak"):
    # Membuat salinan dari list kendaraan untuk menjaga data asli tetap utuh
    data = kendaraan.copy()
    n = len(data)
    # Loop utama untuk iterasi sebanyak panjang data
    for i in range(n):
        # Loop untuk membandingkan pasangan elemen dalam array
        for j in range(0, n-i-1):
            # Jika elemen saat ini lebih besar dari elemen berikutnya pada field tertentu, tukar posisinya
            if data[j][field] > data[j+1][field]:
                data[j], data[j+1] = data[j+1], data[j]  
    return data

# Fungsi untuk mengurutkan data kendaraan secara descending 
# Default pengurutan berdasarkan field "harga_pajak"
def bubble_sort_desc(field="harga_pajak"):
    data = kendaraan.copy()
    n = len(data)
    # Loop utama untuk iterasi sebanyak panjang data
    for i in range(n):
        # Loop untuk membandingkan pasangan elemen dalam array
        for j in range(0, n-i-1):
            # Jika elemen saat ini lebih kecil dari elemen berikutnya pada field tertentu, tukar posisinya
            if data[j][field] < data[j+1][field]:
                
                data[j], data[j+1] = data[j+1], data[j]
    return data

# def bubble_sort(kendaraan, field="harga_pajak", ascending=True):
#     data = kendaraan.copy()
#     n = len(data)
    
#     # Tentukan kondisi pengurutan berdasarkan nilai ascending
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if ascending:
#                 # Jika ascending, tukar jika elemen saat ini lebih besar dari elemen berikutnya
#                 if data[j][field] > data[j+1][field]:
#                     data[j], data[j+1] = data[j+1], data[j]
#             else:
#                 # Jika descending, tukar jika elemen saat ini lebih kecil dari elemen berikutnya
#                 if data[j][field] < data[j+1][field]:
#                     data[j], data[j+1] = data[j+1], data[j]
    
#     return data

# Fungsi untuk mencari kendaraan dengan harga pajak terkecil
def get_pajak_terkecil(kendaraan):
    # Anggap kendaraan pertama adalah yang harga pajaknya terkecil
    kendaraan_terkecil = kendaraan[0]
    # Loop untuk mengecek setiap kendaraan
    for kendaraan_item in kendaraan:
        # Jika harga pajak kendaraan lebih kecil dari yang terkecil
        if kendaraan_item["harga_pajak"] < kendaraan_terkecil["harga_pajak"]:
            # Update kendaraan terkecil menjadi kendaraan ini
            kendaraan_terkecil = kendaraan_item  

    return kendaraan_terkecil

# def get_pajak(kendaraan, mode="terkecil"):
#     if not kendaraan:  # Jika daftar kendaraan kosong, kembalikan None
#         return None

#     # Asumsi awal
#     result = kendaraan[0]

#     for kendaraan_item in kendaraan:
#         if mode == "terkecil" and kendaraan_item["harga_pajak"] < result["harga_pajak"]:
#             result = kendaraan_item
#         elif mode == "terbesar" and kendaraan_item["harga_pajak"] > result["harga_pajak"]:
#             result = kendaraan_item

#     return result

# Fungsi untuk mencari kendaraan dengan harga pajak terbesar
def get_pajak_terbesar(kendaraan):
    # Anggap kendaraan pertama adalah yang harga pajaknya terbesar
    kendaraan_terbesar = kendaraan[0] 
    # Loop untuk mengecek setiap kendaraan
    for kendaraan_item in kendaraan:
        # Jika harga pajak kendaraan lebih besar dari yang terkecil
        if kendaraan_item["harga_pajak"] > kendaraan_terbesar["harga_pajak"]:
            # Update kendaraan terbesar menjadi kendaraan ini
            kendaraan_terbesar = kendaraan_item

    return kendaraan_terbesar

# Fungsi untuk menampilkan menu dan melakukan pencarian serta pengurutan biaya pajak kendaraan
def get_biaya_pajak():
    while True:
        try:
            # Menampilkan menu pilihan kepada pengguna
            print("\n|=============== Menu Mencari Biaya Pajak ==================|")
            print("1. Tampilkan Biaya Pajak Terkecil")
            print("2. Tampilkan Biaya Pajak Terbesar")
            print("3. Urutkan Biaya Pajak dari yang Terkecil")
            print("4. Urutkan Biaya Pajak dari yang Terbesar")
            print("5. Kembali ke Menu Lihat Daftar Kendaraan")            
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-5): "))

            if pilihan == 1:
                kendaraan_terkecil = get_pajak_terkecil(kendaraan)
                # kendaraan_terkecil = bubble_sort_asc()[0]
                print("\nKendaraan dengan Pajak Terkecil:")
                tampilkan_kendaraan([kendaraan_terkecil]) 
            elif pilihan == 2:
                kendaraan_terbesar = get_pajak_terbesar(kendaraan)
                print("\nKendaraan dengan Pajak Terbesar:")
                tampilkan_kendaraan([kendaraan_terbesar])
            elif pilihan == 3:
                # sorted_asc = bubble_sort(kendaraan, field="harga_pajak", ascending=True)
                print("\nKendaraan diurutkan berdasarkan Pajak Terkecil:")
                tampilkan_kendaraan(bubble_sort_asc()) 
            elif pilihan == 4:
                print("\nKendaraan diurutkan berdasarkan Pajak Terbesar:")
                tampilkan_kendaraan(bubble_sort_desc())
            elif pilihan == 5:
                menu_read()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan tidak valid. Masukkan Angka")

# Fungsi untuk menampilkan menu read
def menu_read(): 
    while True: # Membuat perulangan tak terbatas untuk memastikan input plat sesuai kriteria
        try:
            # Menampilkan menu pilihan kepada pengguna
            print("\n|=============== Menu Lihat Daftar Kendaraan ===============|")
            print("1. Menampilkan Semua Kendaraan")
            print("2. Mencari Kendaraan berdasarkan Plat")
            print("3. Mencari kendaraan berdasarkan Jenis")
            print("4. Mencari Kendaraan berdasarkan Status Pajak")
            print("5. Mengecek Ketersediaan Kendaraan jika Ganjil-Genap")
            print("6. Mencari Biaya Pajak")
            print("7. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-7): "))

            if pilihan == 1:
                print("\nBerikut adalah daftar semua kendaraan")
                get_kendaraan()
            elif pilihan == 2:
                get_kendaraan_by_plat()
            elif pilihan == 3:
                get_kendaraan_by_jenis()
            elif pilihan == 4:
                get_kendaraan_by_status_pajak()
            elif pilihan == 5:
                cek_gangen()
            elif pilihan == 6:
                get_biaya_pajak()
            elif pilihan == 7:
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")

        except ValueError:
            print("Pilihan tidak valid. Masukkan Angka")

# Fungsi untuk menambahkan kendaraan baru ke dalam daftar kendaraan
def add_kendaraan():
    while True:
        plat = validate_plat()

        if plat_exist(plat):
            print("Kendaraan Anda sudah terdaftar.")
            continue

        jenis = input("Masukkan jenis kendaraan (misalnya: motor/mobil): ").capitalize()
        merek = input("Masukkan merek kendaraan: ").capitalize()

        masa_berlaku = validate_masa_berlaku()

        harga_pajak = int(input("Masukkan harga pajak: "))
        # Membuat dictionary baru dengan data kendaraan
        new_data = {
            "plat": plat,
            "jenis": jenis,
            "merek": merek,
            "status_pajak" : check_status_pajak(masa_berlaku),
            "masa_berlaku": masa_berlaku,
            "harga_pajak": harga_pajak,
        }
        # Menampilkan data kendaraan yang baru
        tampilkan_kendaraan([new_data])
        validasi = input("Apakah Anda yakin ingin menambahkan data ini? (Y/N):").upper()

        if(validasi == "Y"):
            # Menambahkan data ke dalam list
            kendaraan.append(new_data)
            print("Data kendaraan berhasil ditambahkan.")
            if not lanjutkan("Apakah Anda ingin menambahkan data kendaraan lainnya?"):
                break
        else:
            if not lanjutkan("Apakah Anda masih ingin menambahkan data kendaraan?"):
                break

# Fungsi untuk menampilkan menu tambah kendaraan dan menangani pilihan pengguna
def menu_create():
    while True:
        try:
            # Menampilkan pilihan menu untuk menambah kendaraan
            print("\n|=============== Menu Tambah Kendaraan =====================|")
            print("1. Tambah Data Kendaraan")
            print("2. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = input("Pilih menu (1-2): ")

            if pilihan == "1":
                add_kendaraan()
            elif pilihan == "2":
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan tidak valid. Masukkan Angka.")

# Fungsi untuk memperbarui data kendaraan yang sudah ada
def update_kendaraan():
    while True:
        tampilkan_kendaraan(kendaraan)
        
        plat = validate_plat()

        kendaraan_data = cari_kendaraan(plat)
        # Jika kendaraan tidak ditemukan berdasarkan plat yang dimasukkan
        if kendaraan_data is None:
            print("Kendaraan dengan plat tersebut tidak ditemukan.")
            if not lanjutkan("Apakah Anda ingin mencari plat lainnya?"):
                break
            else:
                continue

        # Menampilkan data kendaraan yang akan diubah
        print("\nData kendaraan yang akan diubah:")
        tampilkan_kendaraan([kendaraan_data])

        if not lanjutkan("Apakah Anda yakin ingin mengubah data kendaraan ini?"):
            if not lanjutkan("Apakah Anda ingin mencoba mengubah kendaraan lain?"):
                break
            else:
                continue

        while True:
            # Memilih kolom yang ingin diubah
            print("\n|===============Pilih data yang ingin diubah:===============|")
            print("1. Jenis kendaraan")
            print("2. Merek kendaraan")
            print("3. Masa berlaku")
            print("4. Harga pajak")
            print("5. Kembali")
            print("|==============================================================|")

            pilihan = int(input("Pilih nomor (1-6): "))

            if pilihan == 1:
                jenis = input("Masukkan jenis kendaraan baru (misalnya: motor/mobil): ").capitalize()
                kendaraan_data["jenis"] = jenis

            elif pilihan == 2:
                merek = input("Masukkan merek kendaraan baru: ").capitalize()
                kendaraan_data["merek"] = merek

            elif pilihan == 3:
                masa_berlaku = validate_masa_berlaku()
                kendaraan_data["masa_berlaku"] = masa_berlaku
                kendaraan_data["status_pajak"] = check_status_pajak(masa_berlaku)

            elif pilihan == 4:
                harga_pajak = int(input("Masukkan harga pajak baru: "))
                kendaraan_data["harga_pajak"] = harga_pajak

            elif pilihan == 5:
                print("Kembali ke pilih kendaraan.")
                break

            else:
                print("Pilihan tidak valid, silakan pilih lagi.")
                continue

            # Menampilkan data kendaraan yang sudah diperbarui
            print("\nData kendaraan yang telah diperbarui:")
            tampilkan_kendaraan([kendaraan_data])

            if not lanjutkan("Apakah Anda ingin mengubah detail lain dari kendaraan ini?"):
                break

        if not lanjutkan("Apakah Anda ingin mengubah data kendaraan lainnya?"):
            break

# Fungsi menu untuk mengubah data kendaraan                 
def menu_update():
    while True:
        try:
            print("\n|=============== Menu Update Kendaraan =====================|")
            print("1. Ubah Data Kendaraan")
            print("2. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-2): "))

            if pilihan == 1:
                update_kendaraan()
            elif pilihan == 2:
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan tidak valid. Masukkan angka.")

# Fungsi untuk menghapus data kendaraan
def hapus_kendaraan():
    while True:
        tampilkan_kendaraan(kendaraan)

        plat = validate_plat()

        kendaraan_data = cari_kendaraan(plat)

        if kendaraan_data is None:
            print("Kendaraan dengan plat tersebut tidak ditemukan.")
            if not lanjutkan("Apakah Anda ingin mencari plat lainnya?"):
                break
            else:
                continue

        # Menampilkan data kendaraan yang akan dihapus
        print("\nData kendaraan yang akan dihapus:")
        tampilkan_kendaraan([kendaraan_data])

        # Meminta konfirmasi untuk menghapus
        if not lanjutkan("Apakah Anda yakin ingin menghapus data kendaraan ini?"):
            if not lanjutkan("Apakah Anda ingin mencoba menghapus kendaraan lain?"):
                break
            else:
                continue

        # Menghapus kendaraan dari daftar
        kendaraan.remove(kendaraan_data)
        print(f"Kendaraan dengan plat {plat} telah dihapus.")

        if not lanjutkan("Apakah Anda ingin menghapus kendaraan lainnya?"):
            break

# Fungsi untuk menampilkan menu hapus kendaraan
def menu_delete():
    while True:
        try:
            print("\n|=============== Menu Hapus Kendaraan =====================|")
            print("1. Hapus Data Kendaraan")
            print("2. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-2): "))

            if pilihan == 1:
                hapus_kendaraan()
            elif pilihan == 2:
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
                print("Pilihan tidak valid. Masukkan angka.")

# Fungsi ini digunakan untuk memeriksa apakah kendaraan dengan plat tertentu sedang disewa
def is_kendaraan_disewa(plat):
    # Mengecek apakah ada kendaraan yang memiliki plat yang sesuai
    return any(sewa['plat'] == plat for sewa in penyewaan)

    # for sewa in penyewaan:
    #     if sewa['plat'] == plat:
    #         return True  # Jika plat ditemukan, kendaraan sedang disewa
    # return False  # Jika plat tidak ditemukan, kendaraan tidak disewa

def sewa_kendaraan():
    print("\nData kendaraan yang tersedia untuk disewa:")
    tampilkan_kendaraan(kendaraan_tersedia())
    plat = validate_plat()
    if plat_exist(plat):
        if is_kendaraan_disewa(plat):
            print(f"Kendaraan dengan plat {plat} sudah disewa.")
            return
        
        kendaraan_data = cari_kendaraan(plat, kendaraan_tersedia())
        
        if kendaraan_data:
            print("\nData kendaraan yang kamu pilih untuk disewa:")
            tampilkan_kendaraan([kendaraan_data])
            
            nama_penyewa = input("Masukkan Nama Penyewa: ").capitalize()
            tanggal_sewa = datetime.now().strftime("%Y-%m-%d")
            # Menghitung tanggal kembali (misalnya 7 hari kemudian)
            tanggal_kembali = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
            
            # Membuat data penyewaan dan menambahkannya ke dalam daftar penyewaan
            data_penyewaan = {
                "plat": plat,
                "jenis": kendaraan_data["jenis"],
                "merek": kendaraan_data["merek"],
                "nama_penyewa": nama_penyewa,
                "tanggal_sewa": tanggal_sewa,
                "tanggal_kembali": tanggal_kembali
            }

            penyewaan.append(data_penyewaan)
            
            print("\nKendaraan berhasil disewa.")
            tampilkan_penyewaan([data_penyewaan])        
        else:
            print("\nKendaraan tidak terdapat dalam list")
    else:
        print(f"Kendaraan dengan plat {plat} tidak ditemukan dalam sistem.")

def kembalikan_kendaraan():
    # Memeriksa apakah list penyewaan kosong
    if not penyewaan:
        # Jika kosong, tampilkan pesan penyewaan dan kembali ke menu sewa
        tampilkan_penyewaan(penyewaan)
        menu_sewa()
    else:
        # Tampilkan seluruh data penyewaan yang ada
        tampilkan_penyewaan(penyewaan)
        plat = validate_plat()
        if plat_exist(plat):
            
            penyewa_data = cari_penyewaan(plat)
            # Memeriksa apakah data penyewaan ditemukan
            if penyewa_data:
                print()
                tampilkan_penyewaan([penyewa_data])
                
                if lanjutkan("Apakah Anda yakin ingin mengembalikan kendaraan ini?"):
                    penyewaan.remove(penyewa_data)
                    print(f"Kendaraan dengan plat {plat} telah berhasil dikembalikan.")
                else:
                    print("Pengembalian dibatalkan.")
            # Jika data penyewaan tidak ditemukan
            else:
                print(f"Kendaraan dengan plat {plat} tidak ditemukan dalam penyewaan.")
         # Jika plat kendaraan tidak ada dalam sistem
        else:
            print(f"Kendaraan dengan plat {plat} tidak ditemukan dalam sistem.")

def menu_sewa():
    while True:
        try:
            print("\n|==================== Menu Penyewaan Kendaraan ==============|")
            print("1. Sewa Kendaraan")
            print("2. Kembalikan Kendaraan")
            print("3. Lihat Daftar Penyewaan")
            print("4. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-4): "))

            if pilihan == 1:
                sewa_kendaraan()
            elif pilihan == 2:
                kembalikan_kendaraan()
            elif pilihan == 3:
                tampilkan_penyewaan(penyewaan)
            elif pilihan == 4:
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def main_menu():
    while True: # Membuat perulangan tak terbatas untuk memastikan input plat sesuai kriteria
        try: # Blok kode yang mungkin menimbulkan error
            print("\n|==================== Kendaraan Tracker ====================|")
            print("1. Lihat Daftar Kendaraan")
            print("2. Menambah Daftar Kendaraan")
            print("3. Mengubah Daftar Kendaraan")
            print("4. Menghapus Daftar Kendaraan")
            print("5. Penyewaan Kendaraan")
            print("6. Keluar Program")
            print("|===========================================================|")
            # Meminta input masa berlaku dari pengguna dan mengkonversi ke integer
            pilihan = int(input("Pilih menu (1-6): "))

            if pilihan == 1:
                menu_read()
            elif pilihan == 2:
                menu_create()
            elif pilihan == 3:
                menu_update()
            elif pilihan == 4:
                menu_delete()
            elif pilihan == 5:
                menu_sewa()
            elif pilihan == 6:
                print("Terima kasih telah menggunakan program kami!\n")
                sys.exit()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        
        except ValueError:  # Menangkap error jika input tidak bisa dikonversi ke integer
            print("Pilihan tidak valid. Masukkan angka.")

