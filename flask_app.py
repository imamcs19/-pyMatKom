# Koding Contoh MK Matematika Komputasi Semester Ganjil 2022/2023 Filkom UB
# Rencana Pembelajaran MK Matematika Komputasi Semester Ganjil 2022/2023 Kelas C
# Fakultas Ilmu Komputer (Filkom), Universitas Brawijaya (UB) 2022.

# Dosen Pengampu:
# 1. Imam Cholissodin, S.Si., M.Kom. | email: imamcs@ub.ac.id | Filkom UB

from flask import Flask,render_template, Response, redirect,url_for,session,request,jsonify
from flask import render_template_string
import sqlite3
from flask_cors import CORS

from flask import send_file
from flask_qrcode import QRcode

from io import BytesIO
import os

import io
import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
# from bokeh.util.string import encode_utf8

from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib_venn import venn3, venn3_circles

app = Flask(__name__, static_folder='static')
qrcode = QRcode(app)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "static/qr_app/db/qrdata.db"))

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
# import pyqrcode
import uuid

CORS(app, resources=r'/api/*')

app.secret_key = 'filkomub2223^&&*(&^(filkom#BJH#G#VB#MatKom99nDataPyICS_ap938255bnUB'

# keterangan:
# "#" adalah untuk comment
# <br> adalah new line
# &nbsp; adalah spasi
# <!-- --> atau <!--- ---> adalah untuk comment

# FrameWeb_atas & FrameWeb_bawah untuk dekorasi web
# agar menjadi Web yang Responsif

FrameWeb_atas = """
{% extends "extends/base.html" %}
{% block title %}
    <title>Web App MatKom Dgn Python</title>
{% endblock title %}
{{ self.title() }}
    Home
{{ self.title() }}
<button onclick="window.location.href='/'" class="btn btn-outline btn-rounded btn-info">
    <i class="ti-arrow-left m-l-5"></i>
    <span>Back Home</span>
</button> Project 1

{{ self.title() }}
    Project 1

{% block content %}
"""
A_a = FrameWeb_atas

FrameWeb_bawah = """
{% endblock content %}
"""
Z_z = FrameWeb_bawah

# @app.route('/')
# def hello_matkom():
#     return 'Hello Students | Koding Matematika Komputasi (MatKom) pada Teknologi Cloud :D'

