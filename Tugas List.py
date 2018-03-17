print "\n Perhitungan Nilai Mahasiswa \n =========================== \n"
jawab = 'ya'
while (jawab == 'ya'):
    no = input ("NO :")
    nama = raw_input ("Nama Anda :")
    nim = input ("NIM Anda :")
    nilaitugas = input ("Nilai Tugas :")
    nilaiuts = input ("Nilai UTS :")
    nilaiuas = input ("Nilai UAS :")
    nilaiakhir = int(nilaitugas*30/100)+(nilaiuts*35/100)+(nilaiuas*35/100)
    print float(nilaiakhir)
    jawab = raw_input("Tambah data (YA/TIDAK) :")
    if jawab == 'tidak':
        print ("==============================================================")
        print ("| No |   Nama   |   NIM   | TUGAS | UTS | UAS | Nilai AKHIR | ")
        print ("==============================================================")
        print "|",no,"|",nama,"|",nim,"|",nilaitugas,"|",nilaiuts,"|",nilaiuas,"|",nilaiakhir,"|"
        break
