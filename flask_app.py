# Koding Contoh MK Matematika Komputasi Semester Ganjil 2022/2023 Filkom UB
# Rencana Pembelajaran MK Matematika Komputasi Semester Ganjil 2022/2023 Kelas C
# Fakultas Ilmu Komputer (Filkom), Universitas Brawijaya (UB) 2022.

# Dosen Pengampu:
# 1. Imam Cholissodin, S.Si., M.Kom. | email: imamcs@ub.ac.id | Filkom UB

from flask import Flask,render_template, Response, redirect,url_for,session,request,jsonify
from flask import json, make_response, render_template_string
import sqlite3
from flask_cors import CORS

from flask import send_file
from flask_qrcode import QRcode

from requests.packages.urllib3.exceptions import ProtocolError
from collections import OrderedDict
from operator import itemgetter
from textblob import TextBlob

from tweepy.streaming import StreamListener

import tweepy
import re
import string
import datetime
import joblib
from flask import send_file
from io import BytesIO

from flask_wtf.file import FileField
from wtforms import SubmitField
from flask_wtf import FlaskForm
import os

app = Flask(__name__, static_folder='static')
qrcode = QRcode(app)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "static/qr_app/db/database.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# DB untuk qr_app
db_qr = SQLAlchemy(app)
migrate = Migrate(app, db_qr)

# Operasi untuk migrate
# flask db_qr init
# flask db_qr migrate
# flask db_qr upgrade

from static.qr_app.model.StudentModel import Student
from static.qr_app.model.AttendanceModel import Attendance
from static.qr_app.module.Camera import Scanner
import pyqrcode
import uuid

CORS(app, resources=r'/api/*')

app.secret_key = 'filkomub2223^&&*(&^(filkom#BJH#G#VB#MatKom99nDataPyICS_ap938255bnUB'