@app.route('/contoh_exp_matrix', methods=['POST', 'GET'])
def contoh_exp_matrix():

    template_view = '''
            <script type="text/javascript" src="{{ url_for('static', filename = 'js/jquery.min.js') }}"></script>
            <div class="row">
                    <div class="col-md-6">
                        <div class="white-box">
                            <h3 class="box-title m-b-0">Penghitungan Exponential Matriks: </h3>
                            <p class="text-muted m-b-30 font-13"> detail nilai elemen matriks Anda </p>
                            <form action="/contoh_exp_matrix" method="post" class="form-horizontal">
                                <div class="form-group">
                                    <p class="text-muted">Ukuran Matrik:</p>
                                        <div class="col-md-2">
                                        <input type="text" name="var1" {% if var1 is defined and var1 %} value="{{var1}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Baris" required="required">
                                        </div>
                                        <div class="col-md-2">
                                            <div class="input-group">
                                                <input type="text" name="var2" {% if var2 is defined and var2 %} value="{{var2}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Kolom" required="required">
                                            </div>
                                        </div>
                                </div>
                                <div class="form-group">
                                    <p class="text-muted">Matrik A:</p>
                                    <div class="table-responsive">
                                        <table class="table color-bordered-table info-bordered-table">
                                            <thead>
                                                <tr>
                                                    <th>#</th>
                                                    <th>Kolom 1</th>
                                                    <th>Kolom 2</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                    <td>Baris 1</td>
                                                    <td>7</td>
                                                    <td>4</td>
                                                </tr>
                                                <tr>
                                                    <td>Baris 2</td>
                                                    <td>-2</td>
                                                    <td>1</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <p class="text-muted">Matrik D:</p>
                                    <div class="table-responsive">
                                        <table class="table color-bordered-table info-bordered-table">
                                            <thead>
                                                <tr>
                                                    <th>#</th>
                                                    <th>Kolom 1</th>
                                                    <th>Kolom 2</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                    <td>Baris 1</td>
                                                    <td>{% if d_in is defined and d_in %} {{d_in[0][0]}} {% endif %}</td>
                                                    <td>{% if d_in is defined and d_in %} {{d_in[0][1]}} {% endif %}</td>
                                                </tr>
                                                <tr>
                                                    <td>Baris 2</td>
                                                    <td>{% if d_in is defined and d_in %} {{d_in[1][0]}} {% endif %}</td>
                                                    <td>{% if d_in is defined and d_in %} {{d_in[1][1]}} {% endif %}</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <p class="text-muted">Matrik P:</p>
                                    <div class="table-responsive">
                                        <table class="table color-bordered-table info-bordered-table">
                                            <thead>
                                                <tr>
                                                    <th>#</th>
                                                    <th>Kolom 1</th>
                                                    <th>Kolom 2</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                    <td>Baris 1</td>
                                                    <td>{% if p_in is defined and p_in %} {{p_in[0][0]}} {% endif %}</td>
                                                    <td>{% if p_in is defined and p_in %} {{p_in[0][1]}} {% endif %}</td>
                                                </tr>
                                                <tr>
                                                    <td>Baris 2</td>
                                                    <td>{% if p_in is defined and p_in %} {{p_in[1][0]}} {% endif %}</td>
                                                    <td>{% if p_in is defined and p_in %} {{p_in[1][1]}} {% endif %}</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <p class="text-muted">Matrik P invers:</p>
                                    <div class="table-responsive">
                                        <table class="table color-bordered-table info-bordered-table">
                                            <thead>
                                                <tr>
                                                    <th>#</th>
                                                    <th>Kolom 1</th>
                                                    <th>Kolom 2</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                    <td>Baris 1</td>
                                                    <td>{% if inv_p_in is defined and inv_p_in %} {{inv_p_in[0][0]}} {% endif %}</td>
                                                    <td>{% if inv_p_in is defined and inv_p_in %} {{inv_p_in[0][1]}} {% endif %}</td>
                                                </tr>
                                                <tr>
                                                    <td>Baris 2</td>
                                                    <td>{% if inv_p_in is defined and inv_p_in %} {{inv_p_in[1][0]}} {% endif %}</td>
                                                    <td>{% if inv_p_in is defined and inv_p_in %} {{inv_p_in[1][1]}} {% endif %}</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>

                                <div class="form-group m-b-0">
                                    <div class="col-sm-offset-3 col-sm-9 text-right">
                                        <button type="submit" class="btn btn-info waves-effect waves-light m-t-10">Hitung Hasil</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="white-box">
                            <h3 class="box-title m-b-0">Hasil Exponential Matriksnya exp(A) adalah</h3>
                            {% if c_save_a is defined and c_save_a %}
                            <p class="text-muted m-b-30 font-13"> A = P*D*inv(P) = {{c_save_a_hitung}} </p>
                            {% endif %}
                            <div class="mt-8">
                                {% if var1 is defined and var1 %}
                                <p>Ukuran Matriks: {{var1}} x {{var2}}</p>
                                {% endif %}
                            </div>

                            <div class="table-responsive">
                                <table class="table color-bordered-table info-bordered-table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Kolom 1</th>
                                            <th>Kolom 2</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                            <tr>
                                                <td>Baris 1</td>
                                                <td>{% if exp_a_in is defined and exp_a_in %} {{'%0.4f'|format(exp_a_in[0][0]|float)}} {% endif %}</td>
                                                <td>{% if exp_a_in is defined and exp_a_in %} {{'%0.4f'|format(exp_a_in[0][1]|float)}} {% endif %}</td>
                                            </tr>
                                            <tr>
                                                <td>Baris 2</td>
                                                <td>{% if exp_a_in is defined and exp_a_in %} {{'%0.4f'|format(exp_a_in[1][0]|float)}} {% endif %}</td>
                                                <td>{% if exp_a_in is defined and exp_a_in %} {{'%0.4f'|format(exp_a_in[1][1]|float)}} {% endif %}</td>
                                            </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <div class="white-box">
                            <h3 class="box-title m-b-0">Hasil ln Matriks A atau ln(A) adalah</h3>

                            <div class="table-responsive">
                                <table class="table color-bordered-table info-bordered-table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Kolom 1</th>
                                            <th>Kolom 2</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                            <tr>
                                                <td>Baris 1</td>
                                                <td>{% if ln_a_in is defined and ln_a_in %} {{'%0.4f'|format(ln_a_in[0][0]|float)}} {% endif %}</td>
                                                <td>{% if ln_a_in is defined and ln_a_in %} {{'%0.4f'|format(ln_a_in[0][1]|float)}} {% endif %}</td>
                                            </tr>
                                            <tr>
                                                <td>Baris 2</td>
                                                <td>{% if ln_a_in is defined and ln_a_in %} {{'%0.4f'|format(ln_a_in[1][0]|float)}} {% endif %}</td>
                                                <td>{% if ln_a_in is defined and ln_a_in %} {{'%0.4f'|format(ln_a_in[1][1]|float)}} {% endif %}</td>
                                            </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <div class="white-box">
                            <h3 class="box-title m-b-0">Hasil akar Matriks A atau sqrt(A) Type 1 atau Cara 1 adalah</h3>

                            <div class="table-responsive">
                                <table class="table color-bordered-table info-bordered-table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Kolom 1</th>
                                            <th>Kolom 2</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                            <tr>
                                                <td>Baris 1</td>
                                                <td>{% if sqrt_a_in is defined and sqrt_a_in %} {{'%0.4f'|format(sqrt_a_in[0][0]|float)}} {% endif %}</td>
                                                <td>{% if sqrt_a_in is defined and sqrt_a_in %} {{'%0.4f'|format(sqrt_a_in[0][1]|float)}} {% endif %}</td>
                                            </tr>
                                            <tr>
                                                <td>Baris 2</td>
                                                <td>{% if sqrt_a_in is defined and sqrt_a_in %} {{'%0.4f'|format(sqrt_a_in[1][0]|float)}} {% endif %}</td>
                                                <td>{% if sqrt_a_in is defined and sqrt_a_in %} {{'%0.4f'|format(sqrt_a_in[1][1]|float)}} {% endif %}</td>
                                            </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>


                        <div class="white-box">
                            <h3 class="box-title m-b-0">Hasil akar Matriks A atau sqrt(A) Type 2 atau Cara 2 adalah</h3>

                            <div class="table-responsive">
                                <table class="table color-bordered-table info-bordered-table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Kolom 1</th>
                                            <th>Kolom 2</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                            <tr>
                                                <td>Baris 1</td>
                                                <td>{% if sqrt_a_type_2_in is defined and sqrt_a_type_2_in %} {{'%0.4f'|format(sqrt_a_type_2_in[0][0]|float)}} {% endif %}</td>
                                                <td>{% if sqrt_a_type_2_in is defined and sqrt_a_type_2_in %} {{'%0.4f'|format(sqrt_a_type_2_in[0][1]|float)}} {% endif %}</td>
                                            </tr>
                                            <tr>
                                                <td>Baris 2</td>
                                                <td>{% if sqrt_a_type_2_in is defined and sqrt_a_type_2_in %} {{'%0.4f'|format(sqrt_a_type_2_in[1][0]|float)}} {% endif %}</td>
                                                <td>{% if sqrt_a_type_2_in is defined and sqrt_a_type_2_in %} {{'%0.4f'|format(sqrt_a_type_2_in[1][1]|float)}} {% endif %}</td>
                                            </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <div class="white-box">
                            <h3 class="box-title m-b-0">Hasil invers Matriks A atau inv(A) dengan Library dari numpy adalah</h3>

                            <div class="table-responsive">
                                <table class="table color-bordered-table info-bordered-table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Kolom 1</th>
                                            <th>Kolom 2</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                            <tr>
                                                <td>Baris 1</td>
                                                <td>{% if inv_a_by_lib_in is defined and inv_a_by_lib_in %} {{'%0.4f'|format(inv_a_by_lib_in[0][0]|float)}} {% endif %}</td>
                                                <td>{% if inv_a_by_lib_in is defined and inv_a_by_lib_in %} {{'%0.4f'|format(inv_a_by_lib_in[0][1]|float)}} {% endif %}</td>
                                            </tr>
                                            <tr>
                                                <td>Baris 2</td>
                                                <td>{% if inv_a_by_lib_in is defined and inv_a_by_lib_in %} {{'%0.4f'|format(inv_a_by_lib_in[1][0]|float)}} {% endif %}</td>
                                                <td>{% if inv_a_by_lib_in is defined and inv_a_by_lib_in %} {{'%0.4f'|format(inv_a_by_lib_in[1][1]|float)}} {% endif %}</td>
                                            </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <div class="white-box">
                            <h3 class="box-title m-b-0">Hasil invers Matriks A atau inv(A) dengan kaidah Exp(-1*ln(A)) adalah</h3>

                            <div class="table-responsive">
                                <table class="table color-bordered-table info-bordered-table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Kolom 1</th>
                                            <th>Kolom 2</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                            <tr>
                                                <td>Baris 1</td>
                                                <td>{% if inv_a_by_exp_in is defined and inv_a_by_exp_in %} {{'%0.4f'|format(inv_a_by_exp_in[0][0]|float)}} {% endif %}</td>
                                                <td>{% if inv_a_by_exp_in is defined and inv_a_by_exp_in %} {{'%0.4f'|format(inv_a_by_exp_in[0][1]|float)}} {% endif %}</td>
                                            </tr>
                                            <tr>
                                                <td>Baris 2</td>
                                                <td>{% if inv_a_by_exp_in is defined and inv_a_by_exp_in %} {{'%0.4f'|format(inv_a_by_exp_in[1][0]|float)}} {% endif %}</td>
                                                <td>{% if inv_a_by_exp_in is defined and inv_a_by_exp_in %} {{'%0.4f'|format(inv_a_by_exp_in[1][1]|float)}} {% endif %}</td>
                                            </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>

                </div>

                <!-- <div class="row white-box gx-0"> -->
                <!--     <div class="col-md-6"> -->
                <!--                 <img style="max-width:40%; margin: 0 auto;" class="img-responsive" src="{{ url_for('static', filename = 'img/filkom.png') }}" alt="logo-filkom">-->
                <!--     </div>-->
                <!--     <div class="col-md-6">-->
                <!--                 <img style="max-width:10%; margin: 0 auto;" class="img-responsive" src="{{ url_for('static', filename = 'img/conan.jpg') }}" alt="kartun-conan">-->
                <!--     </div>-->
                <!-- </div>-->

                <!-- <div class="row"> -->
                <!--     <div class="col-md-6"> -->
                <!--    <div class="white-box"> -->
                <!--                <img style="max-width:45%; margin: 0 auto;" class="img-responsive" src="{{ url_for('static', filename = 'img/filkom.png') }}" alt="logo-filkom">-->
                <!--    </div> -->
                <!--    </div> -->
                <!--    <div class="col-md-6">-->
                <!--    <div class="white-box"> -->
                <!--                <img style="max-width:10%; margin: 0 auto;" class="img-responsive" src="{{ url_for('static', filename = 'img/conan.png') }}" alt="kartun-conan">-->
                <!--    </div>-->
                <!-- </div>-->

                <!-- </div> -->

                <div class="row">
                    <div class="col-md-12">
                    <div class="white-box">
                                <img style="max-width:10%; margin: 0 auto;" class="img-responsive" src="{{ url_for('static', filename = 'img/filkom.png') }}" alt="logo-filkom">
                                <br>
                                <img style="max-width:10%; margin: 0 auto;" class="img-responsive" src="{{ url_for('static', filename = 'img/conan.png') }}" alt="kartun-conan">
                    </div>
                    </div>

                </div>
        '''

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /contoh_exp_matrix

        import numpy as np

        var1_in = request.form['var1']
        var2_in = request.form['var2']
        c = 2*float(var1_in)

        # matriks A
        A = np.array ([
            [7, 4],
            [-2, 1]
        ])

        # matriks D
        D = np.array ([
            [3, 0],
            [0, 5]
        ])

        # matriks P
        P = np.array ([
            [-1, -2],
            [1, 1]
        ])

        # matriks invers P
        inv_P = np.linalg.inv(P)

        # A = np.linalg.inv(np.transpose(X).dot(X)).dot(np.transpose(X)).dot(Y)
        A_hitung = P.dot(D).dot(inv_P)

        # matriks exp_D
        exp_D = np.array ([
            [np.exp(3), 0],
            [0, np.exp(5)]
        ])

        # hitung exp_A
        exp_A = P.dot(exp_D).dot(inv_P)

        # matriks ln_D
        ln_D = np.array ([
            [np.log(3), 0],
            [0, np.log(5)]
        ])

        ln_D_type_1 = np.array ([
            [np.exp(0.5*np.log(3)), 0],
            [0, np.exp(0.5*np.log(5))]
        ])


        sqrt_D = np.array ([
            [np.sqrt(3), 0],
            [0, np.sqrt(5)]
        ])

        # hitung ln A
        ln_A = P.dot(ln_D).dot(inv_P)

        # hitung sqrt cara 1
        sqrt_A = P.dot(ln_D_type_1).dot(inv_P)

        # hitung sqrt A cara 2
        sqrt_A_type_2 = P.dot(sqrt_D).dot(inv_P)

        # untuk hitung inv A dengan exp
        ln_D_utk_inv= np.array ([
            [np.exp(-1*np.log(3)), 0],
            [0, np.exp(-1*np.log(5))]
        ])

        # hitung hasil invers Matriks A atau inv(A) dengan library
        inv_A_by_lib = np.linalg.inv(A)

        # hitung Hasil invers Matriks A atau inv(A) dengan kaidah Exp(-1*ln(A))
        inv_A_by_exp = P.dot(ln_D_utk_inv).dot(inv_P)


        return render_template_string(A_a+template_view+Z_z, var1 = var1_in, var2 = var2_in, d_in = list(D), p_in = list(P), inv_p_in = list(inv_P),  exp_a_in = list(exp_A), ln_a_in = list(ln_A), sqrt_a_in = list(sqrt_A), sqrt_a_type_2_in = list(sqrt_A_type_2), inv_a_by_lib_in = list(inv_A_by_lib), inv_a_by_exp_in = list(inv_A_by_exp), c_save_a = list(A), c_save_a_hitung = A_hitung)

    else: # untuk yang 'GET' data awal untuk di send ke /contoh_exp_matrix
        return render_template_string(A_a+template_view+Z_z)

