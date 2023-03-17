# DATA EXISTING
gradeStudent = [
    {   
        'Student Code': 'JCDS-0206-001',
        'Nama': 'Ardiana',
        'Modul 1': 95,
        'Modul 2' : 100,
        'Modul 3' : 100
    }
    # {   
    #     'Student Code': 'JCDS-0206-002',
    #     'Nama': 'Berlian',
    #     'Modul 1': 75,
    #     'Modul 2' : 80,
    #     'Modul 3' : 95
    # },
    # {   
    # 'Student Code': 'JCDS-0206-003',
    #     'Nama': 'Cintya',
    #     'Modul 1': 95,
    #     'Modul 2' : 90,
    #     'Modul 3' : 85
    # },
    # {   
    #     'Student Code': 'JCDS-0206-004',
    #     'Nama': 'Denise',
    #     'Modul 1': 85,
    #     'Modul 2' : 80,
    #     'Modul 3' : 90
    # },
    # {   
    #     'Student Code': 'JCDS-0206-005',
    #     'Nama': 'Erlangga',
    #     'Modul 1': 70,
    #     'Modul 2' : 90,
    #     'Modul 3' : 65
    # }
]

# MAIN MENU:
def mainMenu():
    print('\n')
    print('-'*140)
    print('''============== PURWADHIKA ==============
============= DATA SCIENCE ============= ''')
    print("-"*140)
    # while True :
    print('============== MENU UTAMA ==============')
    opsiMainMenu = input('''
Pilihan Menu :
1. Report Data Nilai Siswa
2. Menambah Data Nilai Siswa
3. Mengubah Data Nilai Siswa
4. Menghapus Data Nilai Siswa
5. Keluar Program

Masukkan nomor menu yang dipilih : ''')
    if opsiMainMenu == '1':
        showData()     
    elif opsiMainMenu == '2':
        addData()
    elif opsiMainMenu == '3':
        updateData()
    elif opsiMainMenu == '4':
        delData()
    elif opsiMainMenu == '5':
        print('-'*140)
        print('\t\tSee you!')
        print('-'*140)
        print('\n')
        global run
        run = 0
        # break
    else:
        print('-'*140)
        print('Silahkan masukkan angka sesuai pilihan menu yang tersedia dibawah.\n ')
        mainMenu()

# READ DATA ()
def showData():
    while True:
        print('-'*140)
        print('============== MENU REPORT NILAI ==============')
        opsiShowMenu = input('''
    Pilihan Menu :
    1. Tampilkan semua data nilai siswa
    2. Cari data nilai siswa tertentu
    3. Kembali ke Menu utama

    Masukkan nomor menu yang dipilih : ''')
        if opsiShowMenu == '1' :
            if len(gradeStudent) == 0:
                print('-'*140)
                print("Tidak Ada Data")
            else:
                dataStudent()
        elif opsiShowMenu == '2':
            if len(gradeStudent) == 0:
                print('-'*140)
                print("Tidak Ada Data")
            else:
                searchData()
        elif opsiShowMenu == '3':
            break
        else :
            print('-'*140)
            print('Silahkan masukkan angka sesuai pilihan menu yang tersedia dibawah.')
    mainMenu()

# SUB-READ DATA (ALL DATA)
def dataStudent():
    print('-'*140)
    print('''
================================================ Report Data Nilai Siswa ================================================
================================================= Program Data Science ==================================================\n''')
    print('-'*121)         
    print('|Student Code \t| Nama   \t\t| Modul 1 \t| Modul 2 \t| Modul 3\t| Final Score\t| Status\t|')
    print('-'*121) 
    for i in range(len(gradeStudent)):
        fScore = (gradeStudent[i]['Modul 1']+gradeStudent[i]['Modul 2']+gradeStudent[i]['Modul 3'])//3
        isPass = ""
        if fScore >= 80 and fScore <=100:
            isPass = "Pass   "
        else:
            isPass = "Not Pass"
        print(f"|{(gradeStudent[i]['Student Code'])} \t| {gradeStudent[i]['Nama']}   \t\t| {gradeStudent[i]['Modul 1']} \t\t| {gradeStudent[i]['Modul 2']} \t\t| {gradeStudent[i]['Modul 3']}\t\t| {fScore}\t\t| {isPass}\t|")
    print('-'*121)
    print('\n')

# SUB-READ DATA (SEARCH DATA)
def searchData():
    print('-'*140)
    studentCode = input('Masukkan Student Code : ').upper()
    for i in range (len(gradeStudent)):
        if studentCode == gradeStudent[i]['Student Code']:
            fScore = (gradeStudent[i]['Modul 1']+gradeStudent[i]['Modul 2']+gradeStudent[i]['Modul 3'])//3
            isPass = ""
            if fScore >= 80 and fScore <=100:
                isPass = "Pass   "
            else:
                isPass = "Not Pass"
            print('-'*140)
            print(f'Berikut data nilai siswa dengan student code {studentCode} :\n')
            print('-'*121)
            print("|Student Code \t| Nama   \t\t| Modul 1 \t| Modul 2 \t| Modul 3\t| Final Score\t| Status\t|")
            print('-'*121)
            print(f"|{(gradeStudent[i]['Student Code'])} \t| {gradeStudent[i]['Nama']}   \t\t| {gradeStudent[i]['Modul 1']} \t\t| {gradeStudent[i]['Modul 2']} \t\t| {gradeStudent[i]['Modul 3']}\t\t| {fScore}\t\t| {isPass}\t|")
            print('-'*121)
            break
        elif (i == len(gradeStudent)-1):
            print('-'*140)
            print('\tStudent Code Tidak Ditemukan')

