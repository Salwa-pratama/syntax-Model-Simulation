import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
# 1. Membuat data asli
np.random.seed(42)
data_asli = np.random.randn(200, 2) + [2, 2]
data_asli = np.vstack([data_asli, np.random.randn(200, 2) + [-2, -2]])
data_asli = np.vstack([data_asli, np.random.randn(200, 2) + [2, -2]])
# Standarisasi
scaler = StandardScaler()
X_asli = scaler.fit_transform(data_asli)
# Klastering pada Data Asli
kmeans_asli = KMeans(n_clusters=3, random_state=42)
label_asli = kmeans_asli.fit_predict(X_asli)
# Menambahkan Gaussian Noise (0.5 adalah tingkat gangguan)
noise = np.random.normal(0, 0.5, X_asli.shape)
X_noisy = X_asli + noise
# Klastering pada Data Terganggu
kmeans_noisy = KMeans(n_clusters=3, random_state=42)
label_noisy = kmeans_noisy.fit_predict(X_noisy)
from sklearn.metrics import jaccard_score
# Menghitung stabilitas rata-rata untuk seluruh klaster
def hitung_stabilitas(label1, label2):
    # Menggunakan average='macro' untuk rata-rata stabilitas tiap klaster
    skor = jaccard_score(label1, label2, average='macro')
    return skor
stabilitas = hitung_stabilitas(label_asli, label_noisy)
print(f"Indeks Jaccard (Stabilitas Sistem): {stabilitas:.4f}")
