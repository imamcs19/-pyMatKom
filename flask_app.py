# Koding Contoh MK Matematika Komputasi Semester Ganjil 2022/2023 Filkom UB
# Rencana Pembelajaran MK Matematika Komputasi Semester Ganjil 2022/2023 Kelas C
# Fakultas Ilmu Komputer (Filkom), Universitas Brawijaya (UB) 2022.

# Dosen Pengampu:
# 1. Imam Cholissodin, S.Si., M.Kom. | email: imamcs@ub.ac.id | Filkom UB

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Students | Koding Matematika Komputasi (MatKom) pada Teknologi Cloud :D'

# Start =============================
# 2.1 Pengantar Sistem Bilangan
# ===================================
@app.route('/2_1/<dec>')
def code_2_1(dec):

    # konversi "deca atau basis 10" ke "biner atau basis 2"
    # 19 (deca) => 10011 (biner)
    # dengan fungsi lambda
    binary = lambda n: '' if n==0 else binary(n//2) + str(n%2)
    hasil = str(binary(int(dec)))
    hasil = '0' if hasil == '' else hasil

    return hasil

@app.route('/2_1_0/<dec>')
def code_2_1_0(dec):
    # konversi "deca atau basis 10" ke "biner atau basis 2"
    # dengan fungsi yang dibuat mandiri, misal dengan nama decToBin
    def decToBin(n):
        if n==0: return ''
        else:
            return decToBin(n//2) + str(n%2)

    hasil = str(decToBin(int(dec)))
    hasil = '0' if hasil == '' else hasil

    return hasil

@app.route('/2_1_1')
def code_2_1_1():
    # konversi "deca atau basis 10" ke "biner atau basis 2"
    # dengan library numpy
    import numpy as np

    a = 10
    b = 4

    return "a = " + str(a) + " (Basis 10) = " + str(np.binary_repr(a, width=8)) + " (Basis 2) <br>" + \
    "b = " + str(b) + " (Basis 10) = " + str(np.binary_repr(b, width=8)) + " (Basis 2)"

@app.route('/2_1_2')
def code_2_1_2():
    # mencoba konversi bilangan "Decimal ( base r=10 ) atau basis 10" |
    # "Binary ( base r=2) atau basis 2" |
    # "Octal ( base r=8 ) atau basis 8" |
    # "Hexadecimal ( base r=16 ) atau basis 16"

    # contoh:
    # ----------------
    # >>> bin(8)
    # '0b1000'
    # >>> oct(8)
    # '0o10'
    # >>> hex(8)
    # '0x8'
    #
    # octal_num = 17 # misal sbg bilangan octal
    # binary_num = bin(int(str(octal_num), 8))  # octal ke binary, hasilnya '0b1111'
    # dec = int(binary_num, 2)  # binary ke decimal, hasilnya '15'

    # Ref:
    # [0] https://stackoverflow.com/questions/3973685/python-homework-converting-any-base-to-any-base
    # [1] https://stackoverflow.com/questions/67300423/python-octal-to-decimal
    # [2] https://stackoverflow.com/questions/47761528/converting-a-base-10-number-to-any-base-without-strings
    # [3] https://stackoverflow.com/questions/3528146/convert-decimal-to-binary-in-python
    #
    #     Remodified by Imam Cholissodin
    #
    def konversiBilangan(n, base=10, to=10):
        '''
        params atau argumen:
          n     - bilangan yang dikonversi
          base  - basis awal dari bilangan 'n'
          to    - basis target, must be <= 36 , nilai 36 sbg batasan basis
        '''
        # cek basis target untuk memastikan apakah <= 36
        if to > 36 or base > 36:
            raise ValueError('max base is 36')

        # melakukan konversi dengan fungsi bawaan (built-in) dari python yaitu "int",
        # sesuai nilai base sebagai basis yang dimasukkan pada argumen
        n = int(str(n), base)
        positive = n >= 0

        # return if base 10 is desired
        if to == 10:
            return str(n)

        # melakukan konversi sesuai dengan nilai to sebagai basis yang dimasukkan pada argumen
        n = abs(n)
        num = []
        handle_digit = lambda n: str(n) if n < 10 else chr(n + 55)
        while n > 0:
            num.insert(0, handle_digit(n % to))
            n = n // to

        # return hasil dalam bentuk string
        return '0' if ''.join(num)=='' else ''.join(num) if positive else '-' + ''.join(num)


    import numpy as np

    # generate angka dengan basis 10
    batas_generate = 20
    basis_10 = np.arange(0,batas_generate,1)

    # menampung hasil konversi
    basis_2 = []
    basis_8 = []
    basis_16 = []
    for angka_basis_10 in basis_10:
        # basis_10 ke basis_2
        basis_2.append(konversiBilangan(angka_basis_10,10,2))

        # basis_10 ke basis_8
        basis_8.append(konversiBilangan(angka_basis_10,10,8))

        # basis_10 ke basis_16
        basis_16.append(konversiBilangan(angka_basis_10,10,16))


    template_view = '''
        <html>
            <head>
            </head>
            <body>
              <h2>
                <p style="text-decoration: underline;">
                  Mencoba konversi bilangan "Decimal ( base r=10 ) atau basis 10" |
                  "Binary ( base r=2) atau basis 2" |
                  "Octal ( base r=8 ) atau basis 8" |
                  "Hexadecimal ( base r=16 ) atau basis 16:
                </p>
              </h2>
              <table border ="1">
                    <tr>
                      <td align = "center">Decimal ( base r=10 )</td>
                      <td align = "center">Binary ( base r=2)</td>
                      <td align = "center">Octal ( base r=8 )</td>
                      <td align = "center">Hexadecimal ( base r=16 )</td>
                    </tr>
                    {% for angka_basis_10, angka_basis_2, angka_basis_8, angka_basis_16  in basis_all  %}
                    <tr>
                      <td align = "center">{{angka_basis_10}}</td>
                      <td align = "center">{{angka_basis_2}}</td>
                      <td align = "center">{{angka_basis_8}}</td>
                      <td align = "center">{{angka_basis_16}}</td>
                    </tr>
                    {% endfor %}
              </table>
            </body>
        </html>
        '''

    return render_template_string(template_view, basis_all = zip(basis_10, basis_2, basis_8, basis_16))

# End =============================
# 2.1 Pengantar Sistem Bilangan
# ===================================

# Start =============================
# 2.2 Logika Proposisi
# ===================================

@app.route('/2_2_1')
def code_2_2_1():
    # mencoba operator logika "and", "or", "negation" & "xor"
    import numpy as np

    a = 10
    b = 4

    return '''
        <html>
            <head>
            </head>
            <body>
              <h2><p style="text-decoration: underline;">Mencoba operator logika: </p></h2>
              <table border ="1">
                    <tr>
                      <td>a =</td>
                      <td align = "right">%s (Basis 10) = </td>
                      <td>%s (Basis 2)</td>
                    </tr>
                    <tr>
                      <td>b =</td>
                      <td align = "right">%s (Basis 10) = </td>
                      <td>%s (Basis 2)</td>
                    </tr>
              </table>

              <br>

              <form method="post">
                <table border ="1">
                    <tr>
                      <td>Operasi AND</td>
                      <td>Operasi OR</td>
                      <td>Operasi NOT</td>
                      <td>Operasi XOR</td>
                    </tr>
                    <tr>
                      <td>%s</td>
                      <td>%s</td>
                      <td>%s</td>
                      <td>%s</td>
                    </tr>
                </table>
              </form>

            </body>
        </html>
        ''' % (str(a), str(np.binary_repr(a, width=8)), str(b), str(np.binary_repr(b, width=8)), str(np.binary_repr(a & b, width=8)), str(np.binary_repr(a | b, width=8)), str(np.binary_repr(~a, width=8)), str(np.binary_repr(a ^ b, width=8)))

@app.route('/2_2_2')
def code_2_2_2():
    # Contoh Latihan Soal:
    # -------------------------
    # Si A, Si B, Si C adalah beberapa orang yang terdakwa kasus kriminal.
    # Mereka telah tertangkap dan sedang dalam proses diinterogasi oleh Detektif Conan dengan alat poligraph dengan didapatkan pernyatan berikut:
    # +> Si A berkata  : Si B bersalah dan Si C tidak bersalah
    # +> Si B berkata	 : Jika Si A bersalah maka Si C bersalah,
    # +> Si C berkata  : Saya tidak bersalah, tetapi Si B atau Si A bersalah.

    # (a) Tuliskan pernyataan dari semua yang terdakwa ke dalam bentuk logika proposisi.
    #     Lalu buatkan tabel kebenarannya.
    # (b) Tentukan siapa saja yang bersalah (berdasarkan tabel kebenaran tersebut),
    #     bila ternyata hasil tes poligraph memberikan indikasi bahwa Si B telah berbohong,
    #     sementara kedua temannya mengatakan kebenaran!

    # Jawaban:
    # ----------------
    # Berdasarkan dari soal, misal digunakan simbolisasi seperti berikut,
    # p: Si A tidak bersalah
    # q: Si B tidak bersalah
    # r: Si C tidak bersalah

    # Hasil pembuatan Logika Proposisi:
    # Si A : (~q)∧ r
    # Si B : (~p) → (~r)
    # Si C : r ∧ ((~p) ∨ (~q))

    # penentuan jumlah himpunan bagian
    byk_simbol = 3 # dari p, q, r
    byk_himp_bagian = 2**byk_simbol # menyatakan banyak baris tabel
    # print(byk_himp_bagian)
    rasio = 0.5 # untuk deret geometri dari misal 8 => 4, 2, 1
    # pro menyatakan nilai kebenaran proposisi (bisa T/F)
    # misal pro1 mewakili kolom p
    #       pro2 mewakili kolom q
    #       pro3 mewakili kolom r
    #       .. dst
    #
    # pro = np.zeros(byk_himp_bagian,byk_simbol)
    import numpy as np
    pro = np.chararray((byk_himp_bagian,byk_simbol))

    for i in range(byk_simbol):
      loop = int((byk_himp_bagian/2)*(rasio**i))
      # print(loop)
      loop_div = int(byk_himp_bagian/loop)
      cur = 'T'
      Temp_hasil=[]
      for j in range(loop_div):
        if(j==0 or cur == 'T'):
          for letter in 'T'*loop:
            Temp_hasil.append(letter)
          # print('T'*loop, end='')
          cur = 'F'
        elif(cur == 'F'):
          for letter in 'F'*loop:
            Temp_hasil.append(letter)
          # print('F'*loop, end='')
          cur = 'T'
      # print()
      # print(Temp_hasil)
      pro[:,i] = Temp_hasil
      # print()

    # pembuatan tabel kebenaran:
    # ------------------------------------------------------------------------------------------------
    # |  p 	|	q 	|	r	|	Si A ((~q)∧ r)  | Si B ((~p) → (~r)) |   Si C (r ∧ ((~p) ∨ (~q)))	|
    # ------------------------------------------------------------------------------------------------
    # |  T	|	T	|	T	|			F		|			T		 |				F				 |
    # |  T	|	T	|	F	|			F		|			T		 | 				F				 |
    # |  T	|   F	|   T	|           T	    |           T        |          	T                |
    # |  T	F	F	F	T	F
    # |  F	T	T	F	F	T
    # |  F	T	F	F	T	F
    # |  F	F	T	T	F	T
    # |  F	F	F	F	T	F
    # ------------------------------------------------------------------------------------------------

    template_view = '''
        <html>
            <head>
            </head>
            <body>
              <h2>
                <p style="text-decoration: underline;">
                  Mencoba membuat Tabel Kebenaran:
                </p>
              </h2>
              <table border ="1">
                    <tr>
                      <td align = "center">p</td>
                      <td align = "center">q</td>
                      <td align = "center">r</td>
                      <td align = "center">Si A ((~q)∧ r)</td>
                      <td align = "center">Si B ((~p) → (~r))</td>
                      <td align = "center">Si C (r ∧ ((~p) ∨ (~q)))	</td>
                    </tr>
                    {% for pro  in pro_utk_tabel  %}
                    <tr>
                      <td align = "center">{{ pro[0] }}</td>
                      <td align = "center">{{ pro[1] }}</td>
                      <td align = "center">{{ pro[2] }}</td>
                      <td align = "center"></td>
                      <td align = "center"></td>
                      <td align = "center"></td>
                    </tr>
                    {% endfor %}
              </table>
            </body>
        </html>
        '''

    return render_template_string(template_view, pro_utk_tabel = pro.decode().tolist())

# End =============================
# 2.2 Logika Proposisi
# ===================================





