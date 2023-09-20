import numpy as np  # library Numpy ini digunakan untuk operasi matematika


def f(x): # digunakan untuk mencari akar dari f(x)
    return x**3 - 2*x + 1

def bisection_method(f, a, b, e): #bisection digunakan sebagai metode pencarian akar dari suatu fungsi f(x)
    if np.sign(f(a)) == np.sign(f(b)): # pengecekan jika f(a) dan f(b) nya sama
        raise Exception('Tidak ada akar pada interval a dan b')   #jika a dan b nya sama maka progam akan terhenti disini 
    
    while (b - a) / 2 > e: # dugunakan untuk menghitung selisih antara b dan a lalu dibagi dua yang nantinya akan menghasilkan panjang interval
        m = (a + b) / 2  #m merupakan nilai tengah dari a dan b  dan digunakan sebagai nilai fungsi di tengah interval 
        if f(m) == 0:
            return m
        elif np.sign(f(m)) == np.sign(f(a)): #kondisi dimana f(m) dama dengan f(a), 
            a = m #jika kodisi tersebut memenuhi maka a akan diperbaharui menjadi m
        else:
            b = m #kondisi terakhir jika f(m) dan f(a) berbeda, maka b akan diperbaharui menjadi m
    
    return (a + b) / 2 #jika proses iterasi selesai maka akan mengembalikan nilai tengah dari interval yang sudah ditemukan

a = -2  #batas dari bawah interval
b = 2   #batas dari atas interval
e = 1e-6  #tingkat toleransi error
akar = bisection_method(f, a, b, e) #penggunaan metode biseksi
print(f"Akar dari f(x) = x^3 - 2x + 1 adalah {akar}") #merupakan hasil output dari hasil akar yang telah ditemukan