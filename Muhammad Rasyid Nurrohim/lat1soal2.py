import math # pemanggilan library
import numpy as np #pemanggilan library yang berkaitan dengna perhitungan numerik
import matplotlib.pyplot as plt #pemanggilan library untuk menampilkan grafik


def f(x): # digunakan untuk mencari akar dari f(x)
    return eval(persamaan)

def bisection(a, b, tlt, n):  # Mendefinisikan fungsi untuk mencari akar menggunakan metode bagi dua atau bisection
    iterasi = []
    for i in range(n): #digunakannya for untuk melakukan itarasi sebanyak n kali
        c = (a + b) / 2
        iterasi.append(c) #menyimpan nilai c kedalam iterasi
        if f(c) == 0 or (b - a) / 2 < tlt: #mengecek tingkat akurasi yang diinginkan dan memasukannya ke dalam iterasi
            return c, iterasi
        elif f(a) * f(c) < 0: #memeriksa perkalian
            b = c #jika kurang dari nol akan memperbaharui nilai b menjadi c
        else:
            a = c #jika salah, maka akan memperbaharui nilai a menjadi c
    return (a + b) / 2, iterasi 


persamaan = input("Masukkan persamaan fungsi (contoh: 'x**2 - 2*x - 8'): ") #ser melakukan input

persamaan = persamaan.replace("e", "math.e") #mengganti karakter e dalam persamaan fungsi agar e dapat dikenapi sebagai euler

a = float(input("Masukkan batas bawah interval (a): ")) #menginput nilai batas bawah interval
b = float(input("Masukkan batas atas interval (b): ")) #menginput nilai batas atas interval
n = int(input("Masukkan jumlah maksimum iterasi: ")) #menginput jumlah maksimum iterasi
teliti = float(input("Masukkan ketelitian (contoh : '0.001', 3 angka dibelakang koma): ")) #menginput jumlah ketelitian


akar_hampiran, iterasi = bisection(a, b, teliti, n) #pemanggilan fungsi bisection untuk mencari akar fungsi yang telah di input

x = np.linspace(a, b, 400) #membuat arrat dari interval a dan b dengan 400 titik
y = [f(xi) for xi in x] 

iterasi_x = [a, b] + iterasi  #nilai tengah dari seriap iterasi akan disimpaan di iterasi_x

#pemanggilan library matplotbib
plt.plot(x, y, label=f'f(x) = {persamaan}')
plt.axhline(0, color='red', linestyle='--', linewidth=0.7, label='y = 0')
plt.scatter(iterasi_x, [f(xi) for xi in iterasi_x], color='green', label='Iterasi', zorder=5)
plt.annotate(f'Akar hampiran: {akar_hampiran:.6f}', (akar_hampiran, f(akar_hampiran)), color='blue')

#mengatur dari grafik yang akan ditampilkan
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik fungsi f(x) dengan Iterasi Metode Bisection')
plt.grid(True)
plt.legend()

plt.show() #pemanggilan yang berfungsi untuk menampilkan grafik
