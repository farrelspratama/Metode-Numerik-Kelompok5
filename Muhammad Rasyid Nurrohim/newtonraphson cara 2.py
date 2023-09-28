def newton_raphson(f, df, xi, e): #mendefinisikan nilai f(x), f'(x), xi(nilai awal) dan toleransi error
    print("Nilai xi: ", xi)
    if abs(f(xi)) < e: #kondisi apakah nilai f(xi) lebih kecil dari e
        return xi
    else:
        xi = xi - f(xi)/df(xi) #jika masih besar maka akan menghitung dengan metode newton raphsonn
        return newton_raphson(f, df, xi, e)

#menginput fungsi f(x) dan f'(x) sebagai string
fx_str = input("Masukkan fungsi f(x) sebagai string (contoh: 'x**2 + 3*x - 108'): ")
f_prime_str = input("Masukkan fungsi turunan pertama f'(x) sebagai string (contoh: '2*x + 3'): ")

#Membuat fungsi dari string input pengguna
fx = lambda x: eval(fx_str)
f_prime = lambda x: eval(f_prime_str)

n = float(input("Masukkan Nilai Aproksimasi Awal: ")) #user menginput nilai aproksima awal

estimate = newton_raphson(fx, f_prime, n, 1e-3) #pemanggilan fungsi yang hasilnya akan disimpan pada nilai cariabel estiamte
print ("estimate = %.3f" % estimate) #hasil akar yang ditemukan dengan menggunakan metode newton raphson dengan 3 angka desimal belakang koma
