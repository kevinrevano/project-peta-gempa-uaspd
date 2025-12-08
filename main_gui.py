import json
import os
import tkinter as tk
from tkinter import messagebox

# Lokasi data JSON
JSON_DIR = "data"
JSON_PATH = os.path.join(JSON_DIR, "sesar.json")

# buat folder data
os.makedirs(JSON_DIR, exist_ok=True)

# buat file json jika belum ada
if not os.path.exists(JSON_PATH):
    with open(JSON_PATH, "w") as f:
        json.dump([], f, indent=4)

def load_data():
    with open(JSON_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=4)

def add_segment():
    nama = entry_nama.get().strip()
    magnitudo = entry_magnitudo.get().strip()
    panjang = entry_panjang.get().strip()
    tahun = entry_tahun.get().strip()
    lat = entry_lat.get().strip()
    lon = entry_lon.get().strip()
    angle = entry_angle.get().strip()

    if not (nama and magnitudo and panjang and tahun and lat and lon and angle):
        messagebox.showwarning("Perhatian", "Semua field wajib diisi!")
        return

    try:
        magnitudo = float(magnitudo)
        panjang = float(panjang)
        tahun = int(tahun)
        lat = float(lat)
        lon = float(lon)
        angle = float(angle)
    except:
        messagebox.showwarning("Perhatian", "Pastikan semua angka valid!")
        return

    segmen = {
        "nama": nama,
        "magnitudo_maksimum": magnitudo,
        "panjang_segmen_km": panjang,
        "tahun_gempa_terakhir": tahun,
        "lat": lat,
        "lon": lon,
        "angle": angle
    }

    data = load_data()
    data.append(segmen)
    save_data(data)

    messagebox.showinfo("Berhasil", "Segmen berhasil ditambahkan!")

    # reset input
    entry_nama.delete(0, tk.END)
    entry_magnitudo.delete(0, tk.END)
    entry_panjang.delete(0, tk.END)
    entry_tahun.delete(0, tk.END)
    entry_lat.delete(0, tk.END)
    entry_lon.delete(0, tk.END)
    entry_angle.delete(0, tk.END)

# ================= GUI ======================
root = tk.Tk()
root.title("Input Segmen Megathrust Indonesia")
root.geometry("420x600")

tk.Label(root, text="Nama Segmen").pack()
entry_nama = tk.Entry(root, width=40); entry_nama.pack()

tk.Label(root, text="Magnitudo Maksimum").pack()
entry_magnitudo = tk.Entry(root, width=40); entry_magnitudo.pack()

tk.Label(root, text="Panjang Segmen (km)").pack()
entry_panjang = tk.Entry(root, width=40); entry_panjang.pack()

tk.Label(root, text="Tahun Gempa Terakhir").pack()
entry_tahun = tk.Entry(root, width=40); entry_tahun.pack()

tk.Label(root, text="Latitude (titik tengah)").pack()
entry_lat = tk.Entry(root, width=40); entry_lat.pack()

tk.Label(root, text="Longitude (titik tengah)").pack()
entry_lon = tk.Entry(root, width=40); entry_lon.pack()

tk.Label(root, text="Arah Segmen (derajat)").pack()
entry_angle = tk.Entry(root, width=40); entry_angle.pack()

tk.Button(root, text="Simpan Segmen", font=("Arial", 12),
          bg="lightgreen", command=add_segment).pack(pady=20)

root.mainloop()