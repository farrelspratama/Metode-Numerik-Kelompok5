import numpy as np #pemanggilan library

def f(x): # digunakan untuk mencari akar dari f(x)
    return x**x - x

# Mendefinisikan fungsi untuk mencari akar menggunakan metode bagi dua atau bisection
def bisection_method(a, b, e): #bisection digunakan sebagai metode pencarian akar dari suatu fungsi f(x)

    while (b - a) / 2 > e: # dugunakan untuk menghitung selisih antara b dan a lalu dibagi dua yang nantinya akan menghasilkan panjang interval
        m = (a + b) / 2 #m merupakan nilai tengah dari a dan b  dan digunakan sebagai nilai fungsi di tengah interval 
        if f(m) == 0: #memeriksa apakah m sama dengan nol
            return m
        elif np.sign(f(a)) * np.sign(f(m)) < 0: #akan memeriksa dengan sebuah perkaliannya kurang dari nol yang berarti akar berada di antara a dan m 
            b = m #jika kodisi tersebut memenuhi maka a akan diperbaharui menjadi m
        else:
            a = m #kondisi terakhir jika f(m) dan f(a) berbeda, maka b akan diperbaharui menjadi m
    return (a + b) / 2 #jika proses iterasi selesai maka akan mengembalikan nilai tengah dari interval yang sudah ditemukan

a = -1  #batas dari bawah interva;
b = 1 #batas atas interval
e = 1e-3 #tingkat roleransi error

akar_hampiran = bisection_method(a, b, e) #pemanggilan fungsi metode biseksi

print("Akar dari f(x) = x^x - x adalah", akar_hampiran) #merupakan hasil output dari hasil akar yang telah ditemukan
