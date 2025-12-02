import json
import os
import tkinter as tk
from tkinter import messagebox

# Lokasi file JSON
JSON_DIR = "data"
JSON_PATH = os.path.join(JSON_DIR, "sesar.json")

# --------------------------------------------------
# 1. Buat folder data jika belum ada
# --------------------------------------------------
os.makedirs(JSON_DIR, exist_ok=True)

# --------------------------------------------------
# 2. Buat file JSON kosong jika belum ada
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
    """Tambah segmen baru ke JSON"""

    nama = entry_nama.get().strip()
    magnitudo = entry_magnitudo.get().strip()
    panjang = entry_panjang.get().strip()
    tahun = entry_tahun.get().strip()
    koordinat_raw = text_koordinat.get("1.0", tk.END).strip()

    # Validasi sederhana
    if not (nama and magnitudo and panjang and tahun and koordinat_raw):
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

    # Parsing koordinat
    try:
        koordinat = []
        for baris in koordinat_raw.split("\n"):
            lat, lon = baris.split(",")
            koordinat.append([float(lat), float(lon)])
    except:
        messagebox.showwarning("Perhatian", "Format koordinat salah!\nGunakan format: lat,lon per baris")
        return

    # Buat segmen baru
    segmen = {
        "nama": nama,
        "magnitudo_maksimum": magnitudo,
        "panjang_segmen_km": panjang,
        "tahun_gempa_terakhir": tahun,
        "koordinat": koordinat
    }

    # Load data lama → tambah segmen baru
    data = load_data()
    data.append(segmen)

    # Simpan kembali
    save_data(data)

    # Notifikasi
    messagebox.showinfo("Berhasil", "Segmen ditambahkan!")

    # Bersihkan input
    entry_nama.delete(0, tk.END)
    entry_magnitudo.delete(0, tk.END)
    entry_panjang.delete(0, tk.END)
    entry_tahun.delete(0, tk.END)
    text_koordinat.delete("1.0", tk.END)


# -----------------------------------------------------------------------
#                    GUI TKINTER
# -----------------------------------------------------------------------

root = tk.Tk()
root.title("Input Segmen Megathrust Indonesia")
root.geometry("500x650")

tk.Label(root, text="Nama Segmen:", font=("Arial", 11)).pack()
entry_nama = tk.Entry(root, width=45)
entry_nama.pack()

tk.Label(root, text="Magnitudo Maksimum:", font=("Arial", 11)).pack()
entry_magnitudo = tk.Entry(root, width=45)
entry_magnitudo.pack()

tk.Label(root, text="Panjang Segmen (km):", font=("Arial", 11)).pack()
entry_panjang = tk.Entry(root, width=45)
entry_panjang.pack()

tk.Label(root, text="Tahun Gempa Terakhir:", font=("Arial", 11)).pack()
entry_tahun = tk.Entry(root, width=45)
entry_tahun.pack()

tk.Label(root, text="Koordinat (lat,lon per baris):", font=("Arial", 11)).pack()
text_koordinat = tk.Text(root, height=8, width=45)
text_koordinat.pack()

btn = tk.Button(root, text="Simpan Segmen", bg="lightgreen", font=("Arial", 12), command=add_segment)
btn.pack(pady=15)

root.mainloop()