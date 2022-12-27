class Kubus():
    def __init__ (self,sisi):
        self.sisi = sisi

    def volume (self):
        volume_kubus = self.sisi **3
        print("Volume Kubus Adalah:",volume_kubus)

    def luas (self):
        luas_kubus = 6 * self.sisi **2
        print("Luas Kubus Adalah:", luas_kubus)

class Balok():
    def __init__ (self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi


    def volume (self):
        volume_balok = self.panjang * self.lebar * self.tinggi
        print("Volume balok adalah :", volume_balok)

    def luas (self):
        luas_balok = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang)
        print("Luas Balok Adalah:", luas_balok)

class Tabung():
    def __init__ (self, jari, tinggi):
        self.jari = jari
        self.tinggi = tinggi

    def volume (self):
        volume_tabung = 22/7 * self.jari **2 * self.tinggi
        print("Volume tabung adalah :",round (volume_tabung,2))


    def luas(self):
        luas_tabung = 2 * 22/7 * self.jari * self.tinggi + 2 * 22/7 * self.jari **2
        print("luas tabung adalah :",round (luas_tabung,2))

class LimasSegitiga():
    def __init__ (self, alas, tinggiA, tinggi):
        self.alas = alas
        self.tinggiA = tinggiA
        self.tinggi = tinggi

    def volume (self):
        volume_LimasSegitiga = 1/3 * 1/2 * self.alas * self.tinggiA + (3 * 1/2 * self.alas * self.tinggiA)
        print("volume LimasSegitga adalah :",round (volume_LimasSegitiga,2))


    def luas (self):
        luas_LimasSegitiga = 1/2 * self.alas * self.tinggiA + (3 * 1/2 * self.alas * self.tinggiA)
        print("luas LimasSegitiga adalah :",round (luas_LimasSegitiga,2))

while True:
    print()
    print("TUGAS UAS PBO")
    print("Nama = Masdar")
    print("Nim = D0221323")
    print("Kelas = Informatika E")
    print("""Bangun Ruang Yang Akan Di Hitung
    1.Balok
    2.Kubus
    3.Tabung
    4.LimasSegitiga
    5.Berhenti""")
    menu = input("Masukkan Menu: ")

    if menu =='1':
        p = float(input("Masukkan Panjang:"))
        l = float(input("Masukkan Luas:"))
        t = float(input("Masukkan Tinggi:"))
        Balok = Balok(p,l,t)
        print()
        Balok.volume()
        Balok.luas()
    elif menu =='2':
        s = float(input("Masukkan Sisi:"))
        Kubus = Kubus (s)
        print()
        Kubus.volume()
        Kubus.luas()
    elif menu =='3':
        j = float(input("Masukkan Jari-jari:"))
        t = float(input("Masukkan Tinggi:"))
        Tabung = Tabung(j,t)
        print()
        Tabung.volume()
        Tabung.luas()
    elif menu =='4':
        a = float(input("Masukkan Alas:"))
        tA = float(input("Masukkan Tinggi Alas:"))
        t = float(input("Masukkan Tinggi:"))
        LimasSegitiga = LimasSegitiga(a,tA,t)
        print()
        LimasSegitiga.volume()
        LimasSegitiga.luas()
    elif menu =='5':
        break
    else:
        print("Inputan Salah!")
        