@app.route('/pbb/<m>/<n>')
def pbb(m,n):

    m_awal = int(m)
    n_awal = int(n)

    m = m_awal
    n = n_awal
    r_awal = m % n

    # Jika m = n*q + r,
    # maka PBB(m,n) = PBB(n,r)

    while n !=0:
        r = m % n
        m = n
        n = r

    # return "pbb siap dikomputasi"
    # return render_template_string(A_a+"pbb siap dikomputasi"+Z_z)
    # return render_template_string(A_a+"PBB("+str(m_awal)+","+str(n_awal)+") = "+str(m)+Z_z)
    return render_template_string(A_a+"PBB("+str(m_awal)+","+str(n_awal)+") = "+
    "PBB("+str(n_awal)+","+str(r_awal)+") = "
    +str(m)+Z_z)

@app.route('/prim/<dec>')
def prim(dec):
    n = int(dec)

    # cara ke-1
    # Wilson's theorem
    def fn_prim(n):
        return 1 + sum([
            math.floor(pow(n/sum([
                math.floor(pow(math.cos(math.pi * (math.factorial(j - 1) + 1)/j), 2))
                for j in range(1, i+1)
            ]), 1/n))
            for i in range(1, pow(2, n)+1)
        ])

    # # membuat looping hasil prima untuk cara ke-1
    # hasil = []
    # for i in range(n):
    #     hasil.append(fn_prim(i+1))

    # cara ke-2
    # Willans gave the formula
    def fn_prim2(n):
        return math.floor( ( math.factorial(n)%(n+1) ) /n )*(n-1) + 2

    # # membuat looping hasil prima untuk cara ke-2
    # hasil = []

    # num_search_prim = 1
    # flag = True
    # while(flag):
    #     hasil_init = fn_prim2(num_search_prim)
    #     if hasil_init not in hasil:
    #         hasil.append(hasil_init)

    #     if(len(hasil) == n):
    #         flag = False

    #     num_search_prim +=1

    # cara ke-3, by _
    # membuat looping hasil prima
    hasil = []

    num_search_prim = 1
    flag = True
    while(flag):
        # hasil_init = fn_prim2(num_search_prim)

        if(num_search_prim==1):
          hasil_init = 2
          hasil.append(hasil_init)

        else:
          sqrt_num_search_prim = int((num_search_prim+1)**0.5)
          filter_pembagi = filter(lambda x: x <= sqrt_num_search_prim, hasil)
          len_cek = len(list(filter(lambda x: x==0, map(lambda x: (num_search_prim + 1)%x, filter_pembagi))))

          # cek apakah ada yg membagi habis
          if len_cek ==0:
            # print('tidak ada yang membagi habis')
            hasil_init = num_search_prim + 1
            hasil.append(hasil_init)
          # else:
          #   print('ada yang membagi habis')

        if(len(hasil) == n):
            flag = False

        num_search_prim +=1

    return str(hasil)