# @app.route('/')
# def hello_matkom():
#    return 'Hello Students | Koding Matematika Komputasi (MatKom) pada Teknologi Cloud :D'

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

    byk_logic = 3
    pro_hasil_logic = np.chararray((byk_himp_bagian,byk_logic))
    for idx, proposisi_in in enumerate(pro.decode().tolist()):
        p_in = True if proposisi_in[0] == 'T' else False
        q_in = True if proposisi_in[1] == 'T' else False
        r_in = True if proposisi_in[2] == 'T' else False

        # print(idx)
        # print(proposisi_in)

        Temp_hasil = []

        # ((~q)∧ r)
        Temp_hasil.append('T' if ((not q_in) and r_in) else 'F')

        #  ~p --> ~r = ~(~p) V ~r
        Temp_hasil.append('T' if ((not (not p_in)) or (not r_in)) else 'F')

        #  (r ∧ ((~p) ∨ (~q)))
        Temp_hasil.append('T' if (r_in and (not p_in or not q_in)) else 'F')
        pro_hasil_logic[idx,:] = Temp_hasil

    # pembuatan tabel kebenaran:
    # ------------------------------------------------------------------------------------------------
    # |  p 	|	q 	|	r	|	Si A ((~q)∧ r)  | Si B ((~p) → (~r)) |   Si C (r ∧ ((~p) ∨ (~q)))	|
    # ------------------------------------------------------------------------------------------------
    # |  T	|	T	|	T	|			F		|			T		 |				F				 |
    # |  T	|	T	|	F	|			F		|			T		 | 				F				 |
    # |  T	|   F	|   T	|           T	    |           T        |          	T                |
    # |  T	|   F	|   F	|           F    	|           T	     |              F                |
    # |  F	|   T	|   T	|           F	    |           F	     |              T                |
    # |  F	|   T   |	F	|           F	    |           T	     |              F                |
    # |  F	|   F	|   T	|           T	    |           F	     |              T                |
    # |  F  |	F	|   F	|           F	    |           T	     |              F                |
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
                    {% for pro_init, pro_hasil  in pro_utk_tabel  %}
                    <tr>
                      <td align = "center">{{ pro_init[0] }}</td>
                      <td align = "center">{{ pro_init[1] }}</td>
                      <td align = "center">{{ pro_init[2] }}</td>
                      <td align = "center">{{ pro_hasil[0] }}</td>
                      <td align = "center">{{ pro_hasil[1] }}</td>
                      <td align = "center">{{ pro_hasil[2] }}</td>
                    </tr>
                    {% endfor %}
              </table>
            </body>
        </html>
        '''

    return render_template_string(template_view, pro_utk_tabel = zip(pro.decode().tolist(), pro_hasil_logic.decode().tolist()))

# End =============================
# 2.2 Logika Proposisi
# ===================================

@app.route('/db/<aksi>')
def manipulate_tabel(aksi):
    conn = connect_db()
    db = conn.cursor()

    # Aksi => Edit, Hapus, Play, Extenf Date Berlaku

    # db.execute("DROP TABLE IF EXISTS '" + DATABASE_TABLE + "'");

    if aksi == 'c':
        str_info = 'tabel berhasil dibuat :D'
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS data_cronjob
        (tipe_run TEXT, date_pembuatan DATETIME,
        teks_call_sintaks TEXT,
        keterangan TEXT,
        date_masa_berlaku DATETIME)
        """)
    elif aksi== 'd':
        str_info = 'tabel berhasil dihapus :D'
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS data_cronjob
        """)

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/db/CloudAI_Air/<aksi>')
def manipulate_tabel_CloundAI_Air(aksi):
    conn = connect_db()
    db = conn.cursor()

    if aksi == 'c':
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS CloudAI_Air (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
        """)
        str_info = 'tabel berhasil dibuat :D'
    elif aksi== 'd':
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS CloudAI_Air
        """)

        str_info = 'tabel berhasil dihapus :D'

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/db/CloudAI_Air_Rev/<aksi>')
def manipulate_tabel_CloundAI_Air_Rev(aksi):
    conn = connect_db()
    db = conn.cursor()

    if aksi == 'c':
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS CloudAI_Air_Rev (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
        """)
        str_info = 'tabel berhasil dibuat :D'
    elif aksi== 'd':
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS CloudAI_Air_Rev
        """)

        str_info = 'tabel berhasil dihapus :D'

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/user')
def data_user():
    try:
        conn = connect_db()
        db = conn.cursor()

        rs = db.execute("SELECT * FROM user order by id")
        userslist = rs.fetchall()
        return render_template('data_user.html',userslist=userslist)

    except Exception as e:
        print(e)
    finally:
        db.close()
        conn.close()

@app.route("/update_user",methods=["POST","GET"])
def update_user():
    try:
        conn = connect_db()
        db = conn.cursor()
        if request.method == 'POST':
            field = request.form['field']
            value = request.form['value']
            editid = request.form['id']

            if field == 'mail':
                db.execute("""UPDATE user SET Mail=? WHERE id=?""",(value,editid))
            if field == 'name':
                db.execute("""UPDATE user SET Name=? WHERE id=?""",(value,editid))
            if field == 'pwd':
                db.execute("""UPDATE user SET Password=? WHERE id=?""",(value,editid))
            if field == 'level':
                db.execute("""UPDATE user SET Level=? WHERE id=?""",(value,editid))

            conn.commit()
            success = 1
        return jsonify(success)
    except Exception as e:
        print(e)
    finally:
        db.close()
        conn.close()

# ================ awal - dasar ke-2 ===============
#

# buat input dari url, untuk penjumlahan misal 2 bilangan
@app.route('/add/<a>/<b>')
def add_ab(a,b):
    c = int(a) + float(b)
    return 'a + b = ' + str(c)
    # return 'a + b = %s' % c
# https://userAnda.pythonanywhere.com/add/1/2.5
# hasil => a + b = 3.5

#
# buatlah halaman post sekaligus get
# nilai a dan b, lalu ditambahkan
# dengan return kode html dalam flask python Web App
@app.route('/post_add2', methods=["POST", "GET"])
def inputkan_ab():
    # membuat penjumlahan 2 bilangan

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

        a_in = float(request.form['a'])
        b_in = float(request.form['b'])
        c = a_in + b_in

        return '''
        <html>
            <head>
            </head>
            <body>
              <form method="post">
                <input type="text" name="a" value="%s" />
                <input type="text" name="b" value="%s" />
                <input type="submit" value="Hitung a + b"/>

              </form>
              <h2>Hasil a + b = %s + %s = %s </h2>
            </body>
        </html>
        ''' % (a_in, b_in, a_in, b_in, c)

    else: # untuk yang 'GET' data awal untuk di send ke /post_add2
        return '''
            <html>
                <head>
                </head>
                <body>
                  <form action="/post_add2" method="post">
                    Masukkan nilai a = <input type="text" name="a" value="" />
                    <br>
                    Masukkan nilai b = <input type="text" name="b" value="" />
                    <input type="submit" value="Hitung a + b"/>
                  </form>
                </body>
            </html>
        '''

#
# buatlah halaman post sekaligus get
# nilai a dan b, lalu ditambahkan
# dengan return file "form_add3.html" dalam folder "mysite/templates", flask python Web App
@app.route('/post_add3', methods=["POST", "GET"])
def inputkan_ab3():
    # membuat penjumlahan 2 bilangan
    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

        a_in = float(request.form['a'])
        b_in = float(request.form['b'])
        c = a_in + b_in

        return render_template('form_add3.html', a_save = a_in, b_save = b_in, c_save = c)

    else: # untuk yang 'GET' data awal untuk di send ke /post_add3
        return render_template('form_add3.html')


# ================================================================================
# Contoh koding dasar operasi CRUD pada tabel CloudAI_Air,
# mulai dari "def dasar2_create_database():" sampai sebelum "# ================ akhir - dasar ke-2 ==============="
#
# membuat render_template_string sebagai pengganti render_template
# agar semua kodenya hanya dalam 1 file, sehingga lebih mudah untuk membuat dan run kodingnya
#
def dasar2_create_database():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS CloudAI_Air (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
                """)

    conn.commit()
    conn.close()

def dasar2_generate_data():
    """Generate sintesis atau dummy data untuk percontohan."""
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('SELECT * FROM CloudAI_Air')
    entry = cur.fetchone()

    if entry is None:
        import numpy as np
        import pandas as pd
        import os.path

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))


        # Misal skema dataset-nya seperti berikut: => Silahkan dimodifikasi sesuai case Anda
        kolomFitur_X_plus_Target_Y = ['Suhu (X1)','Kelembaban (X2)', 'Curah Hujan (X3)','Angin (X4)','Durasi Air Dlm Menit (Y)']

        # set bykData = 3*np.power(10,7)
        bykData = 10
        bykFitur = len(kolomFitur_X_plus_Target_Y)-1

        # Interval atau Variasi nilai fitur
        nilaiFitur_Suhu = [17,35]
        nilaiFitur_Kelembaban = [70,90]
        nilaiFitur_Curah_Hujan = [2,95]
        nilaiFitur_Angin = [0,15]
        labelTargetY = [0.0,90.0]

        # generate isi dataset
        content_dataGenerate = np.array([np.arange(bykData)]*(bykFitur+1)).T
        df_gen = pd.DataFrame(content_dataGenerate, columns=kolomFitur_X_plus_Target_Y)

        df_gen ['Suhu (X1)'] = np.random.randint(nilaiFitur_Suhu[0], nilaiFitur_Suhu[1], df_gen.shape[0])
        df_gen ['Kelembaban (X2)'] = np.random.randint(nilaiFitur_Kelembaban[0], nilaiFitur_Kelembaban[1], df_gen.shape[0])
        df_gen ['Curah Hujan (X3)'] = np.random.randint(nilaiFitur_Curah_Hujan[0], nilaiFitur_Curah_Hujan[1], df_gen.shape[0])
        df_gen ['Angin (X4)'] = np.random.randint(nilaiFitur_Angin[0], nilaiFitur_Angin[1], df_gen.shape[0])
        df_gen ['Durasi Air Dlm Menit (Y)'] = np.round(np.random.uniform(labelTargetY[0], labelTargetY[1], df_gen.shape[0]),2)

        # save dataframe generate ke *.csv
        import os
        userhome = os.path.expanduser("~").split("/")[-1]

        path = "/home/"+userhome+"/mysite/static/data_contoh"
        if not os.path.exists(path):
            os.makedirs(path)
        # file_name_data_generate = 'static/data_contoh/Data_CloudAI_Air.csv'
        # df_gen.to_csv(file_name_data_generate, encoding='utf-8', index=False)
        url_file_name_data_generate = os.path.join(BASE_DIR, "static/data_contoh/Data_CloudAI_Air.csv")
        df_gen.to_csv(url_file_name_data_generate, encoding='utf-8', index=False)

        # read file *.csv dan tampilkan
        # data_generate = pd.read_csv(file_name_data_generate)

        url = os.path.join(BASE_DIR, "static/data_contoh/Data_CloudAI_Air.csv")

        # Importing the dataset => ganti sesuai dengan case yg anda usulkan
        dataset = pd.read_csv(url)
        # X = dataset.iloc[:, :-1].values
        # y = dataset.iloc[:, 1].values

        def pushCSVdatasetToDB(x1,x2,x3,x4,y):
            #inserting values inside the created table

            cmd = "INSERT INTO CloudAI_Air(suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES('{}','{}','{}','{}','{}')".format(x1,x2,x3,x4,y)
            cur.execute(cmd)
            conn.commit()

        # CSV_to_SQLite3 dari file dataset
        for i in range(0,len(dataset)):
            pushCSVdatasetToDB(dataset.iloc[i][0],dataset.iloc[i][1],dataset.iloc[i][2],dataset.iloc[i][3],dataset.iloc[i][4])
    else:
        ket_hasil = 'Tidak dilakukan Insert, karena Tabel tidak kosong'
        print(ket_hasil)

    conn.commit()
    cur.close()
    conn.close()

@app.route('/dasar2_crud')
def dasar2_index():
    return '<a href="/dasar2_list">Demo Menampilkan List dari Tabel + Support => Create, Read, Update, Delete (CRUD)</a>'

@app.route('/dasar2_list')
def dasar2_list():

    # buat tabel dan generate data dummy
    dasar2_create_database()
    dasar2_generate_data()

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM CloudAI_Air")
    rows = cur.fetchall()

    conn.close()

    #return render_template("list.html", rows=rows)
    return render_template_string(template_list, rows=rows)


@app.route('/dasar2_edit/<int:number>', methods=['GET', 'POST'])
def dasar2_edit(number):
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        item_id      = number
        item_suhu    = request.form['suhu']
        item_kelembaban = request.form['kelembaban']
        item_hujan  = request.form['hujan']
        item_angin = request.form['angin']
        item_durasi = request.form['durasi']

        # suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit

        cur.execute("UPDATE CloudAI_Air SET suhu_dlm_celcius = ?, humidity_kelembaban_dlm_persen = ?, precipitation_curah_hujan_dlm_persen = ?, wind_angin_dlm_km_per_jam = ?, durasi_air_dlm_menit = ? WHERE id = ?",
                    (item_suhu, item_kelembaban, item_hujan, item_angin, item_durasi, item_id))
        conn.commit()

        return redirect('/dasar2_list')

    cur.execute("SELECT * FROM CloudAI_Air WHERE id = ?", (number,))
    item = cur.fetchone()

    conn.close()

    #return render_template("edit.html", item=item)
    return render_template_string(template_edit, item=item)

@app.route('/dasar2_delete/<int:number>')
def dasar2_delete(number):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM CloudAI_Air WHERE id = ?", (number,))

    conn.commit()
    conn.close()

    return redirect('/dasar2_list')

@app.route('/dasar2_add', methods=['GET', 'POST'])
def dasar2_add():
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        # item_id      = number
        item_suhu    = request.form['suhu']
        item_kelembaban = request.form['kelembaban']
        item_hujan  = request.form['hujan']
        item_angin = request.form['angin']
        item_durasi = request.form['durasi']

        cur.execute("""INSERT INTO CloudAI_Air (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES (?, ?, ?, ?, ?)""",
                    (item_suhu, item_kelembaban, item_hujan, item_angin, item_durasi))
        conn.commit()

        return redirect('/dasar2_list')

    #return render_template("add.html", item=item)
    return render_template_string(template_add)

@app.route('/dasar2_add2')
def dasar2_add2():
    conn = connect_db()
    cur = conn.cursor()

    # get data dari iot API
    import requests
    # from datetime import datetime
    # import pytz
    # Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y %H:%M:%S'))

    def F2C(f_in):
        return (f_in - 32)* 5/9

    def Kelvin2C(k_in):
      return (k_in-273.15)

    # list_kota = ['Jakarta','Los Angeles','Chicago','New York City','Toronto','São Paulo', \
    #              'Lagos', 'London', 'Johannesburg', 'Kairo', 'Paris', 'Zurich', 'Istanbul', 'Moskwa', 'Dubai', \
    #             'Mumbai','Hong Kong','Shanghai','Singapura','Tokyo','Sydney']
    list_kota = ['Malang']


    for nama_kota in list_kota:
        #   each_list_link='http://api.weatherapi.com/v1/current.json?key=re2181c95fd6d746e9a1331323220104&q='+nama_kota
        each_list_link='http://api.weatherapi.com/v1/current.json?key=2181c95fd6d746e9a1331323220104&q='+nama_kota
        resp=requests.get(each_list_link)

        # print(nama_kota)

        #http_respone 200 means OK status
        if resp.status_code==200:
            resp=resp.json()
            suhu = resp['current']['temp_c']
            curah_hujan = resp['current']['precip_mm']
            lembab = resp['current']['humidity']
            angin = resp['current']['wind_mph']
        else:
            # print("Error")
            suhu = '-'
            curah_hujan = '-'
            lembab = '-'
            angin = '-'

        # print(nama_kota, 'dengan suhu = ', round(float(suhu),2),'°C', end='\n')

        cur.execute("""INSERT INTO CloudAI_Air (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam) VALUES (?, ?, ?, ?)""",
                (suhu, lembab, curah_hujan, angin))

        conn.commit()
        cur.close()
        conn.close()

    return redirect('/dasar2_list')

template_list = """
<h2>Menampilkan Data CloudAI Air + Support Create, Read, Update, delete (CRUD)</h2>
<a href="{{ url_for( "dasar2_add" ) }}">Tambah Data</a> |
<a href="{{ url_for( "dasar2_add2" ) }}">Tambah Data dari iot_api (tanpa nilai Durasi Waktu)</a>
{% if rows %}
<table border="1">
    <thead>
        <td>No</td>
        <td>Suhu (°C)</td>
        <td>Kelembaban (%)</td>
        <td>Curah Hujan (%)</td>
        <td>Kecepatan Angin (Km/Jam)</td>
        <td>Durasi Waktu Pengairan / Penyiraman (Menit)</td>
    </thead>

    {% for row in rows %}
    <tr>
        <td>{{ loop.index }}</td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
        <td>{{row[3]}}</td>
        <td>{{row[4]}}</td>
        <td>{{row[5]}}</td>
        <td>
            <a href="{{ url_for( "dasar2_edit", number=row[0] ) }}">Edit</a> |
            <a href="{{ url_for( "dasar2_delete", number=row[0] ) }}">Hapus</a>
        </td>
    </tr>
    {% endfor %}
</table>
{% else %}
Empty</br>
{% endif %}
"""

template_add = """
<h1>Tambah Data CloudAI Air</h1>
<form method="POST" action="{{ url_for( "dasar2_add" ) }}">
    Suhu: <input name="suhu" value=""/></br>
    Kelembaban: <input name="kelembaban" value=""/></br>
    Curah Hujan: <input name="hujan" value=""/></br>
    Kecepatan Angin: <input name="angin" value=""/></br>
    Durasi Waktu Pengairan / Penyiraman: <input name="durasi" value=""/></br>
    <button>Simpan Data</button></br>
</form>
"""

template_edit = """
<h1>Edit Data CloudAI Air</h1>
<form method="POST" action="{{ url_for( "dasar2_edit", number=item[0] ) }}">
    Suhu: <input name="suhu" value="{{item[1]}}"/></br>
    Kelembaban: <input name="kelembaban" value="{{item[2]}}"/></br>
    Curah Hujan: <input name="hujan" value="{{item[3]}}"/></br>
    Kecepatan Angin: <input name="angin" value="{{item[4]}}"/></br>
    Durasi Waktu Pengairan / Penyiraman: <input name="durasi" value="{{item[5]}}"/></br>
    <button>Simpan Update Data</button></br>
</form>
"""

# ================ akhir - dasar ke-2 ===============

# ================ awal - dasar ke-1 ===============
# #

# @app.route('/add')
# def add():
#     # membuat penjumlahan 2 bilangan
#     a = 10
#     b = 90
#     c = a + b

#     return str(c)

# # buatlah halaman perkalian
# # antara a*b
# @app.route('/kali')
# def kali():
#     # membuat perkalian 2 bilangan
#     a = 10
#     b = 90
#     c = a * b

#     return str(c)

# # buatlah tampilan indeks looping 1..10
# @app.route('/loop')
# def loop():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         c +=str(i+1) + '  '

#     return str(c)

# # buatlah tampilan indeks looping 1..10 dengan new line (<br> dari tag html)
# @app.route('/loop_new_line')
# def loop_new_line():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         c +=str(i+1) + '<br>'

#     return str(c)

# # buatlah tampilan indeks looping 1 sampai 10
# # yang ganjil
# @app.route('/ganjil')
# def ganjil():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         if((i+1)%2!=0):
#             c +=str(i+1) + '  '

#     return str(c)
# # ================ akhir - dasar ke-1 ===============

# ========= untuk Tugas Ke-1 & 2 | Project =================

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login",methods=["GET", "POST"])
def login():
  conn = connect_db()
  db = conn.cursor()
  msg = ""
  if request.method == "POST":
      mail = request.form["mail"]
      passw = request.form["passw"]

      rs = db.execute("SELECT * FROM user WHERE Mail=\'"+ mail +"\'"+" AND Password=\'"+ passw+"\'" + " LIMIT 1")

      conn.commit()

      hasil = []
      for v_login in rs:
          hasil.append(v_login)

      if hasil:
          session['name'] = v_login[3]
          return redirect(url_for("2_2_1"))
      else:
          msg = "Masukkan Username (Email) dan Password dgn Benar!"

  return render_template("login.html", msg = msg)

@app.route("/register", methods=["GET", "POST"])
def register():
  conn = connect_db()
  db = conn.cursor()
  if request.method == "POST":
      mail = request.form['mail']
      uname = request.form['uname']
      passw = request.form['passw']

      cmd = "insert into user(Mail, Password,Name,Level) values('{}','{}','{}','{}')".format(mail,passw,uname,'1')
      conn.execute(cmd)
      conn.commit()

      # conn = db

      return redirect(url_for("login"))
  return render_template("register.html")

def connect_db():
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data.db")

    return sqlite3.connect(db_path)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html")

@app.route('/iot', methods=["GET", "POST"])
def iot():

    if 'name' in session:
        name = session['name']
    else:
        name = 'Guest'

    # start kode untuk download atau export semua data dari tabel data_suhu_dll menjadi file *.csv
    if request.method == "POST":

        from io import StringIO
        import csv

        # date_var = request.args.get('date_var')
        # kota_var = request.args.get('kota_var')
        conn = connect_db()
        db = conn.cursor()

        output = StringIO()
        writer = csv.writer(output)
        c = db.execute("SELECT * FROM data_suhu_dll")

        result = c.fetchall()
        writer.writerow([i[0] for i in c.description])

        for row in result:
            line = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])]
            writer.writerow(line)

        output.seek(0)

        conn.commit()
        db.close()
        conn.close()

        return Response(output, mimetype="text/csv",
                        headers={"Content-Disposition": "attachment;filename=data_suhu_iot_all.csv"})
    # ending kode untuk download atau export semua data dari tabel data_suhu_dll menjadi file *.csv


    # menampilkan data dari tabel data_suhu_dll
    conn = connect_db()
    db = conn.cursor()

    c = db.execute(""" SELECT * FROM  data_suhu_dll """)

    mydata = c.fetchall()
    for x in c.fetchall():
        name_v=x[0]
        data_v=x[1]
        break

    hasil = []
    for v_login in c:
        hasil.append(v_login)

    conn.commit()
    db.close()
    conn.close()


    return render_template("getsuhu_dll.html", header = mydata)

@app.route('/del_iot/', methods=["GET"])
def del_iot():
    date_var = request.args.get('date_var')
    kota_var = request.args.get('kota_var')
    conn = connect_db()
    db = conn.cursor()

    db.execute("DELETE FROM data_suhu_dll WHERE date =\'"+ date_var +"\' AND  kota =\'"+ kota_var +"\'")

    conn.commit()
    db.close()
    conn.close()

    return redirect(url_for("iot"))

@app.route('/dw_iot/', methods=["GET"])
def dw_iot():

    from io import StringIO
    import csv

    date_var = request.args.get('date_var')
    # kota_var = request.args.get('kota_var')
    conn = connect_db()
    db = conn.cursor()

    output = StringIO()
    writer = csv.writer(output)
    c = db.execute("SELECT * FROM data_suhu_dll WHERE date =\'"+ date_var +"\'")

    result = c.fetchall()
    writer.writerow([i[0] for i in c.description])

    for row in result:
        line = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])]
        writer.writerow(line)

    output.seek(0)

    conn.commit()
    db.close()
    conn.close()

    return Response(output, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment;filename=data_suhu_iot.csv"})

@app.route('/logout')
def logout():
   # remove the name from the session if it is there
   session.pop('name', None)
   return redirect(url_for('index'))


# ================
# Ergo Project

@app.route("/in")
def index_qrcode():
    return render_template("qrcode.html")


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")

@app.route('/qr_index')
def qr_index():
    attendance = Attendance.getAll()
    return render_template("qr_scan2.html", data=enumerate(attendance, 1))


@app.route("/qr_scan", methods=["GET"])
def qr_scan():
    return Response(scanner(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/qr_student", methods=["GET", "POST"])
def qr_student():
    if request.method == "POST":
        name = request.form['name']
        nim = request.form['nim']
        UUID = str(uuid.uuid4())
        qr_code_mark = "static/img/tmp_qr/{}.png".format(UUID)
        student = Student(nim=nim, name=name, qr_code=qr_code_mark)
        student.save()

        import qrcode

        # # /qrcode
        # qrcode_img = qrcode.make(student.id)
        # # buf = io.BytesIO()
        # buf_qrcode = BytesIO()
        # qrcode_img.save(buf_qrcode)
        # buf_qrcode.seek(0)
        # # return send_file(buf_qrcode, mimetype='image/jpeg')

        qrcode_img = qrcode.make(student.id)
        # qrcode_img = qrcode(student.id)
        # canvas = Image.new('RGB', (290,290), 'white')
        # draw = ImageDraw.Draw(canvas)
        # canvas.paste(qrcode_img)
        # fname = f'qr_code_{self.name}.png'
        fname = f'static/img/tmp_qr/qr_code_{student.id}.png'.format(UUID)
        buffer = BytesIO()
        # canvas.save(buffer,'PNG')
        # qrcode_img.save(fname, File(buffer), save=False)
        # qrcode_img.save(fname, buffer, save=False)
        # qrcode_img.save(buffer)

        import os.path

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        url_file_name_qrcode = os.path.join(BASE_DIR, fname)

        qrcode_img.save(url_file_name_qrcode, format="PNG")
        # canvas.close()
        # super().save(*args, **kwargs)

        # img = pyqrcode.create(student.id, error="L", mode="binary", version=5)
        # img.png(qr_code, scale=10)
    students = Student.getAll()
    return render_template("qr_student.html", data=enumerate(students, 1))


def scanner():
    camera = Scanner()
    while True:
        frame = camera.get_video_frame()

        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            break

@app.route('/menu')
def launchpad_menu():
   return render_template("launchpad_menu3.html")
   #return render_template("launchpad_menu2.html")
   #return render_template("launchpad_menu.html")