
import json
from abc import ABC, abstractmethod

# Abstract Base Class for aktivitas
class Aktivitas(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def tampilkan_detail(self):
        """abstrack method to show detail aktivitas."""
        pass

    @abstractmethod
    def ke_dictionary(self):
        """Abstract method to convert object ke dictionary (untuk JSON)."""
        pass


class JadwalOlahraga(Aktivitas):
    def __init__(self, nama, hari, durasi_menit):
        super().__init__(nama)
        self.hari = hari
        self.durasi_menit = durasi_menit
        self.tipe = "Olahraga"

    #abstract class (Polymorphism)
    def tampilkan_detail(self):
        return f"[Olahraga] {self.nama} - Hari: {self.hari}, Durasi: {self.durasi_menit} menit"

    def ke_dictionary(self):
        return {
            "tipe": self.tipe,
            "nama": self.nama,
            "hari": self.hari,
            "durasi_menit": self.durasi_menit
        }

class RencanaMakanan(Aktivitas):
    def __init__(self, nama, waktu_makan, kalori):
        super().__init__(nama)
        self.waktu_makan = waktu_makan
        self.kalori = kalori
        self.tipe = "Makanan"

    def tampilkan_detail(self):
        return f"[Makanan] {self.nama} ({self.waktu_makan}) - Estimasi Kalori: {self.kalori} kkal"

    def ke_dictionary(self):
        return {
            "tipe": self.tipe,
            "nama": self.nama,
            "waktu_makan": self.waktu_makan,
            "kalori": self.kalori
        }

# class for manage all aktivitas(activities) & data
class PengelolaAktivitas:
    def __init__(self, file_path='data/aktivitas.json'):
        self.file_path = file_path
        self.daftar_aktivitas = []
        self.muat_data()

    def tambah_aktivitas(self, aktivitas):
        self.daftar_aktivitas.append(aktivitas)
        print(f"\nBerhasil menambahkan: {aktivitas.nama}")

    def lihat_semua_aktivitas(self):
        if not self.daftar_aktivitas:
            print("\nBelum ada aktivitas yang ditambahkan.")
            return

        print("\n--- Daftar Aktivitas Hidup Sehat Anda ---")
       
        for idx, aktivitas in enumerate(self.daftar_aktivitas, 1):
            print(f"{idx}. {aktivitas.tampilkan_detail()}")
        print("----------------------------------------")

    def simpan_data(self):
        """Menyimpan semua data aktivitas ke dalam file JSON."""
        with open(self.file_path, 'w') as f:
            # Konversi setiap objek aktivitas menjadi dictionary
            data_to_save = [aktivitas.ke_dictionary() for aktivitas in self.daftar_aktivitas]
            json.dump(data_to_save, f, indent=4)
        print("\nData berhasil disimpan!")

    def muat_data(self):
        """Memuat data dari file JSON saat aplikasi dimulai."""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                for item in data:
                    if item['tipe'] == 'Olahraga':
                        aktivitas = JadwalOlahraga(item['nama'], item['hari'], item['durasi_menit'])
                    elif item['tipe'] == 'Makanan':
                        aktivitas = RencanaMakanan(item['nama'], item['waktu_makan'], item['kalori'])
                    self.daftar_aktivitas.append(aktivitas)
        except FileNotFoundError:
            # if file not found, create 'data' folder
            import os
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            print("File data tidak ditemukan, file baru akan dibuat saat menyimpan.")
        except json.JSONDecodeError:
            print("File data kosong atau rusak, memulai dengan daftar kosong.")