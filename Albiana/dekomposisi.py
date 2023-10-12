import numpy as np  # Mengimpor library NumPy yang digunakan untuk operasi matriks

def dekomposisi_LU(A):
    n = len(A)  # Menghitung ukuran matriks A
    L = np.zeros((n, n))  # Membuat matriks nol dengan ukuran n x n untuk matriks L
    U = np.zeros((n, n))  # Membuat matriks nol dengan ukuran n x n untuk matriks U

    for i in range(n):  # Looping melalui baris matriks
        # Matriks U: Proses dekomposisi matriks A menjadi matriks U (Segitiga Atas)
        for k in range(i, n):
            total = 0
            for j in range(i):
                total += L[i][j] * U[j][k]
            U[i][k] = A[i][k] - total

        # Matriks L: Proses dekomposisi matriks A menjadi matriks L (Segitiga Bawah)
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  # Elemen diagonal utama matriks L selalu 1
            else:
                total = 0
                for j in range(i):
                    total += L[k][j] * U[j][i]
                L[k][i] = (A[k][i] - total) / U[i][i]

    return L, U  # Mengembalikan matriks L dan U setelah dekomposisi

# Input matriks dari pengguna
n = int(input("Masukkan ukuran matriks (n): "))  # Meminta pengguna untuk memasukkan ukuran matriks
A = np.zeros((n, n))  # Membuat matriks nol dengan ukuran yang telah diinputkan

print("Masukkan elemen matriks A:")  # Memberikan instruksi kepada pengguna untuk memasukkan elemen matriks A
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"A[{i+1}][{j+1}]: "))  # Meminta pengguna untuk memasukkan elemen matriks A

# Lakukan dekomposisi LU
L, U = dekomposisi_LU(A)  # Memanggil fungsi dekomposisi_LU untuk mendapatkan matriks L dan U

# Tampilkan matriks L dan U
print("\nMatriks Segitiga Bawah L:")  # Mencetak matriks L (Segitiga Bawah)
print(L)
print("\nMatriks Segitiga Atas U:")  # Mencetak matriks U (Segitiga Atas)
print(U)
