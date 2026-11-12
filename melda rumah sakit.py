Jenis_pasien_rumah_sakit = [
    "1. Pasien Demam Berdarah (DBD)",
    "2. Pasien Tipes",
    "3. Pasien Kanker",
    "4. Pasien Pasca Operasi",
    "5. Pasien Penyakit Jantung",
    "6. Pasien Stroke",
    "7. Pasien Gagal Ginjal",
    "8. Pasien Pneumonia",
    "9. Pasien Kecelakaan",
    "10. Pasien Demam Anak"
]

# Daftar tarif per hari sesuai urutan jenis pasien (dalam Rupiah)
harga_per_hari = [
    500000,   # 1. DBD
    450000,   # 2. Tipes
    1500000,  # 3. Kanker
    1200000,  # 4. Pasca Operasi
    1300000,  # 5. Penyakit Jantung
    1100000,  # 6. Stroke
    1000000,  # 7. Gagal Ginjal
    600000,   # 8. Pneumonia
    850000,   # 9. Kecelakaan
    400000    # 10. Demam Anak
]

print("=== SISTEM DATA PASIEN RUMAH SAKIT ===")
for pasien in Jenis_pasien_rumah_sakit:
    print(pasien)

pilih_jenis = int(input("\nPilih nomor jenis pasien (1-10): "))
lama_opname = int(input("Masukkan lama hari opname: "))
usia_pasien = int(input("Masukkan usia pasien (tahun): "))

if 1 <= pilih_jenis <= 10:
    indeks = pilih_jenis - 1
    tarif_harian = harga_per_hari[indeks]
    total_awal = tarif_harian * lama_opname
    
    # Variabel Boolean (True / False)
    is_rawat_panjang = lama_opname > 7
    is_lansia = usia_pasien >= 60
    dapat_diskon = is_rawat_panjang  # Diskon hanya aktif jika True

    # Menentukan persentase diskon menggunakan variabel Boolean
    if is_rawat_panjang and is_lansia:
        kategori = "Perawatan Intensif Lansia (Subsidi 20%)"
        diskon = 0.20
    elif is_rawat_panjang:
        kategori = "Rawat Inap Jangka Panjang (Subsidi 10%)"
        diskon = 0.10
    elif lama_opname <= 3:
        kategori = "Rawat Inap Singkat (Biaya normal)"
        diskon = 0.0
    else:
        kategori = "Rawat Inap Menengah (Biaya normal)"
        diskon = 0.0

    # Menghitung total biaya akhir
    potongan_harga = total_awal * diskon
    total_bayar = total_awal - potongan_harga

    print("\n--- RINCIAN PASIEN & STATUS (TRUE/FALSE) ---")
    print(f"Jenis Pasien Terpilih    : {Jenis_pasien_rumah_sakit[indeks]}")
    print(f"Rawat Panjang (> 7 hari) : {is_rawat_panjang}")
    print(f"Prioritas Lansia (>= 60) : {is_lansia}")
    print(f"Status Dapat Diskon      : {dapat_diskon}")
    print(f"Kategori                 : {kategori}")

    print("\n--- RINCIAN BIAYA ---")
    print(f"Tarif Per Hari           : Rp {tarif_harian:,.0f}")
    print(f"Biaya Kotor              : Rp {total_awal:,.0f}")
    print(f"Persentase Diskon        : {int(diskon * 100)}%")
    print(f"Nominal Diskon           : Rp {potongan_harga:,.0f}")
    print(f"Total Bayar              : Rp {total_bayar:,.0f}")
else:
    print("Pilihan tidak valid! Harap masukkan angka 1 sampai 10.")
