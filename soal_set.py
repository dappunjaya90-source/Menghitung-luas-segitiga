# a. Buatlah 2 set untuk menampung pembelian berdasarkan hari pertama dan pembelian hari kedua
pembelian_hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
pembelian_hari_kedua = {"garam", "gula", "coklat", "kecap"}

print("a. Set Pembelian Hari Pertama:", pembelian_hari_pertama)
print("a. Set Pembelian Hari Kedua:", pembelian_hari_kedua)

# b. Tambahkan "keju" pada pembelian hari kedua (penambahan)
pembelian_hari_kedua.add("keju")
print("b. Pembelian Hari Kedua setelah ditambahkan 'keju':", pembelian_hari_kedua)

# c. Cari barang yang sama pada pembelian hari pertama dan pembelian hari kedua (Irisan/Intersection)
barang_sama = pembelian_hari_pertama.intersection(pembelian_hari_kedua)
print("c. Barang sama:", barang_sama)

# d. Cari barang yang dibeli di hari pertama akan tetapi tidak dibeli pada hari kedua. (Selisih/Difference)
barang_h1_saja = pembelian_hari_pertama.difference(pembelian_hari_kedua)
print("d. Barang H-1 saja:", barang_h1_saja)

# e. Hapus "garam" pada pembelian hari pertama.
pembelian_hari_pertama.remove("garam") # Bisa juga menggunakan .discard("garam")
print("e. Pembelian Hari Pertama setelah hapus 'garam':", pembelian_hari_pertama)

# f. Cari barang yang dibeli di hari kedua akan tetapi tidak dibeli pada hari pertama. (Selisih/Difference)
barang_h2_saja = pembelian_hari_kedua.difference(pembelian_hari_pertama)
print("f. Barang H2 saja:", barang_h2_saja)
# g. Cari barang yang tidak sama pada pembelian hari pertama dan pembelian hari kedua. (Beda Simetris/Symmetric Difference)
barang_tidak_sama = pembelian_hari_pertama.symmetric_difference(pembelian_hari_kedua)
print("g. Barang tidak sama:", barang_tidak_sama)

# h. Tampilkan semua keperluan rumah tangga yang dibeli pada hari pertama
print("h. Pembelian Hari Pertama (Final):", pembelian_hari_pertama)

# i. Tampilkan semua keperluan rumah tangga yang dibeli pada hari kedua
print("i. Pembelian Hari Kedua (Final):", pembelian_hari_kedua)