import json
import os
import tkinter as tk
from tkinter import messagebox

JSON_DIR = "data"
JSON_PATH = os.path.join(JSON_DIR, "sesar.json")

os.makedirs(JSON_DIR, exist_ok=True)

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
    magnitudo = entry_m.get().strip()
    panjang = entry_p.get().strip()
    tahun = entry_t.get().strip()
    lat = entry_lat.get().strip()
    lon = entry_lon.get().strip()

    if not (nama and magnitudo and panjang and tahun and lat and lon):
        messagebox.showwarning("Warning", "Semua field wajib diisi!")
        return
    
    try:
        magnitudo = float(magnitudo)
        panjang = float(panjang)
        tahun = int(tahun)
        lat = float(lat)
        lon = float(lon)
    except:
        messagebox.showwarning("Error", "Pastikan angka sudah benar")
        return

    segmen = {
        "nama": nama,
        "magnitudo_maksimum": magnitudo,
        "panjang_segmen_km": panjang,
        "tahun_gempa_terakhir": tahun,
        "lat": lat,
        "lon": lon
    }

    data = load_data()
    data.append(segmen)
    save_data(data)
    messagebox.showinfo("Sukses", "Segmen berhasil ditambahkan!")

    entry_nama.delete(0, tk.END)
    entry_m.delete(0, tk.END)
    entry_p.delete(0, tk.END)
    entry_t.delete(0, tk.END)
    entry_lat.delete(0, tk.END)
    entry_lon.delete(0, tk.END)

root = tk.Tk()
root.title("Input Segmen Megathrust")
root.geometry("420x550")

tk.Label(root, text="Nama Segmen").pack()
entry_nama = tk.Entry(root, width=40)
entry_nama.pack()

tk.Label(root, text="Magnitudo Maksimum").pack()
entry_m = tk.Entry(root, width=40)
entry_m.pack()

tk.Label(root, text="Panjang Segmen (km)").pack()
entry_p = tk.Entry(root, width=40)
entry_p.pack()

tk.Label(root, text="Tahun Gempa Terakhir").pack()
entry_t = tk.Entry(root, width=40)
entry_t.pack()

tk.Label(root, text="Latitude").pack()
entry_lat = tk.Entry(root, width=40)
entry_lat.pack()

tk.Label(root, text="Longitude").pack()
entry_lon = tk.Entry(root, width=40)
entry_lon.pack()

tk.Button(root, text="Simpan Segmen", command=add_segment, bg="lightgreen").pack(pady=15)

root.mainloop()