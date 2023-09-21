import math #Menambahkan library math agar "e" bisa terdeteksi sebagai nilai
import numpy as np #Menambahkan library numpy untuk operasi matematika
import matplotlib.pyplot as plt #Menambahkan library matplotlib.pyplot untuk membuat dan menampilkan grafik

def f(x): #Define fungsi untuk mencari akar
    return eval(persamaan)

def bisection(a, b, tlt, n): #Define algoritma untuk mencari akar dengan metode bagi dua
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

persamaan = input("Masukkan persamaan fungsi (contoh: 'x**2 - 2*x - 8'): ") #Input fungsi yang diinginkan

persamaan = persamaan.replace("e", "math.e") #Mengganti "e" dengan math.e agar "e" terdeteksi sebagai nilai

a = float(input("Masukkan batas bawah interval (a): "))
b = float(input("Masukkan batas atas interval (b): "))
n = int(input("Masukkan jumlah maksimum iterasi: "))
teliti = float(input("Masukkan ketelitian (contoh : '0.001', 3 angka dibelakang koma): "))

akar_hampiran, iterasi = bisection(a, b, teliti, n) #Memasukan nilai pada metode bagi dua

x = np.linspace(a, b, 400) #Membuat array untuk menggambar grafik dari nilai interval a dan b
y = [f(xi) for xi in x]

iterasi_x = [a, b] + iterasi #Mengambil nilai x dari iterasi

#Menggunakan library matplotlib.pyplot untuk menggambar grafik
plt.plot(x, y, label=f'f(x) = {persamaan}') 
plt.axhline(0, color='red', linestyle='--', linewidth=0.7, label='y = 0')
plt.scatter(iterasi_x, [f(xi) for xi in iterasi_x], color='green', label='Iterasi', zorder=5)
plt.annotate(f'Akar hampiran: {akar_hampiran:.6f}', (akar_hampiran, f(akar_hampiran)), color='blue')

#Mengatur isi grafik
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik fungsi f(x) dengan Iterasi Metode Bisection')
plt.grid(True)
plt.legend()

#Menampilkan grafik
plt.show()