menuList = [
    '1. Menampilkan Data Siswa',
    '2. Menambah Data Siswa',
    '3. Mengubah Data Siswa',
    '4. Menghapus Data Siswa',
    '5. Keluar Aplikasi'
]

dataSiswa = [
    {
        'NIS': 10001,
        'NamaSiswa' : 'Cole Palmer',
        'Asal': 'Surabaya',
        'Umur': 17,
        'JenisKelamin': 'Laki-laki',
        'Kelas': 'A',
        'Nilai': 90
    },
    {
        'NIS': 10002,
        'NamaSiswa' : 'Lamine Yamal',
        'Asal': 'Medan',
        'Umur': 17,
        'JenisKelamin': 'Laki-laki',
        'Kelas': 'A',
        'Nilai': 87
    },
    {
        'NIS': 10003,
        'NamaSiswa' : 'John Stones',
        'Asal': 'Jakarta',
        'Umur': 16,
        'JenisKelamin': 'Laki-laki',
        'Kelas': 'B',
        'Nilai': 85
    },
    {
        'NIS': 10004,
        'NamaSiswa' : 'Lewis Hamilton',
        'Asal': 'Solo',
        'Umur': 16,
        'JenisKelamin': 'Laki-laki',
        'Kelas': 'B',
        'Nilai': 91

    },
    {
        'NIS': 10005,
        'NamaSiswa' : 'Max Verstapen',
        'Asal': 'Semarang',
        'Umur': 17,
        'JenisKelamin': 'Laki-laki',
        'Kelas': 'C',
        'Nilai': 85
    }
]

def menu1():
    while True:
        print("======= MENU MELIHAT DATA SISWA =======")
        print("1. Menu Melihat Semua Data Siswa")
        print("2. Menu Melihat Data Siswa Berdasarkan Kelas")
        print("3. Menu Melihat Data Siswa Berdasarkan NIS")
        print("4. Menu Melihat Nilai Siswa")
        print("5. Kembali")
        subMenu = input("Masukkan menu yang dituju [1-5]: ")
        if subMenu == '1':
            print("======= SEMUA DATA SISWA =======")
            for siswa in dataSiswa:
                print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                print("=========================================")
        elif subMenu == '2':
            while True: 
                print("======= MENU MELIHAT DATA SISWA DI KELAS TERTENTU =======")
                print("1. Kelas A")
                print("2. Kelas B")
                print("3. Kelas C")
                print("4. Kembali")
                subMenuKelas = input("Masukkan menu yang dituju [1-4]: ")
                if subMenuKelas == '1':
                    for siswa in dataSiswa:
                        if siswa['Kelas'] == 'A':
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                elif subMenuKelas == '2':
                    for siswa in dataSiswa:
                        if siswa['Kelas'] == 'B':
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                elif subMenuKelas == '3':
                    for siswa in dataSiswa:
                        if siswa['Kelas'] == 'C':
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                elif subMenuKelas == '4':
                    break 
                else:
                    print("Input Anda tidak sesuai!")    
        elif subMenu == '3':
            print("======= MENU MELIHAT DATA SISWA BERDASARKAN NIS =======")
            print("Masukkan NIS siswa yang ingin dilihat:")
            try:
                NIS = int(input("NIS: "))
                for siswa in dataSiswa:
                    if siswa['NIS'] == NIS:
                        print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                        break
                else:
                    print("NIS belum terdaftar!")
            except ValueError:
                print("Input harus berupa angka! Silakan coba lagi.")
        elif subMenu == '4':
            while True:
                print("======= MENU MELIHAT NILAI SISWA =======")
                print("1. Melihat Semua Nilai Siswa")
                print("2. Nilai Siswa Berdasarkan Kelas")
                print("3. Nilai Rata-rata Siswa")
                print("4. Nilai Tertinggi Siswa")
                print("5. Nilai Terendah Siswa")
                print("6. Kembali")
                subMenu = input("Masukkan menu yang dituju [1-6]: ")
                if subMenu == '1':
                    print("Data Nilai Siswa")
                    for siswa in dataSiswa:
                        print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Nilai: {siswa['Nilai']}")
                elif subMenu == '2':
                    while True:
                        print("======= MENU MELIHAT NILAI SISWA DI KELAS TERTENTU =======")
                        print("1. Kelas A")
                        print("2. Kelas B")
                        print("3. Kelas C")
                        print("4. Kembali")
                        subMenu = input("Masukkan menu yang dituju [1-4]: ")
                        if subMenu == '1':
                            print("Data Nilai Siswa Kelas A")
                            for siswa in dataSiswa:
                                if siswa['Kelas'] == 'A':
                                    print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Nilai: {siswa['Nilai']}")
                        elif subMenu == '2':
                            print("Data Nilai Siswa Kelas B")
                            for siswa in dataSiswa:
                                if siswa['Kelas'] == 'B':
                                    print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Nilai: {siswa['Nilai']}")
                        elif subMenu == '3':
                            print("Data Nilai Siswa Kelas C")
                            for siswa in dataSiswa:
                                if siswa['Kelas'] == 'C':
                                    print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Nilai: {siswa['Nilai']}")
                        elif subMenu == '4':
                            break
                        else:
                            print("Input Anda tidak sesuai!")
                elif subMenu == '3':
                    print("Data Nilai Rata-rata Siswa")
                    jumlah_siswa = len(dataSiswa)
                    print(f"Jumlah total siswa adalah: {jumlah_siswa}")
                    total_nilai = 0
                    for siswa in dataSiswa:
                        total_nilai += siswa['Nilai']
                    rata_rata = total_nilai / len(dataSiswa)
                    print(f"Rata-rata nilai siswa adalah {rata_rata}")
                elif subMenu == '4':
                    print("Data Nilai Tertinggi Siswa")
                    nilai_tertinggi = max(siswa['Nilai'] for siswa in dataSiswa)
                    for siswa in dataSiswa:
                        if siswa['Nilai'] == nilai_tertinggi:
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Nilai: {siswa['Nilai']}")
                elif subMenu == '5':
                    print("Data Nilai Terendah Siswa")
                    nilai_terendah = min(siswa['Nilai'] for siswa in dataSiswa)
                    for siswa in dataSiswa:
                        if siswa['Nilai'] == nilai_terendah:
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Nilai: {siswa['Nilai']}")
                elif subMenu == '6':
                    break 
                else:
                    print("Input Anda tidak sesuai!")
        elif subMenu == '5':
            break 
        else:
            print("Input Anda tidak sesuai!")
