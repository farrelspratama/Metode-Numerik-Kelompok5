import math # import library math agar "e" bisa terdeteksi sebagai nilai
import numpy as np # import numpy untuk fungsi yang berkaitan dengan perhitungan
import matplotlib.pyplot as plt # import matplotlib.pyplot untuk membuat dan menampilkan grafik

# Mendefinisikan fungsi untuk mencari akar
def f(x):
    return eval(persamaan)

# Mendefinisikan fungsi untuk mencari akar menggunakan metode bagi dua atau bisection
def bisection(a, b, tlt, n):
    # Proses mencari akar
    iterasi = []
    for i in range(n):
        c = (a + b) / 2.0
        iterasi.append(c)
        if f(c) == 0.0 or (b - a) / 2.0 < tlt:
            return c, iterasi
        elif f(a) * f(c) < 0.0:
            b = c
        else:
            a = c
    return (a + b) / 2.0, iterasi

# Input persamaan, interval, jumlah maksimum iterasi, dan ketelitian dari pengguna
persamaan = input("Masukkan persamaan fungsi (contoh: 'x**2 - 2*x - 8'): ")

# Ganti "e" dengan math.e dalam persamaan
persamaan = persamaan.replace("e", "math.e") # ini agar "e" terdeteksi sebagai nilai

a = float(input("Masukkan batas bawah interval (a): "))
b = float(input("Masukkan batas atas interval (b): "))
n = int(input("Masukkan jumlah maksimum iterasi: "))
teliti = float(input("Masukkan ketelitian (contoh : '0.001', 3 angka dibelakang koma): "))

# memanggil fungsi bisection untuk mencari akar
akar_hampiran, iterasi = bisection(a, b, teliti, n)

# membuat array nilai x untuk menggambar grafik
x = np.linspace(a, b, 400)
y = [f(xi) for xi in x]

# Ambil nilai x dari iterasi
iterasi_x = [a, b] + iterasi

# Gambar grafik fungsi dengan menggunakan library matplotlib.pyplot
plt.plot(x, y, label=f'f(x) = {persamaan}')
plt.axhline(0, color='red', linestyle='--', linewidth=0.7, label='y = 0')
plt.scatter(iterasi_x, [f(xi) for xi in iterasi_x], color='green', label='Iterasi', zorder=5)
plt.annotate(f'Akar hampiran: {akar_hampiran:.6f}', (akar_hampiran, f(akar_hampiran)), color='blue')

# mengkonfigurasi grafik
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik fungsi f(x) dengan Iterasi Metode Bisection')
plt.grid(True)
plt.legend()

# Menampilkan grafik
plt.show()
