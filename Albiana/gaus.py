import numpy as np

def gaussian_elimination(A, b):
    n = A.shape[0]
    C = np.hstack((A, b))

    for i in range(n):
        pivot_row = np.argmax(np.abs(C[i:, i])) + i
        if C[pivot_row, i] == 0:
            return None, "No unique solution exists."

        if pivot_row != i:
            C[[i, pivot_row]] = C[[pivot_row, i]]

        ratio = C[i+1:, i] / C[i, i]
        C[i+1:] -= ratio[:, np.newaxis] * C[i]

    return C

def back_substitution(T):
    n = T.shape[0]
    X = np.zeros(n)
    if T[n-1, n-1] == 0:
        return None, "No unique solution exists."
    else:
        X[n-1] = T[n-1, -1] / T[n-1, n-1]
        for i in range(n-2, -1, -1):
            X[i] = (T[i, -1] - np.sum(T[i, i+1:n] * X[i+1:n])) / T[i, i]
    return X

def get_input_matrix(n):
    A = np.zeros((n, n))
    b = np.zeros((n, 1))

    print(f"Enter elements of matrix A ({n}x{n}):")
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f"A[{i+1}][{j+1}]: "))

    print("Enter elements of matrix B:")
    for i in range(n):
        b[i] = float(input(f"B[{i+1}]: "))

    return A, b

def main():
    n = int(input("Enter the size of the matrix (n x n): "))
    A, b = get_input_matrix(n)

    T = gaussian_elimination(A, b)
    if T is None:
        print("Error:", T)
    else:
        X = back_substitution(T)
        if X is None:
            print("Error:", X)
        else:
            print('Solution:')
            for i, val in enumerate(X):
                print(f"X{i+1} = {val}")

if __name__ == "__main__":
    main()
