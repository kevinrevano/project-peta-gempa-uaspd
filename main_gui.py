import json
import os
import tkinter as tk
from tkinter import messagebox

# Lokasi folder JSON
JSON_DIR = "data"
JSON_PATH = os.path.join(JSON_DIR, "sesar.json")

# --------------------------------------------------
# 1. Membuat folder data jika belum ada
# --------------------------------------------------
os.makedirs(JSON_DIR, exist_ok=True)

# --------------------------------------------------
# 2. Membuat file JSON kosong jika belum ada
# --------------------------------------------------
if not os.path.exists(JSON_PATH):
    with open(JSON_PATH, "w") as f:
        json.dump([], f, indent=4)


def load_data():
    """Memuat isi sesar.json"""
    with open(JSON_PATH, "r") as f:
        return json.load(f)


def save_data(data):
    """Menyimpan data ke sesar.json"""
    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=4)


def add_segment():
    """Tambah segmen tanpa koordinat"""

    nama = entry_nama.get().strip()
    magnitudo = entry_magnitudo.get().strip()
    panjang = entry_panjang.get().strip()
    tahun = entry_tahun.get().strip()

    # Validasi input
    if not (nama and magnitudo and panjang and tahun):
        messagebox.showwarning("Perhatian", "Semua field wajib diisi!")
        return

    # Konversi angka
    try:
        magnitudo = float(magnitudo)
        panjang = float(panjang)
        tahun = int(tahun)
    except:
        messagebox.showwarning("Perhatian", "Magnitudo, panjang, dan tahun harus berupa angka!")
        return

    # Membuat segmen baru TANPA KOORDINAT
    segmen = {
        "nama": nama,
        "magnitudo_maksimum": magnitudo,
        "panjang_segmen_km": panjang,
        "tahun_gempa_terakhir": tahun
    }

    # Load data lama → tambah segmen baru
    data = load_data()
    data.append(segmen)

    # Simpan kembali
    save_data(data)

    messagebox.showinfo("Berhasil", "Segmen berhasil ditambahkan!")

    # Bersihkan input
    entry_nama.delete(0, tk.END)
    entry_magnitudo.delete(0, tk.END)
    entry_panjang.delete(0, tk.END)
    entry_tahun.delete(0, tk.END)


# --------------------------------------------------
# GUI TKINTER
# --------------------------------------------------

root = tk.Tk()
root.title("Input Segmen Megathrust (Tanpa Koordinat)")
root.geometry("420x500")

tk.Label(root, text="Nama Segmen:", font=("Arial", 12)).pack()
entry_nama = tk.Entry(root, width=40)
entry_nama.pack()

tk.Label(root, text="Magnitudo Maksimum:", font=("Arial", 12)).pack()
entry_magnitudo = tk.Entry(root, width=40)
entry_magnitudo.pack()

tk.Label(root, text="Panjang Segmen (km):", font=("Arial", 12)).pack()
entry_panjang = tk.Entry(root, width=40)
entry_panjang.pack()

tk.Label(root, text="Tahun Gempa Terakhir:", font=("Arial", 12)).pack()
entry_tahun = tk.Entry(root, width=40)
entry_tahun.pack()

btn = tk.Button(root, text="Simpan Segmen", bg="lightgreen", font=("Arial", 13), command=add_segment)
btn.pack(pady=20)

root.mainloop()