# ADD DATA (STUDENT CODE SUDAH ADA DI DATABASE TTP MINTA INPUT)
def addData():
        print('-'*140)
        print('============== MENU ADD DATA ==============')
        opsiAddData = input('''
    Pilihan Menu :
    1. Tambah data nilai siswa
    2. Kembali ke menu utama

    Masukkan nomor menu yang dipilih : ''') 
        if opsiAddData == '1':
            dataStudent()
            newStudentCode = input('Masukkan Student Code baru : ').upper()
            if(len(gradeStudent)) == 0:
                studentName = input('Nama\t\t : ').capitalize()
                gradeModul1 = int(input('Nilai Modul 1 (0-100)\t : '))
                gradeModul2 = int(input('Nilai Modul 2 (0-100)\t : '))
                gradeModul3 = int(input('Nilai Modul 3 (0-100)\t : '))
                print('\nBerikut data yang akan ditambahkan :')
                print('-'*90)
                print("|Student Code \t| Nama   \t\t| Modul 1 \t| Modul 2 \t| Modul 3\t|")
                print('-'*90)
                print(f"|{newStudentCode} \t| {studentName}   \t\t| {gradeModul1} \t\t| {gradeModul2} \t\t| {gradeModul3}\t\t|")
                print('-'*90)
                saveData = input('\nApakah yakin data ini akan ditambahkan (Ya[1]/Tidak[else])?: ')
                if saveData == '1':
                    gradeStudent.append({
                        'Student Code': newStudentCode,
                        'Nama'      : studentName,
                        'Modul 1'   : gradeModul1,
                        'Modul 2'   : gradeModul2,
                        'Modul 3'   : gradeModul3
                        })
                    print('-'*140)
                    print('Penambahan Data Berhasil Disimpan')
                    dataStudent()
                    # addData()
                else:
                    print('-'*140)
                    print('Penambahan Data Tidak Disimpan')
            else :
                for i in range(len(gradeStudent)):
                    if newStudentCode == gradeStudent [i]['Student Code']:
                            print('-'*140)
                            print('Student Code Sudah Ada di Database')
                            break
                    elif (i == len(gradeStudent)-1):
                        studentName = input('Nama\t\t : ').capitalize()
                        gradeModul1 = int(input('Nilai Modul 1 (0-100)\t : '))
                        gradeModul2 = int(input('Nilai Modul 2 (0-100)\t : '))
                        gradeModul3 = int(input('Nilai Modul 3 (0-100)\t : '))
                        print('\nBerikut data yang akan ditambahkan :')
                        print('-'*90)
                        print("|Student Code \t| Nama   \t\t| Modul 1 \t| Modul 2 \t| Modul 3\t|")
                        print('-'*90)
                        print(f"|{newStudentCode} \t| {studentName}   \t\t| {gradeModul1} \t\t| {gradeModul2} \t\t| {gradeModul3}\t\t|")
                        print('-'*90)
                        saveData = input('\nApakah yakin data ini akan ditambahkan (Ya[1]/Tidak[else])?: ')
                        if saveData == '1':
                            gradeStudent.append({
                                'Student Code': newStudentCode,
                                'Nama'      : studentName,
                                'Modul 1'   : gradeModul1,
                                'Modul 2'   : gradeModul2,
                                'Modul 3'   : gradeModul3
                                })
                            print('-'*140)
                            print('Penambahan Data Berhasil Disimpan')
                            dataStudent()
                        else:
                            print('-'*140)
                            print('Penambahan Data Tidak Disimpan')
            addData()
        elif opsiAddData == '2':
            mainMenu()
        else:
            print('-'*140)
            print('Silahkan masukkan angka sesuai pilihan menu yang tersedia dibawah. ')
            addData()

