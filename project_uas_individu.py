import mysql.connector
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio_battery import popup_input, confirm
from datetime import datetime


def koneksi_db():
    konek = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="uas_alpro_semt1",
    )
    return konek


def buat_tabel_cuaca():
    konek = koneksi_db()
    cursor = konek.cursor()
    query = "CREATE TABLE IF NOT EXISTS cuaca (id_cuaca INT PRIMARY KEY AUTO_INCREMENT, lokasi varchar(225), waktu date, suhu INT, kondisi varchar(50))"
    cursor.execute(query)


buat_tabel_cuaca()


def kondisi_cuaca(suhu):
    if suhu < 27:
        return "dingin"
    elif suhu >= 27 and suhu <= 31:
        return "normal"
    elif suhu > 31:
        return "panas"


def lihat_lokasi():
    konek = koneksi_db()
    cursor = konek.cursor()
    cursor.execute("SELECT lokasi FROM cuaca")
    hasil_data = cursor.fetchall()
    head = ["LOKASI"]
    return put_table([head] + hasil_data)


def lihat_cuaca():
    konek = koneksi_db()
    cursor = konek.cursor()
    cursor.execute("SELECT * FROM cuaca")
    hasil_data = cursor.fetchall()
    head = ["ID CUACA", "LOKASI", "WAKTU", "SUHU", "KONDISI"]
    return put_table([head] + hasil_data)


def tambah_data_cuaca():
    konek = koneksi_db()
    cursor = konek.cursor()
    tambah_data_waktu = datetime.now()
    form = popup_input(
        [
            put_input("tambah_lokasi", type=TEXT, label="Masukkan Lokasi"),
            put_input("tambah_data_suhu", type=NUMBER, label="Masukkan suhu lokasi"),
        ],
        title="TAMBAH DATA CUACA",
    )
    kondisi_data_lokasi = kondisi_cuaca(form["tambah_data_suhu"])

    query_data_cuaca = (
        "INSERT INTO cuaca (lokasi, waktu, suhu, kondisi) VALUES (%s,%s,%s,%s)"
    )
    query_value = (
        form["tambah_lokasi"],
        tambah_data_waktu,
        form["tambah_data_suhu"],
        kondisi_data_lokasi,
    )
    cursor.execute(query_data_cuaca, query_value)
    konek.commit()
    konek.close()
    with popup("Berhasil"):
        put_text("Data cuaca ditambahkan")


def lihat_data_lokasi():
    with popup("DATA SEMUA LOKASI", size="small"):
        lihat_lokasi()


def lihat_data_cuaca():
    with popup("DATA SEMUA CUACA"):
        lihat_cuaca()


def cari_data(data):
    konek = koneksi_db()
    cursor = konek.cursor()
    val_cari = ("%{}%".format(data),)
    cursor.execute(
        "SELECT id_cuaca, lokasi, waktu, suhu, kondisi FROM cuaca WHERE lokasi LIKE %s",
        val_cari,
    )
    hasil = cursor.fetchall()
    return hasil


def cari_data_cuaca():
    head = ["ID LOKASI", "LOKASI", "WAKTU", "SUHU", "KONSISI"]
    form = popup_input(
        [
            put_input("nama_lokasi", label="Masukkan nama lokasi yang dicari"),
        ],
        title="CARI DETAIL DATA CUACA",
    )
    with popup("HASIL PENCARIAN DATA"):
        put_table([head] + cari_data(form["nama_lokasi"]))


def edit_data_cuaca():
    konek = koneksi_db()
    cursor = konek.cursor()
    edit_data_waktu = datetime.now()
    form = popup_input(
        [
            put_input(
                "id_cuaca", label="Masukkan id data cuaca yang mau diedit", type=NUMBER
            ),
            put_input("lokasi_edit", label="Masukkan lokasi", type=TEXT),
            put_input("suhu_edit", label="Masukkan suhu", type=NUMBER),
            lihat_cuaca(),
        ],
        title="EDIT DATA CUACA",
    )
    kondisi__data_cuaca = kondisi_cuaca(form["suhu_edit"])
    value_edit = (
        form["lokasi_edit"],
        edit_data_waktu,
        form["suhu_edit"],
        kondisi__data_cuaca,
        form["id_cuaca"],
    )
    confirm_edit = confirm(
        f"yakin ingin mengedit data cuaca dengan ID {form['id_cuaca']} "
    )
    if confirm_edit == True:
        cursor.execute(
            "UPDATE cuaca SET lokasi=%s, waktu=%s, suhu=%s, kondisi=%s WHERE id_cuaca=%s",
            value_edit,
        )
        konek.commit()
        konek.close()
        popup("Berhasil Di edit", put_text(f"Data cuaca dengan ID {form['id_cuaca']}"))


def hapus_data_cuaca():
    konek = koneksi_db()
    cursor = konek.cursor()
    form = popup_input(
        [
            put_input("id_cuaca", label="Masukkan id cuaca yang mau dihapus"),
            lihat_cuaca(),
        ],
        title="HAPUS DATA CUACA",
    )
    confirm_hapus = confirm(
        f"yakin ingin menghapus data cuaca dengan ID {form['id_cuaca']} "
    )
    if confirm_hapus == True:
        cursor.execute(f"DELETE FROM cuaca WHERE id_cuaca={form['id_cuaca']}")
        konek.commit()
        konek.close()
        popup("Berhasil Di Hapus", put_text(f"Data cuaca dengan ID {form['id_cuaca']}"))


def menu_cuaca():
    style(put_text("SISTEM INFORMASI CUACA"), "font-size: 35px; font-weight: bold;")
    put_html("<hr/>")
    style(put_text("1. Tambah data cuaca"), "font-size: 20px;")
    style(put_text("2. Lihat data lokasi"), "font-size: 20px;")
    style(put_text("3. Lihat data cuaca"), "font-size: 20px;")
    style(put_text("4. Cari data cuaca"), "font-size: 20px;")
    style(put_text("5. Edit data cuaca"), "font-size: 20px;")
    style(put_text("6. Hapus data cuaca"), "font-size: 20px;")
    put_html("<hr/>")


def main_sistem():
    menu_cuaca()
    while True:
        pilih_menu = int(input("Masukkan menu yang anda pilih (1-6)"))
        if pilih_menu == 1:
            tambah_data_cuaca()
        elif pilih_menu == 2:
            lihat_data_lokasi()
        elif pilih_menu == 3:
            lihat_data_cuaca()
        elif pilih_menu == 4:
            cari_data_cuaca()
        elif pilih_menu == 5:
            edit_data_cuaca()
        elif pilih_menu == 6:
            hapus_data_cuaca()
        else:
            put_text("menu yang anda pilih tidak ada!")


start_server(main_sistem, port=8080)
