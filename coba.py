# Langkah 1: Pembuatan Dataset Sintetis
import numpy as np
import matplotlib.pyplot as plt
# 1. Menyiapkan data (100 sampel)
np.random.seed(42)
X = 2 * np.random.rand(100, 1) # Fitur: Biaya Iklan
y = 4 + 3 * X + np.random.randn(100, 1) # Target: Penjualan (dengan noise)
# Visualisasi data mentah
plt.scatter(X, y, color='blue', label='Data Observasi')
plt.xlabel('Biaya Iklan (Juta)')
plt.ylabel('Penjualan (Unit)')
plt.legend()
plt.title('Sebaran Data Simulasi Bisnis')
plt.show()


# Langkah 2: Estimasi Parameter dengan OLS (Analitik)
from sklearn.linear_network import LinearRegression
# Inisialisasi dan Training
lin_reg = LinearRegression()
lin_reg.fit(X, y)
# Menampilkan parameter yang ditemukan
print("--- Hasil OLS ---")
print(f"Intercept (Beta 0): {lin_reg.intercept_[0]}")
print(f"Slope (Beta 1): {lin_reg.coef_[0][0]}")


# Langkah 3: Estimasi Parameter dengan SGD (Iteratif)
from sklearn.linear_model import SGDRegressor
# Inisialisasi SGD dengan Learning Rate (eta0) = 0.1
sgd_reg = SGDRegressor(max_iter=1000, tol=1e-3, eta0=0.1, random_state=42)
sgd_reg.fit(X, y.ravel()) # .ravel() mengubah matriks jadi array 1D
print("\n--- Hasil SGD ---")
print(f"Intercept (Beta 0): {sgd_reg.intercept_[0]}")
print(f"Slope (Beta 1): {sgd_reg.coef_[0]}")


# Langkah 4: Visualisasi Perbandingan Garis Regresi
X_new = np.array([[0], [2]])
y_predict_ols = lin_reg.predict(X_new)
y_predict_sgd = sgd_reg.predict(X_new)
plt.scatter(X, y, color='blue')
plt.plot(X_new, y_predict_ols, "r-", label="Prediksi OLS")
plt.plot(X_new, y_predict_sgd, "g--", label="Prediksi SGD")
plt.xlabel("Biaya Iklan")
plt.ylabel("Penjualan")
plt.legend()
plt.title("Perbandingan Garis Estimasi Parameter")
plt.show()
