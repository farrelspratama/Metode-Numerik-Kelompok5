# Mendefinisikan fungsi metode newtonRaphson dengan fungsi f(x) dan g(x) sebagai argumen
def newtonRaphson(f, g, x0, e, N):
    step = 1
    while step <= N:
        if g(x0) == 0.0:
            print('Turunan nol, tidak bisa melanjutkan.')
            return
        
        x1 = x0 - f(x0) / g(x0)
        print(f'Iterasi-{step}, x1 = {x1:.6f} dan f(x1) = {f(x1):.6f}')
        x0 = x1
        
        if abs(f(x1)) <= e:
            print(f'\nAkar yang dibutuhkan: {x1:.8f}')
            return
        
        step += 1

    print('\nTidak konvergen')

# Fungsi f(x) dan g(x) didefinisikan sebagai fungsi lambda
f = lambda x: x**2 - 4
g = lambda x: 2*x

# Penanganan kesalahan input
try:
    x0 = float(input('Perkiraan: '))
    e = float(input('Perkiraan Error: '))
    N = int(input('Jumlah Step: '))
except ValueError:
    print('Input tidak valid. Pastikan Anda memasukkan angka.')

newtonRaphson(f, g, x0, e, N)
