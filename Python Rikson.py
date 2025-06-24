def konversi_ke_desimal(angka, basis):
    basis_map = {1: 2, 2: 8, 3: 10, 4: 16}
    if basis not in basis_map:
        raise ValueError("Pilihan basis tidak valid!")
    return int(angka, basis_map[basis])


def biner_2s_complement(nilai, bit=8):
    if nilai >= 0:
        biner = bin(nilai)[2:].zfill(bit)
    else:
        biner = bin((1 << bit) + nilai)[2:].zfill(bit)
    return ' '.join(biner[i:i + 4] for i in range(0, len(biner), 4))


def tampilkan_konversi(nilai):
    print("\n=== HASIL KONVERSI ===")
    print(f"Desimal     : {nilai}")
    print(f"Biner       : {biner_2s_complement(nilai)}")
    print(f"Oktal       : {oct(nilai)[2:] if nilai >= 0 else '-' + oct(abs(nilai))[2:]}")
    print(f"Heksadesimal: {hex(nilai)[2:].upper() if nilai >= 0 else '-' + hex(abs(nilai))[2:].upper()}")


def input_angka(urutan=""):
    print(f"\nAngka {urutan}:")
    print("1. Biner\n2. Oktal\n3. Desimal\n4. Heksadesimal")
    basis = int(input("Pilih basis (1-4): "))
    angka = input("Masukkan angkanya: ").strip()
    return konversi_ke_desimal(angka, basis)


def menu_konversi():
    print("\n=== MODE KONVERSI BILANGAN ===")
    try:
        nilai = input_angka("yang akan dikonversi")
        tampilkan_konversi(nilai)
    except ValueError as e:
        print(f"Input salah: {e}")


def menu_kalkulator():
    print("\n=== MODE KALKULATOR ===")
    try:
        angka1 = input_angka("pertama")
        operator = input("\nPilih operator (+, -, *, /): ").strip()
        angka2 = input_angka("kedua")

        if operator == '+':
            hasil = angka1 + angka2
        elif operator == '-':
            hasil = angka1 - angka2
        elif operator == '*':
            hasil = angka1 * angka2
        elif operator == '/':
            if angka2 == 0:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
                return
            hasil = angka1 // angka2
        else:
            print("Operator tidak dikenali! Gunakan +, -, *, atau /")
            return

        print(f"\n{angka1} {operator} {angka2} = {hasil}")
        tampilkan_konversi(hasil)

    except ValueError as e:
        print(f"Input salah: {e}")


def menu_utama():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Konversi Bilangan")
        print("2. Kalkulator Bilangan")
        print("0. Keluar")
        try:
            pilihan = int(input("Pilih menu (0-2): "))
            if pilihan == 1:
                menu_konversi()
            elif pilihan == 2:
                menu_kalkulator()
            elif pilihan == 0:
                print("Terima kasih telah menggunakan program ini!")
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid!")


# Jalankan program
if __name__ == "__main__":
    menu_utama()
