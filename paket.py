#Nama file : paket.py
#mengimpor modul geometri2D
#yang berada di dalam paket matematika
import matematika.geometri2D

def main():
    #bujur sangkar
    sisi = 5

    luas = matematika.geometr2D.luasBujurSangkar(sisi)

    print("BUJURSANGKAR")
    print("Panjang sisi\t: ", sisi)
    print("Luas\t: ", luas)

if __name__ == "__main__":
    main()