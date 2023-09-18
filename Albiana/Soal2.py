import math #import library math agar "e" bisa terdeteksi sebagai nilai

# Mendefinisikan fungsi dari soal
def f(x): 
    return math.exp(x) - x 

# Mendefinisikan fungsi untuk mencari akar menggunakan metode bagi dua atau bisection
def bisection(a, b, tol):
    # Proses mencari akar
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0.0:
            return c
        elif f(a) * f(c) < 0.0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

# Mendefinisikan interval awal [a, b] dan Ketelitian
a = -1.0
b = 1.0
ketelitian = 1e-3

# Memanggil fungsi bisection untuk mencari akar
akar_hampiran = bisection(a, b, ketelitian)

print("Akar hampiran:", akar_hampiran) # Hasil akarnya