def menu2():
    while True:
        print("======= MENU TAMBAH DATA SISWA =======")
        print("1. Tambah Data Siswa")
        print("2. Kembali")
        subMenu = input("Masukkan menu yang dituju [1-2]: ")
        if subMenu == '1':
            print("Masukkan data siswa baru:")
            try:
                NIS = int(input("NIS: "))
            except ValueError:
                print("Input harus berupa angka! Silakan coba lagi.")
                return
            if any(siswa['NIS'] == NIS for siswa in dataSiswa):
                print("NIS sudah ada di sistem!")
            else:
                NamaSiswa = input("Nama Siswa: ")
                Asal = input("Asal: ")
                try:
                    Umur = int(input("Umur: "))
                except ValueError:
                    print("Input harus berupa angka! Silakan coba lagi.")
                    return 
                JenisKelamin = input("Jenis Kelamin: ")
                Kelas = input("Kelas: ").upper()
                try:
                    Nilai = int(input("Nilai: "))
                except ValueError:
                    print("Input harus berupa angka! Silakan coba lagi.")
                    return
                print("\nData yang akan ditambahkan:")
                print(f"NIS: {NIS}")
                print(f"Nama Siswa: {NamaSiswa}")
                print(f"Asal: {Asal}")
                print(f"Umur: {Umur}")
                print(f"Jenis Kelamin: {JenisKelamin}")
                print(f"Kelas: {Kelas}")
                print(f"Nilai: {Nilai}")
            
                konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
                if konfirmasi == 'y':
                    dataSiswa.append({
                    'NIS': NIS,
                    'NamaSiswa': NamaSiswa,
                    'Asal': Asal,
                    'Umur': Umur,
                    'JenisKelamin': JenisKelamin,
                    'Kelas': Kelas,
                    'Nilai': Nilai
                    })      
                    print(f"Data siswa {NamaSiswa} berhasil ditambahkan!")
                else:
                    print("Penambahan data dibatalkan.")
        elif subMenu == '2':
            break
        else:
            print("Input Anda tidak sesuai!")