@app.route('/fib/<dec>')
def fib(dec):
    # Basis		:  fib(0) = 0;  fib(1) = 1
    # Rekursif	:  fib(n) = fib(n – 1) + fib(n – 2)
    n = int(dec)

    # cara ke-1
    def fn_fib(n):
        if (n == 0 or n==1):
            return n
        else:
            return fn_fib(n-1) + fn_fib(n-2)

    # cara ke-2
    # def fn_fib(n):
    #     return int(((1+(5**0.5))**n - (1-(5**0.5))**n)/((2**n)*(5**0.5)))

    #cara ke-3
    # ref: https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series
    def fn_fib2(n):
        if n == 0:
            return (0, 1)
        else:
            a, b = fn_fib2(n // 2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if n % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)

    # membuat looping hasil fib
    hasil = []
    for i in range(n):
        hasil.append(fn_fib2(i)[0])

    return str(hasil)

# Start =============================
# 2.1 Pengantar Sistem Bilangan
# ===================================
@app.route('/code_2_1/<dec>')
def code_2_1(dec):

    # konversi "deca atau basis 10" ke "biner atau basis 2"
    # 19 (deca) => 10011 (biner)
    # dengan fungsi lambda
    binary = lambda n: '' if n==0 else binary(n//2) + str(n%2)
    hasil = str(binary(int(dec)))
    hasil = '0' if hasil == '' else hasil

    return hasil

#
# buatlah halaman post sekaligus get | Tipe 2
# untuk hitung hasil Dec2Bin
@app.route('/dec2bin_2', methods=["POST", "GET"])
def dec2bin_2():

    template_view_1 = '''
            <!--- <html> --->
            <!--- <head> --->
            <!--- </head> --->
            <!--- <body> --->
                  <form method="post">
                    Masukkan nilai (basis 10) = <input type="text" name="a" value="{{a_post}}" />
                    <input type="submit" value="Hitung Konversi basis 10 ke 2"/>
                  </form>
                  <h2>Hasil Dec2Bin = {{ hasil }} </h2>
            <!--- </body> --->
            <!--- </html> --->
        '''

    template_view_2 = '''
            <!--- <html> --->
            <!--- <head> --->
            <!--- </head> --->
            <!--- <body> --->
                  <form action="/dec2bin_2" method="post">
                    Masukkan nilai (basis 10) = <input type="text" name="a" value="" />
                    <input type="submit" value="Hitung Konversi basis 10 ke 2"/>
                  </form>
            <!--- </body> --->
            <!--- </html> --->
        '''

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /dec2bin_2

        dec = int(float(request.form['a']))

        # hitung hasil dec2Bin atau basis 10 ke basis 2
        # cara ke-1
        binary = lambda n: '' if n==0 else binary(n//2) + str(n%2)

        # cara ke-2
        def decToBin(n):
            if n==0:
                return ''
            else:
                return decToBin(n//2) + str(n%2)

        hasil = str(decToBin(int(dec)))
        hasil = '0' if hasil == '' else hasil

        return render_template_string(A_a+template_view_1+Z_z, a_post = dec, hasil = hasil)

    else: # untuk yang 'GET' data awal untuk di send ke /dec2bin_2
        return render_template_string(A_a+template_view_2+Z_z)

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

@app.route('/code_2_1_1')
def code_2_1_1():
    # konversi "deca atau basis 10" ke "biner atau basis 2"
    # dengan library numpy
    import numpy as np

    a = 10
    b = 4

    # <br> adalah new line

    return "a = " + str(a) + " (Basis 10) = " + str(np.binary_repr(a, width=8)) + " (Basis 2) <br>" + \
    "b = " + str(b) + " (Basis 10) = " + str(np.binary_repr(b, width=8)) + " (Basis 2)"

@app.route('/code_2_1_2')
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
    batas_generate = 18
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
              <h2>
                <!--- <p style="text-decoration: underline;"> --->
                <!---   Konversi Basis "10" | --->
                <!---   "2" | --->
                <!---   "8" | --->
                <!---   "16": --->
                <!--- </p> --->
                <p style="text-decoration: underline;">
                  Konversi Basis "10" |
                  "2" |
                  "8" |
                  "16":
                </p>
              </h2>
              <table border ="1">
                    <tr>
                      <td align = "center">&nbsp; Decimal ( base r=10 ) &nbsp;</td>
                      <td align = "center">&nbsp; Binary ( base r=2) &nbsp;</td>
                      <td align = "center">&nbsp; Octal ( base r=8 ) &nbsp;</td>
                      <td align = "center">&nbsp; Hexadecimal ( base r=16 ) &nbsp;</td>
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
        '''
    return render_template_string(A_a+template_view+Z_z, basis_all = zip(basis_10, basis_2, basis_8, basis_16))

@app.route('/code_2_1_2_2', methods=["POST", "GET"])
def code_2_1_2_2():
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

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /code_2_1_2_2
        # get nilai batas (a)
        dec = int(float(request.form['a']))+1

        # generate angka dengan basis 10
        batas_generate = dec
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
                  <form method="post">
                      <h2>
                        <!--- <p style="text-decoration: underline;"> --->
                        <!---   Konversi Basis "10" | --->
                        <!---   "2" | --->
                        <!---   "8" | --->
                        <!---   "16": --->
                        <!--- </p> --->
                        <p style="text-decoration: underline;">
                          Konversi Basis "10" |
                          "2" |
                          "8" |
                          "16":
                        </p>
                      </h2>
                      Masukkan Batas Generate Konversi = <input type="text" name="a" value="{{a_post}}" />
                      <input type="submit" value="Klik Run"/>
                      <br>
                      <table border ="1">
                            <tr>
                              <td align = "center">&nbsp; Decimal ( base r=10 ) &nbsp;</td>
                              <td align = "center">&nbsp; Binary ( base r=2) &nbsp;</td>
                              <td align = "center">&nbsp; Octal ( base r=8 ) &nbsp;</td>
                              <td align = "center">&nbsp; Hexadecimal ( base r=16 ) &nbsp;</td>
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
                  </form>
            '''
        return render_template_string(A_a+template_view+Z_z, a_post = dec-1, basis_all = zip(basis_10, basis_2, basis_8, basis_16))
    else: # untuk yang 'GET' data awal untuk di send ke /code_2_1_2_2
        template_view = '''
                  <form action="/code_2_1_2_2" method="post">
                      <h2>
                        <!--- <p style="text-decoration: underline;"> --->
                        <!---   Konversi Basis "10" | --->
                        <!---   "2" | --->
                        <!---   "8" | --->
                        <!---   "16": --->
                        <!--- </p> --->
                        <p style="text-decoration: underline;">
                          Konversi Basis "10" |
                          "2" |
                          "8" |
                          "16":
                        </p>
                      </h2>
                      Masukkan Batas Generate Konversi = <input type="text" name="a" value="{{a_post}}" />
                      <input type="submit" value="Klik Run"/>
                      <br>
                  </form>
            '''

        return render_template_string(A_a+template_view+Z_z)

# End =============================
# 2.1 Pengantar Sistem Bilangan
# ===================================

# Start =============================
# 2.2 Logika Proposisi
# ===================================

@app.route('/code_2_2_1')
def code_2_2_1():
    # mencoba operator logika "and", "or", "negation" & "xor"
    import numpy as np

    a = 10
    b = 4

    list_hasil = []
    list_hasil.append(str(a))
    list_hasil.append(str(np.binary_repr(a, width=8)))
    list_hasil.append(str(b))
    list_hasil.append(str(np.binary_repr(b, width=8)))
    list_hasil.append(str(np.binary_repr(a & b, width=8)))
    list_hasil.append(str(np.binary_repr(a | b, width=8)))
    list_hasil.append(str(np.binary_repr(~a, width=8)))
    list_hasil.append(str(np.binary_repr(a ^ b, width=8)))

    # &nbsp; adalah spasi

    template_view = '''
        <!--- <html> --->
        <!--- <head> --->
        <!--- </head> --->
        <!--- <body> --->

              <h2><p style="text-decoration: underline;">Mencoba Konversi Dec2Bin & Operasi logika: </p></h2>

              <table border ="1">

                    <tr>
                      <td align = "center">&nbsp; a = &nbsp;</td>
                      <td align = "center">&nbsp; {{ pro_utk_tabel[0] }} (Basis 10) = &nbsp; </td>
                      <td align = "center">&nbsp; {{ pro_utk_tabel[1] }} (Basis 2) &nbsp;</td>
                    </tr>
                    <tr>
                      <td align = "center">b =</td>
                      <td align = "center">{{ pro_utk_tabel[2] }} (Basis 10) = </td>
                      <td align = "center">{{ pro_utk_tabel[3] }} (Basis 2)</td>
                    </tr>

              </table>

              <br>

              <form method="post">
                <table border ="1">
                    <tr>
                      <td align = "center">&nbsp; Operasi AND &nbsp;</td>
                      <td align = "center">&nbsp; Operasi OR &nbsp;</td>
                      <td align = "center">&nbsp; Operasi NOT &nbsp;</td>
                      <td align = "center">&nbsp; Operasi XOR &nbsp;</td>
                    </tr>
                    <tr>
                      <td align = "center">&nbsp; {{ pro_utk_tabel[4] }} &nbsp;</td>
                      <td align = "center">&nbsp; {{ pro_utk_tabel[5] }} &nbsp;</td>
                      <td align = "center">&nbsp; {{ pro_utk_tabel[6] }} &nbsp;</td>
                      <td align = "center">&nbsp; {{ pro_utk_tabel[7] }} &nbsp;</td>
                    </tr>
                </table>

              </form>

            <!--- </body> --->
        <!--- </html> --->
        '''

    return render_template_string(A_a+template_view+Z_z, pro_utk_tabel = list_hasil)

@app.route('/code_2_2_2')
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
        <!--- <html> --->
        <!--- <head> --->
        <!--- </head> --->
        <!--- <body> --->

              <h2>
                <p style="text-decoration: underline;">
                  Mencoba membuat Tabel Kebenaran:
                </p>
              </h2>
              <table border ="1">
                    <tr>
                      <td align = "center">&nbsp; p &nbsp;</td>
                      <td align = "center">&nbsp; q &nbsp;</td>
                      <td align = "center">&nbsp; r &nbsp;</td>
                      <td align = "center">&nbsp; Si A ((~q)∧ r) &nbsp;</td>
                      <td align = "center">&nbsp; Si B ((~p) → (~r)) &nbsp;</td>
                      <td align = "center">&nbsp; Si C (r ∧ ((~p) ∨ (~q))) &nbsp;</td>
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

        <!--- </body> --->
        <!--- </html> --->
        '''

    return render_template_string(A_a+template_view+Z_z, pro_utk_tabel = zip(pro.decode().tolist(), pro_hasil_logic.decode().tolist()))

# End =============================
# 2.2 Logika Proposisi
# ===================================

# himpunan bagian
@app.route('/code_himpunan_bagian')
def code_himpunan_bagian():

    # Ref:
    # https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
    # fungsi untuk himpunan bagian
    def powerset(x):
        m=[]
        if not x:
            m.append(x)
        else:
            A = x[0]
            B = x[1:]
            for z in powerset(B):
                m.append(z)
                r = [A] + z
                m.append(r)
        return m
    # himpunan = [1, 2, 3, 4]

    # S = {a, d, m, i, n, t, e, s, l}
    # Coba Buat Himpunan Bagian dari S, sebanyak 2^ |S|
    himpunan = ['a', 'd', 'm', 'i', 'n', 't', 'e', 's', 'l']

    hasil = powerset(himpunan)

    template_view = '''
        <!--- <html> --->
        <!--- <head> --->
        <!--- </head> --->
        <!--- <body> --->

              <h2>
                <p style="text-decoration: underline;">
                  Mencoba membuat Himpunan Bagian dari:
                  [
                  {% for himpunan_get  in himpunan  %}
                    {{himpunan_get}}
                    {{ ", " if not loop.last else "" }}
                  {% endfor %}
                  ]
                </p>
              </h2>
              <table border ="1">
                    <tr>
                      <td align = "center">&nbsp; ke-i &nbsp;</td>
                      <td align = "center">&nbsp; Isi Subset &nbsp;</td>
                    </tr>
                    {% for subset_get  in hasil  %}
                    <tr>
                      <td align = "center">{{ loop.index }}</td>
                      <td align = "center">{{ subset_get }}</td>

                    </tr>
                    {% endfor %}
              </table>

        <!--- </body> --->
        <!--- </html> --->
        '''

    return render_template_string(A_a+template_view+Z_z, himpunan = himpunan, hasil = hasil)

@app.route('/code_plot_diagram_venn', methods=['GET'])
def code_plot_diagram_venn():

    import time
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    template_view = '''
            <!--- <html> --->
            <!--- <head> --->
            <!--- </head> --->
            <!--- <body> --->
            <h2>
                <p style="text-decoration: underline;">
                  Plot Diagram Venn (2 Himpunan dan 3 Himpunan):
                </p>
            </h2>
                  <form method="post">
                   {%for data_get in data_himpunan %}
                    Data Himpunan {{ loop.index }}: <br>
                    {{ data_get }}
                    <br><br>
                   {%endfor%}
                  </form>
                  <h2>Plot 2 Himpunan:  </h2>
                  <img src={{url_image2}} alt="Chart" height="480" width="640">
                  <br><br>
                  <h2>Plot 3 Himpunan:  </h2>
                  <img src={{url_image3}} alt="Chart" height="480" width="640">

                  <br><br>

                  <div class="row">
                    <!-- .col -->
                    <div class="col-sm-12">
                        <div class="white-box">
                            <h3 class="box-title m-b-0">Plot Diagram Venn dgn Animasi</h3>
                            <div id="image-popups" class="row">
                                <div class="col-sm-2">
                                    <a href={{url_image2}} data-effect="mfp-zoom-in"><img src={{url_image2}} class="img-responsive">
                                        <br>Plot 2 Himpunan</a>
                                </div>
                                <div class="col-sm-2">
                                    <a href={{url_image3}} data-effect="mfp-newspaper"><img src={{url_image3}} class="img-responsive">
                                        <br>Plot 3 Himpunan</a>
                                </div>

                            </div>
                        </div>
                    </div>
                    <!-- .col -->
                </div>

            <!--- </body> --->
            <!--- </html> --->
        '''


    # contoh membuat set elemen anggota himpunan
    Himpunan_1 = ['A','I','U','E','O']
    Himpunan_2 = ['F','I','L','K','O','M','U','B','2','0','2','2']
    Himpunan_3 = ['M','A','T','K','O','M']



    # Cara plot
    # ---------------
    # simpan dalam path + nama file /static/img/diagram_venn2.png
    url_simpan2 = "static/img/diagram_venn2.png"

    # simpan dalam path + nama file /static/img/diagram_venn3.png
    url_simpan3 = "static/img/diagram_venn3.png"

    # fig = plt.figure()
    # Contoh untuk visualiasi 2 set himpunan
    # Misal membuat Diagram Venn yang terdiri dari 2 groups himpunan, menggunakan sintaks venn2.
    # dengan dibuat ukuran shape-nya sama
    # dimana r = red, g = green, b = blue, alpha menyatakan nilai rasion transparansi
    c2 = venn2_unweighted(subsets = (12, 5, 2), set_labels = ('Himpunan A', 'Himpunan B'), set_colors=('g', 'b'), alpha = 0.5);

    plt.show()

    url_file_image_simpan2 = os.path.join(BASE_DIR, url_simpan2)
    plt.savefig(url_file_image_simpan2)
    plt.close()


    # reopen plt untuk visualiasi 3 set himpunan
    plt.figure()

    # Contoh untuk visualiasi 3 set himpunan
    vd3=venn3([set(Himpunan_1),set(Himpunan_2),set(Himpunan_3)], set_labels=('Himpunan 1', 'Himpunan 2','Himpunan 3'), set_colors=('#c4e6ff', '#F4ACB7','#9D8189'), alpha = 0.8)

    c3=venn3_circles([set(Himpunan_1), set(Himpunan_2),set(Himpunan_3)], linestyle='-.', linewidth=2, color='grey')
    for text in vd3.set_labels:
        text.set_fontsize(16);
    for text in vd3.subset_labels:
        text.set_fontsize(16)

    plt.title('Venn Diagram untuk 3 Himpunan',fontname='DejaVu Sans',fontweight='bold',fontsize=20, pad=15,backgroundcolor='#cbe7e3',color='black',style='italic');

    c3[0].set_lw(7.0)
    c3[0].set_ls(':')
    c3[0].set_color('#c4e6ff')
    plt.show()

    url_file_image_simpan3 = os.path.join(BASE_DIR, url_simpan3)
    plt.savefig(url_file_image_simpan3)
    plt.close()


    data_himpunan = []
    data_himpunan.append("[\'"+"' , '".join([x for x in Himpunan_1])+"\']")
    data_himpunan.append("[\'"+"' , '".join([x for x in Himpunan_2])+"\']")
    data_himpunan.append("[\'"+"' , '".join([x for x in Himpunan_3])+"\']")


    # return hasil
    return render_template_string(A_a+template_view+Z_z, data_himpunan = data_himpunan, url_image2 = url_simpan2, url_image3 = url_simpan3)

@app.route('/db/<aksi>')
def manipulate_tabel(aksi):
    conn = connect_db()
    db = conn.cursor()

    # Aksi => Buat, Hapus

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
    # return redirect(url_for("login"))
    return render_template("index.html")

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
          return redirect(url_for("launchpad_menu"))
      else:
          msg = "Masukkan Username (Email) dan Password dgn Benar!"

  return render_template("login.html", msg = msg)

@app.route("/register", methods=["GET", "POST"])
def register():
  conn = connect_db()
  # db = conn.cursor()
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

def connect_db_to_vacuum():
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data.db")

    return sqlite3.connect(db_path,isolation_level=None)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.errorhandler(500)
def internal_server_error(error):
    userhome = os.path.expanduser("~").split("/")[-1]
    link_error_debug = "https://www.pythonanywhere.com/user/"+userhome+"/files/var/log/"+userhome+".pythonanywhere.com.error.log"

    return render_template("500.html", link_error_debug = link_error_debug)

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

# @user.route('/<userId>/')  # NEED '/' AFTER LINK
# @user.route('/<userId>/<username>')
# def show(userId, username=None):
#     pass

# @user.route('/<user_id>', defaults={'username': default_value})
# @user.route('/<user_id>/<username>')
# def show(user_id, username):
#   #
#   pass

@app.route('/myadmin/', methods = ['GET','POST'])
@app.route('/myadmin/<none_atau_lainnya>', methods = ['GET','POST'])
def myadmin(none_atau_lainnya=None):

    template_view = '''
                <div class="row">
                    <div class="col-12">
                        <div class="white-box">
                                <div class="card-body">
                                    <form action="/myadmin" method="post">
                                    <h4 class="card-title">Masukkan tabel yang akan dibuat</h4>
                                    <h6 class="card-subtitle"></h6>
                                    <button type="button" class="btn btn-info btn-rounded m-t-10 float-right" data-toggle="modal" data-target="#add-contact">Buat Tabel</button>

                                    <!-- Add Contact Popup Model -->
                                    <!--<div id="add-contact" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;"> -->
                                    <div id="add-contact" class="modal fade in" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                                        <div class="modal-dialog">
                                            <div class="modal-content">
                                                <div class="modal-header">
                                                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                                                    <h4 class="modal-title" id="myModalLabel">Buat Tabel baru</h4> </div>
                                                <div class="modal-body">
                                                    <from class="form-horizontal form-material">
                                                        <div class="form-group">
                                                            <div class="col-md-12 m-b-20">
                                                                <input type="text" name="nama_tabel" class="form-control" placeholder="Nama tabel" required="required"> </div>
                                                            <div class="col-md-12 m-b-20">
                                                                <textarea class="form-control" name="teks_sintaks" rows="4" placeholder="Teks sintaks"></textarea> </div>
                                                        </div>
                                                    </from>
                                                </div>
                                                <div class="modal-footer">
                                                    <button type="submit" class="btn btn-info waves-effect">Simpan</button>
                                                    <button type="button" class="btn btn-default waves-effect" data-dismiss="modal">Batal</button>
                                                    <!-- <button type="reset" class="btn btn-default waves-effect" data-dismiss="modal">Batal</button> -->
                                                </div>
                                            </div>
                                            <!-- /.modal-content -->
                                        </div>
                                        <!-- /.modal-dialog -->
                                    </div>

                                    </form>

                                    <div class="table-responsive">
                                        <!-- <table id="footable-addrow" class="table table-bordered m-t-30 table-hover contact-list footable footable-5 footable-paging footable-paging-center breakpoint-lg" data-paging="true" data-paging-size="7" style=""> -->
                                        <!-- <table id="footable-addrow" class="table footable footable-6 footable-editing footable-editing-right footable-editing-no-view footable-filtering footable-filtering-right footable-paging footable-paging-center breakpoint-lg" data-paging="true" data-filtering="true" data-sorting="true" data-editing="true" data-state="true" style=""> -->
                                        <!-- <table id="example23" class="display nowrap table table-hover table-striped table-bordered" cellspacing="0" width="100%"> -->
                                        <!-- <table id="footable-addrow" class="table" data-paging="true" data-filtering="true" data-sorting="true" data-editing="true" data-state="true">-->

                                        <!-- <table id="example23" class="display nowrap table table-hover table-striped table-bordered" data-paging="true" data-filtering="true" data-sorting="true" data-editing="true" data-state="true">-->
                                        <table id="example23" class="display nowrap table table-hover table-striped table-bordered" cellspacing="0" width="100%">
                                        <!-- <table id="myTable" class="table table-striped"> -->
                                            <thead>
                                                <tr class="footable-header">
                                                    <th style="display: table-cell;" class="footable-first-visible">No</th>
                                                    <th style="display: table-cell;">Nama</th>
                                                    <th style="display: table-cell;">Tanggal Pembuatan</th>
                                                    <th style="display: table-cell;" class="th-inner">Teks Sintaks</th>
                                                    <th style="display: table-cell;" class="footable-last-visible"></th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {% for item in var_tabel_myadmin %}
                                                <tr class={{ loop.cycle('odd', 'even') }}>
                                                    <td style="display: table-cell;" class="footable-first-visible">{{ loop.index }}</td>
                                                    <td style="display: table-cell;">{{item[1]}}</td>
                                                    <td style="display: table-cell;">{{item[2]}}</td>
                                                    <td style="display: table-cell;">
                                                        {{item[3]}} </td>
                                                    <td style="display: table-cell;" class="footable-last-visible">

                                                        <a href="" data-toggle="modal" data-target="#editor-modal{{item[1]}}">
                                                        <button type="button" class="btn btn-info btn-outline btn-circle btn-lg m-r-5"><i class="ti-pencil-alt"></i></button></a>

                                                        <!-- <a href="/myadmin/edit-nama_tabel_var-{{item[1]}}"> -->
                                                        <!-- <button type="button" class="btn btn-info btn-outline btn-circle btn-lg m-r-5"><i class="ti-pencil-alt"></i></button></a> -->

                                                        <!-- <a href="/myadmin/del-nama_tabel_var-{{item[1]}}"> -->
                                                        <!-- <button type="button" class="btn btn-info btn-outline btn-circle btn-lg m-r-5"><i class="ti-trash"></i></button></a> -->

                                                        <a href="" data-toggle="modal" data-target="#hapus-modal{{item[1]}}">
                                                        <button type="button" class="btn btn-info btn-outline btn-circle btn-lg m-r-5"><i class="ti-trash"></i></button></a>


                                                        <a href="/myadmin/run-nama_tabel_var-{{item[1]}}">
                                                        <button type="button" class="btn btn-info btn-outline btn-circle btn-lg m-r-5"><i class="ti-control-play"></i></button></a>

                                                        <!-- Start Popup Model utk Edit -->
                                                        <!-- <div class="modal fade" id="editor-modal" tabindex="-1" role="dialog" aria-labelledby="editor-title"> -->
                                                        <!-- <div id="editor-modal{{item[1]}}" class="modal fade in" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> -->
                                                        <div class="modal fade in" id="editor-modal{{item[1]}}" tabindex="-1" role="dialog" aria-labelledby="editor-title">
                                                            <!--<div class="modal-dialog" role="document"> -->
                                                            <div class="modal-dialog">
                                                                <form action="/myadmin/edit-nama_tabel_var-{{item[1]}}" class="modal-content form-horizontal" id="editor" method="post">
                                                                    <div class="modal-content">
                                                                        <div class="modal-header">
                                                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                                                                            <h4 class="modal-title" id="editor-title">Ubah Data ke-{{item[0]}}</h4>
                                                                        </div>
                                                                        <div class="modal-body">
                                                                            <from class="form-horizontal form-material">
                                                                                <div class="form-group">
                                                                                    <label for="firstName" class="col-sm-3 control-label">Nama</label>
                                                                                    <div class="col-sm-9">
                                                                                        <input type="text" class="form-control" name="nama_tabel_edit_{{item[1]}}" value="{{item[1]}}" placeholder="Nama Tabel" readonly>
                                                                                    </div>
                                                                                </div>
                                                                                <!-- <div class="form-group"> -->
                                                                                    <!-- <label for="dob" class="col-sm-3 control-label">Tanggal Pembuatan</label> -->
                                                                                    <!-- <label class="col-sm-3 control-label">Tanggal Pembuatan</label> -->
                                                                                    <!-- <div class="col-sm-9"> -->
                                                                                        <!-- <input type="date" class="form-control" name="tgl_buat_tabel_edit" value="{{item[2]}}" placeholder="Tanggal Pembuatan Tabel"> -->
                                                                                        <!-- <input type="date" data-date="" data-date-format="dd-mm-YYYY HH:MM:SS" class="form-control" name="tgl_buat_tabel_edit" value="{{item[2]}}" placeholder="Tanggal Pembuatan Tabel"> -->

                                                                                    <!-- </div> -->
                                                                                <!-- </div> -->
                                                                                <div class="form-group">
                                                                                    <label for="status" class="col-sm-3 control-label">Sintaks</label>
                                                                                    <div class="col-sm-9">
                                                                                        <!--input type="text" class="form-control" id="status" name="status" placeholder="Status Here" required> -->
                                                                                        <textarea class="form-control" name="teks_sintaks_edit_{{item[1]}}" rows="4" placeholder="Teks sintaks">{{item[3]}}</textarea>
                                                                                    </div>
                                                                                </div>
                                                                            </from>
                                                                        </div>
                                                                        <div class="modal-footer">
                                                                            <!-- <button type="submit" class="btn btn-primary">Save changes</button> -->
                                                                            <!-- <a href="/myadmin/edit-nama_tabel_var-{{item[1]}}" class="btn btn-info" role="button">Simpan</a>-->
                                                                            <!-- <button type="submit" class="btn btn-primary">Simpan</button>-->
                                                                            <button type="submit" class="btn btn-info waves-effect">Simpan</button>
                                                                            <button type="button" class="btn btn-default" data-dismiss="modal">Batal</button>
                                                                        </div>
                                                                    </div>
                                                                    <!-- /.modal-content -->
                                                                </form>
                                                            </div>
                                                            <!-- /.modal-dialog -->
                                                        </div>
                                                        <!-- End Popup Model utk Edit -->

                                                        <!-- Start Popup Model utk Hapus -->
                                                        <div class="modal fade in" id="hapus-modal{{item[1]}}" tabindex="-1" role="dialog" aria-labelledby="editor-title">
                                                            <div class="modal-dialog">
                                                                <form action="/myadmin/del-nama_tabel_var-{{item[1]}}" class="modal-content form-horizontal" id="editor" method="post">
                                                                    <div class="modal-content">
                                                                        <div class="modal-header">
                                                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                                                                            <h4 class="modal-title" id="editor-title">Hapus Data ke-{{item[0]}}</h4>
                                                                        </div>
                                                                        <div class="modal-body">
                                                                            <from class="form-horizontal form-material">
                                                                                <div class="form-group">
                                                                                    <label for="firstName" class="col-sm-3 control-label">Nama</label>
                                                                                    <div class="col-sm-9">
                                                                                        <input type="text" class="form-control" name="nama_tabel_hapus_{{item[1]}}" value="{{item[1]}}" placeholder="Nama Tabel" readonly>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="form-group">
                                                                                    <label for="status" class="col-sm-3 control-label">Sintaks</label>
                                                                                    <div class="col-sm-9">
                                                                                        <!--input type="text" class="form-control" id="status" name="status" placeholder="Status Here" required> -->
                                                                                        <textarea class="form-control" name="teks_sintaks_hapus_{{item[1]}}" rows="4" placeholder="Teks sintaks">{{item[3]}}</textarea>
                                                                                    </div>
                                                                                </div>
                                                                            </from>
                                                                        </div>
                                                                        <div class="modal-footer">
                                                                            <button type="submit" class="btn btn-info waves-effect">Hapus</button>
                                                                            <button type="button" class="btn btn-default" data-dismiss="modal">Batal</button>
                                                                        </div>
                                                                    </div>
                                                                    <!-- /.modal-content -->
                                                                </form>
                                                            </div>
                                                            <!-- /.modal-dialog -->
                                                        </div>
                                                        <!-- End Popup Model utk Hapus -->

                                                        <!-- Start Popup Model utk Generate Kode untuk flask_app.py -->
                                                        <div class="modal fade in" id="gen-modal{{item[1]}}" tabindex="-1" role="dialog" aria-labelledby="editor-title">
                                                            <div class="modal-dialog">
                                                                <form action="/myadmin/gen-nama_tabel_var-{{item[1]}}" class="modal-content form-horizontal" id="editor" method="post">
                                                                    <div class="modal-content">
                                                                        <div class="modal-header">
                                                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                                                                            <h4 class="modal-title" id="editor-title">Hapus Data ke-{{item[0]}}</h4>
                                                                        </div>
                                                                        <div class="modal-body">
                                                                            <from class="form-horizontal form-material">
                                                                                <div class="form-group">
                                                                                    <label for="firstName" class="col-sm-3 control-label">Nama</label>
                                                                                    <div class="col-sm-9">
                                                                                        <input type="text" class="form-control" name="nama_tabel_gen_{{item[1]}}" value="{{item[1]}}" placeholder="Nama Tabel" readonly>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="form-group">
                                                                                    <label for="status" class="col-sm-3 control-label">Sintaks</label>
                                                                                    <div class="col-sm-9">
                                                                                        <!--input type="text" class="form-control" id="status" name="status" placeholder="Status Here" required> -->
                                                                                        <textarea class="form-control" name="teks_sintaks_tabel_gen_{{item[1]}}" rows="4" placeholder="Teks sintaks">{{item[3]}}</textarea>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="form-group">
                                                                                    <label for="status" class="col-sm-3 control-label">Generate Kode untuk flask_app.py</label>
                                                                                    <div class="col-sm-9">
                                                                                        <!--input type="text" class="form-control" id="status" name="status" placeholder="Status Here" required> -->
                                                                                        <textarea class="form-control" name="teks_sintaks_page_gen_{{item[1]}}" rows="4" placeholder="Teks sintaks">{{item[3]}}</textarea>
                                                                                    </div>
                                                                                </div>
                                                                            </from>
                                                                        </div>
                                                                        <div class="modal-footer">
                                                                            <button type="submit" class="btn btn-info waves-effect">Hapus</button>
                                                                            <button type="button" class="btn btn-default" data-dismiss="modal">Batal</button>
                                                                        </div>
                                                                    </div>
                                                                    <!-- /.modal-content -->
                                                                </form>
                                                            </div>
                                                            <!-- /.modal-dialog -->
                                                        </div>
                                                        <!-- End Popup Model utk utk Generate Kode untuk flask_app.py -->

                                                    </td>
                                                </tr>
                                                {% endfor %}
                                            </tbody>
                                        </table>
                                    </div>
                                    <!-- </form> -->
                                </div>
                            </div>



                    </div>
                </div>



                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/footable.min.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/custom.min.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/footable-init.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/jQuery.style.switcher.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/jquery.min.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/bootstrap.min.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/jquery.slimscroll.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/moment.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/sidebar-nav.min.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/waves.js') }}"></script>-->

                <!-- There could be multiple reasons for this error. -->
                    <!-- jQuery DataTables library is missing. -->
                    <!-- jQuery library is loaded after jQuery DataTables. -->
                    <!-- Multiple versions of jQuery library is loaded. -->


                <!-- ./wrapper -->
                <!-- REQUIRED SCRIPTS -->
                <!-- jQuery -->
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/jquery.min.js.download') }}"></script>
                <!-- Bootstrap 4 -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/bootstrap.bundle.min.js.download') }}"></script> -->
                <!-- AdminLTE App -->
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/adminlte.min.js.download') }}"></script>
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/sweetalert2-9.10.12.min.js.download') }}"></script>
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/site.js.download') }}"></script>


                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/jquery.validate.min.js.download') }}"></script>
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/jquery.validate.unobtrusive.min.js.download') }}"></script>
                <!-- <script> -->
                <!--$("#main_form").validate(); -->
                <!-- </script> -->

                <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename = 'css/css_tabel_suhu/dataTables.bootstrap4.min.css') }}" />
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/jquery.dataTables.min.js.download') }}"></script>
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/dataTables.bootstrap4.min.js.download') }}"></script>


                <!-- /#wrapper -->

                <!-- Bootstrap Core JavaScript -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/bootstrap.min.js') }}"></script> -->
                <!-- Menu Plugin JavaScript -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/sidebar-nav.min.js') }}"></script> -->
                <!--slimscroll JavaScript -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/jquery.slimscroll.js') }}"></script> -->
                <!--Wave Effects -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/waves.js') }}"></script> -->
                <!-- Custom Theme JavaScript -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/custom.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/datatables.min.js') }}"></script> -->
                <!-- start - This is for export functionality only -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/dataTables.buttons.min.js') }}"></script> -->
                <!-- jQuery -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/jquery.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/buttons.flash.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/jszip.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/pdfmake.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/vfs_fonts.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/buttons.html5.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/buttons.print.min.js') }}"></script> -->
                <!-- end - This is for export functionality only -->




                <script>
                    /*
                    $(document).ready(function() {
                        $('#myTable').DataTable();
                        $(document).ready(function() {
                            var table = $('#example').DataTable({
                                "columnDefs": [{
                                    "visible": false,
                                    "targets": 2
                                }],
                                "order": [
                                    [2, 'asc']
                                ],
                                "displayLength": 25,
                                "drawCallback": function(settings) {
                                    var api = this.api();
                                    var rows = api.rows({
                                        page: 'current'
                                    }).nodes();
                                    var last = null;
                                    api.column(2, {
                                        page: 'current'
                                    }).data().each(function(group, i) {
                                        if (last !== group) {
                                            $(rows).eq(i).before('<tr class="group"><td colspan="5">' + group + '</td></tr>');
                                            last = group;
                                        }
                                    });
                                }
                            });
                            // Order by the grouping
                            $('#example tbody').on('click', 'tr.group', function() {
                                var currentOrder = table.order()[0];
                                if (currentOrder[0] === 2 && currentOrder[1] === 'asc') {
                                    table.order([2, 'desc']).draw();
                                } else {
                                    table.order([2, 'asc']).draw();
                                }
                            });
                        });
                    }); */
                    $('#example23').DataTable({
                        dom: 'Bfrtip',
                        buttons: [
                            'copy', 'csv', 'excel', 'pdf', 'print'
                        ]
                    });
                    $('.buttons-copy, .buttons-csv, .buttons-print, .buttons-pdf, .buttons-excel').addClass('btn btn-primary m-r-10');
                </script>
            '''

    if(none_atau_lainnya is not None):

        list_none_atau_lainnya = none_atau_lainnya.split("-")
        str_none_atau_lainnya = ' '.join(list_none_atau_lainnya)

        # get jenis query edit atau del atau run
        get_jenis_query = list_none_atau_lainnya[0]
        get_nama_tabel = list_none_atau_lainnya[-1]

        conn = connect_db()
        db = conn.cursor()

        if(get_jenis_query == 'edit'):

            # var1_in_edit = request.form.get['nama_tabel_edit_'+get_nama_tabel]
            var1_in_edit = request.form['nama_tabel_edit_'+get_nama_tabel]
            # var1_in_edit = get_nama_tabel
            # var2_in_edit = "CREATE TABLE IF NOT EXISTS data_tabel_myadmin (id INTEGER PRIMARY KEY AUTOINCREMENT, kolom1 TEXT, kolm2 DATETIME, kolom3 TEXT) ok"
            # var2_in_edit = request.form.get['teks_sintaks_edit_'+get_nama_tabel]
            var2_in_edit = request.form['teks_sintaks_edit_'+get_nama_tabel]

            # if(request.form['teks_sintaks_edit'] is not None):
            #     var2_in_edit = request.form['teks_sintaks_edit']
            # else:
            #     var2_in_edit = "CREATE TABLE IF NOT EXISTS data_tabel_myadmin (id INTEGER PRIMARY KEY AUTOINCREMENT, kolom1 TEXT, kolm2 DATETIME, kolom3 TEXT) ok"

            # update pada Tabel data_tabel_myadmin, pada kolom teks_sintaks
            db.execute("UPDATE data_tabel_myadmin SET teks_sintaks = ? WHERE nama_tabel = ?",(var2_in_edit, var1_in_edit))

            conn.commit()

        elif(get_jenis_query == 'del'):
            var1_in_hapus = request.form['nama_tabel_hapus_'+get_nama_tabel]

            # hapus data pada Tabel data_tabel_myadmin, pada kolom nama_tabel
            db.execute("DELETE FROM data_tabel_myadmin WHERE nama_tabel = ?",(var1_in_hapus,))

            conn.commit()

        elif(get_jenis_query == 'gen'):

            var1_in_gen = request.form['nama_tabel_gen_'+get_nama_tabel]
            var2_in_gen = request.form['teks_sintaks_tabel_gen_'+get_nama_tabel]
            var3_in_gen = request.form['teks_sintaks_page_gen_'+get_nama_tabel]

            # hapus data pada Tabel data_tabel_myadmin, pada kolom nama_tabel
            # db.execute("DELETE FROM data_tabel_myadmin WHERE nama_tabel = ?",(var1_in_hapus,))

            # conn.commit()

            # generate kode @app.route.. untuk flask_app.py
            var3_in_gen += """



            """

        # return 'Hello ' + str_none_atau_lainnya + ' Tipe request = ' + request.method + ' ' + list_none_atau_lainnya[0]+ ' ' + list_none_atau_lainnya[-1]

        # # menampilkan data dari tabel data_tabel_myadmin
        # # conn = connect_db()
        # # db = conn.cursor()

        # c = db.execute(""" SELECT * FROM  data_tabel_myadmin """)

        # var_tabel_myadmin_in = c.fetchall()

        # conn.commit()
        # # db.close()
        # # conn.close()

        db.close()
        conn.close()

        # return render_template_string(A_a+template_view+Z_z, var_tabel_myadmin = var_tabel_myadmin_in)

        return redirect(url_for('myadmin'))

    else:
        # Aksi => Buat, Hapus Tabel data_tabel_myadmin
        aksi = 'c'

        if aksi == 'c':
            conn = connect_db()
            db = conn.cursor()

            str_info = 'tabel berhasil dibuat :D'
            # create tabel
            db.execute("""
            CREATE TABLE IF NOT EXISTS data_tabel_myadmin
            (id INTEGER PRIMARY KEY AUTOINCREMENT, nama_tabel TEXT, date_pembuatan DATETIME,
            teks_sintaks TEXT)
            """)

            conn.commit()

        elif aksi== 'd':
            conn = connect_db()
            db = conn.cursor()

            str_info = 'tabel berhasil dihapus :D'
            # hapus tabel
            db.execute("""
            DROP TABLE IF EXISTS data_tabel_myadmin
            """)

            conn.commit()
            # db.close()
            # conn.close()

            # untuk membersihkan semacam cache setelah proses hapus tabel
            # conn = connect_db_to_vacuum()
            # db = conn.cursor()

            db.execute("""
            vacuum
            """)

            conn.commit()
            # db.close()
            # conn.close()

        # return str_info

        if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route lain, misal /myadmin

            var1_in = request.form['nama_tabel']
            var2_in = request.form['teks_sintaks']

            # untuk mengkondisikan nama tabel tidak boleh ada spasi
            var1_in = var1_in.replace(" ","_").lower()

            # Aksi => Buat, Hapus Tabel dari Tabel data_tabel_myadmin
            aksi_sub = 'c'

            if aksi_sub == 'c':
                # conn = connect_db()
                # db = conn.cursor()

                str_info = 'tabel berhasil dibuat :D'
                # create tabel
                db.execute("""
                CREATE TABLE IF NOT EXISTS """ + var1_in + """
                (kolom2 TEXT, kolom3 DATETIME, kolom4 TEXT)
                """)

                conn.commit()
                # db.close()
                # conn.close()

                """Mengisi data untuk spesifikasi tabel."""
                # conn = connect_db()
                # db = conn.cursor()

                db.execute("SELECT * FROM data_tabel_myadmin WHERE nama_tabel = ?", (var1_in,))
                entry = db.fetchone()

                if entry is None:
                    import numpy as np
                    import pandas as pd

                    from datetime import datetime
                    import pytz
                    Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y %H:%M:%S'))

                    db.execute("""INSERT INTO data_tabel_myadmin (nama_tabel, date_pembuatan, teks_sintaks) VALUES (?, ?, ?)""",
                        (var1_in, Date, var2_in))

                else:
                    ket_hasil = 'Tidak dilakukan Insert, karena Tabel tidak kosong'

                conn.commit()
                # db.close()
                # conn.close()

            elif aksi_sub== 'd':
                # conn = connect_db()
                # db = conn.cursor()

                str_info = 'tabel berhasil dihapus :D'
                # hapus tabel
                db.execute("""
                DROP TABLE IF EXISTS """ + var1_in + """
                """)

                conn.commit()
                # db.close()
                # conn.close()

                # untuk membersihkan semacam cache setelah proses hapus tabel
                # conn = connect_db_to_vacuum()
                # db = conn.cursor()

                db.execute("""
                vacuum
                """)

                conn.commit()
                # db.close()
                # conn.close()

            # menampilkan data dari tabel data_tabel_myadmin
            # conn = connect_db()
            # db = conn.cursor()

            c = db.execute(""" SELECT * FROM  data_tabel_myadmin """)

            var_tabel_myadmin_in = c.fetchall()

            conn.commit()
            # db.close()
            # conn.close()

            db.close()
            conn.close()

            return render_template_string(A_a+template_view+Z_z, var1 = var1_in, var2 = var2_in, var_tabel_myadmin = var_tabel_myadmin_in)

        else: # untuk yang 'GET' data awal untuk di send ke /myadmin

            # menampilkan data dari tabel data_tabel_myadmin
            # conn = connect_db()
            # db = conn.cursor()

            c = db.execute(""" SELECT * FROM  data_tabel_myadmin """)

            var_tabel_myadmin_in = c.fetchall()

            conn.commit()
            # db.close()
            # conn.close()

            db.close()
            conn.close()
            return render_template_string(A_a+template_view+Z_z, var_tabel_myadmin = var_tabel_myadmin_in)

@app.route('/launchpad_menu')
def launchpad_menu():
   return render_template("launchpad_menu.html")