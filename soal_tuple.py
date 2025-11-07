# Data Peserta Kelas:
# hari pertama mahasiswa yang masuk adalah Lukman, Andi, Soleh dan Putri
# hari kedua mahasiswa yang masuk adalah Soleh, Putri dan Andi

# a. Masukan data hari pertama kedalam tuple kemudian cetak
tuple_hari_pertama = ("Lukman", "Andi", "Soleh", "Putri")
print("a. Tuple Hari Pertama:", tuple_hari_pertama)

# b. Masukan data hari kedua kedalam tuple kemudian cetak
tuple_hari_kedua = ("Soleh", "Putri", "Andi")
print("b. Tuple Hari Kedua:", tuple_hari_kedua)

# c. Cetak nama soleh pada tuple hari pertama
print(tuple_hari_pertama[2]) 

# d. Gabungkan tuple hari pertama dengan hari kedua kemudian cetak (Concatenation)
tuple_gabungan = tuple_hari_pertama + tuple_hari_kedua
print(tuple_gabungan)

# e. Cari ada berapa data Putri dalam tuple gabungan
jumlah_putri = tuple_gabungan.count("Putri")
print(jumlah_putri)

# f. Adakah nama Lukman dalam tuple hari kedua
tuple_hari_kedua = ("Soleh, Putri, dan Andi")
member = "Lukman" in tuple_hari_kedua
print("Lukman" in tuple_hari_kedua)

# g. Cari apakah nama Andi ada dalam tuple gabungan
jumlah_andi = tuple_gabungan.count("Andi")
print(jumlah_andi)

# h. Kemudian cetak semua isi tuple  gabungan menggunakan perulangan
for nama in tuple_gabungan:
    print(nama)