def menu3():
    while True:
        print("======= MENU UBAH DATA SISWA =======")
        print("1. Ubah Semua Data Siswa")
        print("2. Ubah Data Siswa Secara Spesifik")
        print("3. Kembali")
        subMenu = input("Masukkan menu yang dituju [1-3]: ")
        if subMenu == '1':
            print("Masukkan NIS siswa yang ingin diubah:")
            try:
                NIS = int(input("NIS: "))
            except ValueError:
                print("Input harus berupa angka! Silakan coba lagi.")
                return
            for siswa in dataSiswa:
                if siswa['NIS'] == NIS:
                    print(f"Nama {siswa['NamaSiswa']} Ditemukan!")
                    print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                    NamaSiswa = input("Nama Siswa: ")
                    Asal = input("Asal: ")
                    try:
                        Umur = int(input("Umur: "))
                    except ValueError:
                        print("Input harus berupa angka! Silakan coba lagi.")
                        return
                    JenisKelamin = input("Jenis Kelamin: ")
                    Kelas = input("Kelas: ").upper()
                    try:
                        Nilai = int(input("Nilai: "))
                    except ValueError:
                        print("Input harus berupa angka! Silakan coba lagi.")
                        return

                    print("\nData yang akan dirubah:")
                    print(f"NIS: {NIS}")
                    print(f"Nama Siswa: {NamaSiswa}")
                    print(f"Asal: {Asal}")
                    print(f"Umur: {Umur}")
                    print(f"Jenis Kelamin: {JenisKelamin}")
                    print(f"Kelas: {Kelas}")
                    print(f"Nilai: {Nilai}")

                    konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
                    if konfirmasi == 'y':
                        siswa.update({
                        'NamaSiswa': NamaSiswa,
                        'Asal': Asal,
                        'Umur': Umur,
                        'JenisKelamin': JenisKelamin,
                        'Kelas': Kelas,
                        'Nilai': Nilai
                        })
                        print(f"Data siswa {NamaSiswa} berhasil diubah!")
                    break
            else:
                print(f"Siswa dengan NIS {NIS} tidak ditemukan!")
        elif subMenu == '2':
            while True:
                print("1. Ubah NIS Siswa")
                print("2. Ubah Nama Siswa")
                print("3. Ubah Asal Siswa")
                print("4. Ubah Umur Siswa")
                print("5. Ubah JenisKelamin Siswa")
                print("6. Ubah Kelas Siswa")
                print("7. Ubah Nilai Siswa")
                print("8. Kembali")
                subMenu = input("Masukkan menu yang dituju [1-8]: ")
                if subMenu == '1':
                    print("Masukkan NIS siswa yang ingin diubah:")
                    try:
                        NIS = int(input("NIS: "))
                    except ValueError:
                        print("Input harus berupa angka! Silakan coba lagi.")
                        return    
                    
                    for siswa in dataSiswa:
                        if siswa['NIS'] == NIS:
                            print(f"Data siswa {siswa['NamaSiswa']} ditemukan!")
                            try:
                                NIS = int(input("NIS: "))
                            except ValueError:
                                print("Input harus berupa angka! Silakan coba lagi.")
                                return 
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                            konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
                            if konfirmasi == 'y':   
                                siswa.update({'NIS': NIS})
                                print(f"NIS siswa {NIS} berhasil diubah!")
                            break
                    else:
                        print(f"Siswa dengan NIS {NIS} tidak ditemukan!")
                elif subMenu == '2':
                    print("Masukkan NIS siswa yang ingin diubah:")
                    try:
                        NIS = int(input("NIS: "))
                    except ValueError:
                        print("Input harus berupa angka! Silakan coba lagi.")
                        return    
                    
                    for siswa in dataSiswa:
                        if siswa['NIS'] == NIS:
                            print(f"Data siswa {siswa['NamaSiswa']} ditemukan!")
                            Nama = input("Nama: ")
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                            konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
                            if konfirmasi == 'y':   
                                siswa.update({'NamaSiswa': Nama})
                                print(f"Nama siswa {Nama} berhasil diubah!")
                            break
                    else:
                        print(f"Siswa dengan NIS {NIS} tidak ditemukan!")   
                elif subMenu == '3':
                    print("Masukkan NIS siswa yang ingin diubah:")
                    try:
                        NIS = int(input("NIS: "))
                    except ValueError:
                        print("Input harus berupa angka! Silakan coba lagi.")
                        return    
                    
                    for siswa in dataSiswa:
                        if siswa['NIS'] == NIS:
                            print(f"Data siswa {siswa['NamaSiswa']} ditemukan!")
                            Asal = input("Asal: ")
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                            konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
                            if konfirmasi == 'y':   
                                siswa.update({'Asal': Asal})
                                print(f"Asal siswa {Asal} berhasil diubah!")
                            break
                    else:
                        print(f"Siswa dengan NIS {NIS} tidak ditemukan!")     
                elif subMenu == '4':
                    print("Masukkan NIS siswa yang ingin diubah:")
                    try:
                        NIS = int(input("NIS: "))
                    except ValueError:
                        print("Input harus berupa angka! Silakan coba lagi.")
                        return    
                    
                    for siswa in dataSiswa:
                        if siswa['NIS'] == NIS:
                            print(f"Data siswa {siswa['NamaSiswa']} ditemukan!")
                            try:
                                Umur = int(input("Umur: "))
                            except ValueError:
                                print("Input harus berupa angka! Silakan coba lagi.")
                                return 
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                            konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
                            if konfirmasi == 'y':   
                                siswa.update({'Umur': Umur})
                                print(f"Umur siswa {Umur} berhasil diubah!")
                            break
                    else:
                        print(f"Siswa dengan NIS {NIS} tidak ditemukan!")
                elif subMenu == '5':
                    print("Masukkan NIS siswa yang ingin diubah:")
                    try:
                        NIS = int(input("NIS: "))
                    except ValueError:
                        print("Input harus berupa angka! Silakan coba lagi.")
                        return    
                    
                    for siswa in dataSiswa:
                        if siswa['NIS'] == NIS:
                            print(f"Data siswa {siswa['NamaSiswa']} ditemukan!")
                            JenisKelamin = input("JenisKelamin: ")
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                            konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
                            if konfirmasi == 'y':   
                                siswa.update({'JenisKelamin': JenisKelamin})
                                print(f"JenisKelamin siswa {JenisKelamin} berhasil diubah!")
                            break
                    else:
                        print(f"Siswa dengan NIS {NIS} tidak ditemukan!")                       
                elif subMenu == '6':
                    print("Masukkan NIS siswa yang ingin diubah:")
                    try:
                        NIS = int(input("NIS: "))
                    except ValueError:
                        print("Input harus berupa angka! Silakan coba lagi.")
                        return    
                    
                    for siswa in dataSiswa:
                        if siswa['NIS'] == NIS:
                            print(f"Data siswa {siswa['NamaSiswa']} ditemukan!")
                            Kelas = input("Kelas: ").upper()
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                            konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
                            if konfirmasi == 'y':   
                                siswa.update({'Kelas': Kelas})
                                print(f"Kelas siswa {Kelas} berhasil diubah!")
                            break
                    else:
                        print(f"Siswa dengan NIS {NIS} tidak ditemukan!")
                elif subMenu == '7':
                    print("Masukkan NIS siswa yang ingin diubah:")
                    try:
                        NIS = int(input("NIS: "))
                    except ValueError:
                        print("Input harus berupa angka! Silakan coba lagi.")
                        return    
                    
                    for siswa in dataSiswa:
                        if siswa['NIS'] == NIS:
                            print(f"Data siswa {siswa['NamaSiswa']} ditemukan!")
                            try:
                                Nilai = int(input("Nilai: "))
                            except ValueError:
                                print("Input harus berupa angka! Silakan coba lagi.")
                                return 
                            print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                            konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
                            if konfirmasi == 'y':   
                                siswa.update({'Nilai': Nilai})
                                print(f"Nilai siswa {Nilai} berhasil diubah!")
                            break
                    else:
                        print(f"Siswa dengan NIS {NIS} tidak ditemukan!")
                elif subMenu == '8':
                    break                       
        elif subMenu == '3':
            break
        else:
            print("Input Anda tidak sesuai!")
