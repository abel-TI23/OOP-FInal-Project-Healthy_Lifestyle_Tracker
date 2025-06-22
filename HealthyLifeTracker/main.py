from models import PengelolaAktivitas, JadwalOlahraga, RencanaMakanan

def tampilkan_menu():
    """Menampilkan menu utama kepada pengguna."""
    print("\n===== Aplikasi Pelacak Hidup Sehat =====")
    print("1. Tambah Jadwal Olahraga")
    print("2. Tambah Rencana Makanan")
    print("3. Lihat Semua Aktivitas")
    print("4. Simpan Data dan Keluar")
    print("========================================")

def main():
    """Fungsi utama untuk menjalankan aplikasi."""
    pengelola = PengelolaAktivitas()

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda (1-4): ")

        if pilihan == '1':
            nama = input("Masukkan nama olahraga (e.g., Lari Pagi): ")
            hari = input("Masukkan hari (e.g., Senin): ")
            while True:
                try:
                    durasi = int(input("Masukkan durasi dalam menit: "))
                    break
                except ValueError:
                    print("Input tidak valid, harap masukkan angka.")
            
            olahraga_baru = JadwalOlahraga(nama=nama, hari=hari, durasi_menit=durasi)
            pengelola.tambah_aktivitas(olahraga_baru)

        elif pilihan == '2':
            nama = input("Masukkan nama makanan (e.g., Salad Ayam): ")
            waktu = input("Masukkan waktu makan (Pagi/Siang/Malam): ")
            while True:
                try:
                    kalori = int(input("Masukkan estimasi kalori: "))
                    break
                except ValueError:
                    print("Input tidak valid, harap masukkan angka.")

            makanan_baru = RencanaMakanan(nama=nama, waktu_makan=waktu, kalori=kalori)
            pengelola.tambah_aktivitas(makanan_baru)

        elif pilihan == '3':
            pengelola.lihat_semua_aktivitas()

        elif pilihan == '4':
            pengelola.simpan_data()
            print("Terima kasih telah menggunakan aplikasi. Sampai jumpa!")
            break

        else:
            print("\nPilihan tidak valid. Harap masukkan angka antara 1 dan 4.")

if __name__ == "__main__":
    main()