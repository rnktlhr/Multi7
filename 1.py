import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan hasil prediksi
def predict_result():
    try:
        # Memeriksa apakah semua nilai berada dalam rentang 0–100
        for entry in entries:
            n = int(entry.get())
            if not (0 <= n <= 100):
                raise ValueError("Nilai harus 0-100")
        # Menampilkan hasil prediksi jika semua input valid
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi", fg="#FFFFFF")
    except ValueError as ve:
        # Menampilkan pesan kesalahan jika ada input yang tidak valid
        messagebox.showerror("Input Error", "Pastikan input sesuai dengan yang diminta")
        hasil_label.config(text="")

# Inisialisasi jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x650")
root.configure(bg="#FFA500")  # Warna latar belakang oranye

# Menggunakan font Gilroy (Pastikan font ini terinstal di sistem Anda)
try:
    root.option_add("*Font", "Gilroy 12")  # Mengatur font default menjadi Gilroy
except:
    root.option_add("*Font", "Arial 12")  # Jika Gilroy tidak ada, gunakan Arial

# Label Judul
judul_label = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Gilroy", 20, "bold"),  # Menggunakan font Gilroy
    bg="#FFA500",  # Warna latar belakang oranye
    fg="#FFFFFF"  # Warna teks putih
)
judul_label.pack(pady=20)

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#FFD700")  # Warna kuning oranye untuk frame input
frame_input.pack(pady=10)

# Membuat 10 input nilai mata pelajaran
entries = []
for i in range(10):
    label = tk.Label(
        frame_input,
        text=f"Nilai Mata Pelajaran {i + 1}:",
        font=("Gilroy", 12),  # Menggunakan font Gilroy
        bg="#FFD700",  # Warna kuning oranye untuk label
        fg="#333333"  # Warna teks hitam
    )
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(
        frame_input, 
        width=10, 
        font=("Gilroy", 12),  # Menggunakan font Gilroy
        relief="solid", 
        bd=1, 
        bg="#FFFAF0",  # Warna latar belakang input box
        highlightbackground="#DADCE0",
        highlightthickness=1
    )
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Tombol Hasil Prediksi
prediksi_button = tk.Button(
    root,
    text="Hasil Prediksi",
    command=predict_result,
    font=("Gilroy", 12, "bold"),  # Menggunakan font Gilroy
    bg="#FF8C00",  # Warna oranye gelap untuk tombol
    fg="white",  # Warna teks putih
    activebackground="#FF4500",  # Warna aktif saat hover
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10
)
prediksi_button.pack(pady=30)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(
    root,
    text="",
    font=("Gilroy", 14, "italic"),  # Menggunakan font Gilroy
    bg="#FFA500",  # Warna latar belakang oranye
    fg="#FFFFFF"  # Warna teks putih
)
hasil_label.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()