def menu4():
    while True:
        print("======= MENU HAPUS DATA SISWA =======")
        print("1. Hapus Data Siswa")
        print("2. Kembali")
        subMenu = input("Masukkan menu yang dituju [1-2]: ")
        if subMenu == '1':
            print("Masukkan NIS siswa yang ingin dihapus:")
            try:
                NIS = int(input("NIS: "))
            except ValueError:
                print("Input harus berupa angka! Silakan coba lagi.")
                continue
            for siswa in dataSiswa:
                if siswa['NIS'] == NIS:
                    print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaSiswa']} , Asal: {siswa['Asal']}, Umur: {siswa['Umur']} tahun, Jenis Kelamin: {siswa['JenisKelamin']}, Kelas: {siswa['Kelas']}, Nilai: {siswa['Nilai']}")
                    konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
                    if konfirmasi == 'y':
                        dataSiswa.remove(siswa)
                        print(f"Data siswa {siswa['NamaSiswa']} berhasil dihapus!")
                        break
                    else:
                        print(f"Penghapusan Data Siswa Dibatalkan!")
            else:
                print(f"Siswa dengan NIS {NIS} tidak ditemukan!")
        elif subMenu == '2':
            break
        else:
            print("Input Anda tidak sesuai!")

def menu5():
    print("======= MENU KELUAR APLIKASI =======")
    print("Terima kasih telah menggunakan aplikasi ini!")

def mainMenu():
    userInput = 5

    while userInput != '5':
        for menu in menuList:
            print(menu)

        userInput = input("Masukkan menu yang dituju [1-5]: ")
        if userInput == '1':
            menu1()
        elif userInput == '2':
            menu2()
        elif userInput == '3':
            menu3()
        elif userInput == '4':
            menu4()
        elif userInput == '5':
            print("Anda telah keluar dari aplikasi.")
        else:
            print("Menu yang Anda pilih tidak sesuai!\n")


mainMenu()