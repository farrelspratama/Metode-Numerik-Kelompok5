import sympy as sp #library

#user diminta untuk menginput f(x) dan g(x) sebagai string
fx_str = input("Masukkan fungsi f(x) sebagai string (contoh: 'x**2 - 2*x - 8'): ")
gx_str = input("Masukkan fungsi g(x) sebagai string (contoh: '2*x - 2'): ")

#membuat simbol dan mengkonversi string yang mewakili fungsi f(x)dan g(x)
x = sp.symbols('x')
fx = sp.sympify(fx_str)
gx = sp.sympify(gx_str)

#mendefinisikan fungsi f(x) dan g(x) dari string input pengguna
f = sp.lambdify(x, fx, 'numpy')
g = sp.lambdify(x, gx, 'numpy')

# Mendefinisikan fungsi metode newtonRaphson
def newtonRaphson(x0,e,N): #x0= perkiraan awal, e= toleransi error, N = jumlah langkah maksimum
    step = 1
    flag = 1
    condition = True  #sebuah kondisi untuk menjalankan loop
    while condition:  
        if g(x0) == 0.0:   #pemeriksaan kondisi apakah g(x) pada nilai x0 sama dengan 0
            print('dibagi 0 error')  #maka program akan mengeluarkan output error dan akan menghentiakan program dengan break
            break
        x1 = x0 - f(x0)/g(x0) #menghitung x1 dengan rumus newton-raphson
        print('Iterasi-%d, x1 = %0.6f dan f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1 #digunakan sebagai menambahkan jumlah iterasi

        if step > N: #kondisi untuk memriksa apakah jumlah iterasi mencapai batas yang ditentukan oleh pengguna
            flag = 0
            break   #jika ya maka akan dihentikan

        condition = abs(f(x1)) > e

    if flag==1:
        print('\nakar yang dibutuhkan : %0.8f' % x1)
    else:
        print('\ntidak konvergen')

#inputan tipe data
x0 = input('Perkiraan: ')
x0 = float(x0)
e = input('Perkiraan Error: ')
e = float(e)
# convert inputan ke tipe data int
N = input('Jumlah Step: ')
N = int(N)

newtonRaphson(x0,e,N) #pemanggilan fungsi newton raphson
