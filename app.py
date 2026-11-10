from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

def salam_waktu(jam):
    """Mengembalikan salam sesuai jam (0-23)."""
    if 4 <= jam < 11:
        return "Selamat pagi"
    if 11 <= jam < 15:
        return "Selamat siang"
    if 15 <= jam < 18:
        return "Selamat sore"
    return "Selamat malam"  # 18.00-03.59

# Satu rute untuk GET (buka halaman) dan POST (kirim formulir)
@app.route("/", methods=["GET", "POST"])
def beranda():
    nama = ""
       # Tanggal dan jam server saat ini, lalu tentukan salamnya
    waktu_sekarang = datetime.now()
    sekarang = waktu_sekarang.strftime("%d-%m-%Y %H:%M:%S")
    salam = salam_waktu(waktu_sekarang.hour)

    return render_template("index.html", sekarang=sekarang, nama=nama, salam=salam)

@app.route("/bantuan")
def bantuan():
    return render_template("bantuan.html")

@app.route("/tentang")
def tentang():
    anggota = ["bayunandapamungkas", "nursintianabila"]
    return render_template("tentang.html", anggota=anggota)

if __name__ == "__main__":
    # Berjalan di localhost saja
    app.run(host="127.0.0.1", port=5000, debug=True)