# UPDATE DATA ()
def updateData():
    # while True:
        print('-'*140)
        print('============ MENU UPDATE DATA ============')
        opsiUpdateData = input('''
    Pilihan Menu :
    1. Ubah Data Nilai Siswa
    2. Kembali ke Menu Utama

    Masukkan nomor menu yang dipilih : ''') 
        if opsiUpdateData == '1':
            dataStudent()
            updateStudentCode = input('Masukkan Student Code : ').upper()
            for i in range(len(gradeStudent)):
                if updateStudentCode == gradeStudent[i]['Student Code'] :
                    # while True:
                        print('-'*140)
                        print('Berikut Data Siswa yang Akan Diubah : ')
                        print('-'*90)         
                        print('|Student Code \t| Nama   \t\t| Modul 1 \t| Modul 2 \t| Modul 3\t|')
                        print('-'*90) 
                        print(f"|{(gradeStudent[i]['Student Code'])} \t| {gradeStudent[i]['Nama']}   \t\t| {gradeStudent[i]['Modul 1']} \t\t| {gradeStudent[i]['Modul 2']} \t\t| {gradeStudent[i]['Modul 3']}\t\t|")
                        print('-'*90)
                        confirm = input('Lanjut Update Data (Ya[1]/Tidak[else])? : ')
                        if confirm == '1':
                            findKey = input('''
    Opsi Kolom
        1.  Student Code
        2.  Nama
        3.  Nilai Modul 1
        4.  Nilai Modul 2
        5.  Nilai Modul 3
                            
    Pilih kolom yang ingin di ubah (1-5) : ''')
                            if findKey == '1' :
                                findKey = 'Student Code'
                                valueChange = input(f'\nMasukkan {findKey} baru : ').upper()
                            elif findKey == '2':
                                findKey = 'Nama'
                                valueChange = input(f'\nMasukkan {findKey} baru : ').capitalize()
                            elif findKey == '3':
                                findKey = 'Modul 1'
                                valueChange = int(input(f'\nMasukkan Nilai {findKey} baru : '))
                            elif findKey == '4':
                                findKey = 'Modul 2'
                                valueChange = int(input(f'\nMasukkan Nilai {findKey} baru : '))
                            elif findKey == '5':
                                findKey = 'Modul 3'
                                valueChange = int(input(f'\nMasukkan Nilai {findKey} baru : '))
                            else:
                                print('\nTidak ada opsi. Kembali ke menu sebelumnya')
                                # updateData()                                   
                            saveData = input('\nApakah data jadi diubah (Ya[1]/Tidak[else]) : ')
                            if saveData == '1':
                                    gradeStudent[i][findKey] = valueChange
                                    print('-'*140)
                                    print('Data Telah Diubah')
                                    dataStudent()
                                    # updateData()
                            else:
                                print('\nData Tidak Diubah')
                            # updateData()       
                        else:
                            print('-'*140)
                            print('Data Tidak Diubah')
                            # updateData()
                elif (i == len(gradeStudent)-1):
                    print('-'*140)
                    print('Student Code Tidak Ditemukan')
                    # updateData()
            updateData()
        elif opsiUpdateData == '2':
            mainMenu()
        else:
            print('-'*140)
            print('Silahkan masukkan angka sesuai pilihan menu yang tersedia dibawah.\n')
            updateData()
    
# DELETE DATA ()
def delData():
    # while True:
        print('-'*140)
        print('============ MENU DELETE DATA ============')
        opsiDelData = input('''
    Pilihan Menu :
    1. Hapus Data Nilai Siswa
    2. Kembali ke Menu Utama

    Masukkan nomor menu yang dipilih : ''') 
        if opsiDelData == '1':
            dataStudent()
            delStudentCode = input('Masukkan Student Code yang Akan Dihapus: ').upper()
            for i in range(len(gradeStudent)):
                if delStudentCode == gradeStudent[i]['Student Code']:
                    fScore = (gradeStudent[i]['Modul 1']+gradeStudent[i]['Modul 2']+gradeStudent[i]['Modul 3'])//3
                    isPass = ""
                    if fScore >= 80 and fScore <=100:
                        isPass = "Pass   "
                    else:
                        isPass = "Not Pass"
                    print('\n')
                    print('-'*140)
                    print('\nBerikut Data Student Code yang Akan Dihapus :\n''')
                    print('-'*121)
                    print("|Student Code \t| Nama   \t\t| Modul 1 \t| Modul 2 \t| Modul 3\t| Final Score\t| Status\t|")
                    print('-'*121)
                    print(f"|{(gradeStudent[i]['Student Code'])} \t| {gradeStudent[i]['Nama']}   \t\t| {gradeStudent[i]['Modul 1']} \t\t| {gradeStudent[i]['Modul 2']} \t\t| {gradeStudent[i]['Modul 3']}\t\t|{fScore}\t\t| {isPass}\t|")
                    print('-'*121)
                    # while True :
                    saveData = input('\nApakah data ini akan dihapus (Ya[1]/Tidak[else])?: ')
                    if saveData == '1':
                            del gradeStudent[i]
                            print('-'*140)
                            print('Data Berhasil Dihapus')
                            dataStudent()
                            break
                            # delData()
                    else:
                            print('-'*140)
                            print('Data Tidak Dihapus')
                            # delData()
                        # break
                elif (i == len(gradeStudent)-1):
                        print('-'*140)
                        print('Student Code Tidak Ditemukan')
                        # delData()
            delData()
        elif opsiDelData == '2':
            mainMenu()
        else:
            print('-'*140)
            print('Silahkan masukkan angka sesuai pilihan menu yang tersedia dibawah.\n')
            delData()
          
# RUN PROGRAM
run = 1
while run == 1:
    mainMenu()
    



