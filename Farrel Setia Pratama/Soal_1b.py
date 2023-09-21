import numpy as np #Menambahkan library numpy untuk operasi matematika

def f(x): #Define fungsi untuk mencari akar
    return x**x - x

def bisection_method(a, b, e): #Define algoritma untuk mencari akar dengan metode bagi dua

    while (b - a) / 2.0 > e:
        c = (a + b) / 2.0
        if f(c) == 0.0:
            return c
        elif f(a) * f(c) < 0.0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

a = -1  #Batas negatif untuk interval
b = 1 #Batas positif untuk interval
e = 1e-3 #Nilai toleransi galat

akar_hampiran = bisection_method(a, b, e) #Memasukan nilai pada metode bagi dua

print("Akar dari f(x) = x^x - x adalah", akar_hampiran) #Memunculkan nilai akar