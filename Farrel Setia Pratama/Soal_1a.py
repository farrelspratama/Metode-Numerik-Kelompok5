import numpy as np #Menambahkan library numpy untuk operasi matematika

def f(x): #Define fungsi untuk mencari akar
    return x**3 - 2*x + 1

def bisection_method(f, a, b, e): #Define algoritma untuk mencari akar dengan metode bagi dua
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    
    while (b - a) / 2 > e:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif np.sign(f(m)) == np.sign(f(a)):
            a = m
        else:
            b = m
    
    return (a + b) / 2

a = -2  #Batas negatif untuk interval
b = 2   #Batas positif untuk interval
e = 1e-6  #Nilai toleransi galat
akar = bisection_method(f, a, b, e) #Memasukan nilai pada metode bagi dua
print(f"Akar dari f(x) = x^3 - 2x + 1 adalah {akar}") #Memunculkan nilai akar