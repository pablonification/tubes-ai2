import numpy as np
import pickle
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import Counter

class KNN:
    def __init__(self, k=3, metric='euclidean', weights='uniform'):
        """
        Inisialisasi Model KNN.
        
        Parameters:
        - k (int): Jumlah tetangga terdekat.
        - metric (str): Metode jarak ('euclidean', 'manhattan').
        - weights (str): 'uniform' (voting biasa) atau 'distance' (BONUS: weighted voting).
        """
        self.k = k
        self.metric = metric
        self.weights = weights
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        """
        Melatih model (menyimpan data latih).
        """
        self.X_train = np.array(X)
        self.y_train = np.array(y)
        print(f"Model KNN dilatih dengan {len(self.X_train)} data.")

    def _calculate_distance(self, x_query):
        """
        Menghitung jarak antara satu data test (x_query) dengan seluruh X_train.
        Menggunakan Vectorization (Broadcasting) agar cepat.
        """
        if self.metric == 'euclidean':
            # Rumus: sqrt(sum((x - y)^2))
            return np.sqrt(np.sum((self.X_train - x_query)**2, axis=1))
        
        elif self.metric == 'manhattan':
            # Rumus: sum(|x - y|)
            return np.sum(np.abs(self.X_train - x_query), axis=1)
        
        else:
            raise ValueError(f"Metric '{self.metric}' belum diimplementasikan.")

    def _predict_one(self, x_query):
        """
        Memprediksi satu sampel data.
        """
        # 1. Hitung jarak ke seluruh data latih
        distances = self._calculate_distance(x_query)
        
        # 2. Ambil K indeks dengan jarak terdekat
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = self.y_train[k_indices]
        k_nearest_dists = distances[k_indices]
        
        # 3. Voting Mechanism
        if self.weights == 'uniform':
            most_common = Counter(k_nearest_labels).most_common(1)
            return most_common[0][0]
        
        elif self.weights == 'distance':
            epsilon = 1e-5 
            weights = 1 / (k_nearest_dists + epsilon)
            
            class_weights = {}
            for label, w in zip(k_nearest_labels, weights):
                class_weights[label] = class_weights.get(label, 0) + w
            
            return max(class_weights, key=class_weights.get)

    def predict(self, X_test):
        """
        Memprediksi sekumpulan data X_test.
        """
        X_test = np.array(X_test)
        predictions = [self._predict_one(x) for x in X_test]
        return np.array(predictions)

    # Save & Load Model
    def save_model(self, filename):
        """Menyimpan objek model ke file .pkl"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print(f"Model berhasil disimpan ke {filename}")

    @staticmethod
    def load_model(filename):
        """Memuat objek model dari file .pkl"""
        with open(filename, 'rb') as f:
            return pickle.load(f)

# Visualisasi Proses Training/Klasifikasi (Bonus)
def generate_knn_video(model, X_train_2d, y_train, x_query_2d, filename='knn_process.mp4'):
    """
    Membuat video animasi proses pencarian tetangga terdekat.
    Syarat: Data harus sudah direduksi ke 2D (misal pakai PCA) agar bisa di-plot.
    """
    print("Sedang men-generate video visualisasi...")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    scatter = ax.scatter(X_train_2d[:, 0], X_train_2d[:, 1], c=y_train, cmap='viridis', alpha=0.6, label='Training Data')
    
    ax.scatter(x_query_2d[0], x_query_2d[1], c='red', marker='X', s=150, label='Query Point')
    
    dists = np.sqrt(np.sum((X_train_2d - x_query_2d)**2, axis=1))
    k_indices = np.argsort(dists)[:model.k]
    max_radius = dists[k_indices[-1]]
    
    circle = plt.Circle(x_query_2d, 0.0, color='red', fill=False, linestyle='--', linewidth=2)
    ax.add_patch(circle)
    
    ax.legend()
    ax.set_title(f"KNN Process (k={model.k})")
    
    def update(frame):
        progress = frame / 50
        current_radius = progress * max_radius * 1.1 
        circle.set_radius(current_radius)
        return circle,

    ani = animation.FuncAnimation(fig, update, frames=60, interval=50, blit=True)
    
    try:
        ani.save(filename, writer='ffmpeg', fps=30)
        print(f"Video berhasil disimpan: {filename}")
    except Exception as e:
        print(f"Gagal menyimpan video (pastikan ffmpeg terinstall): {e}")
        # Fallback ke GIF jika mp4 gagal
        ani.save(filename.replace('.mp4', '.gif'), writer='pillow', fps=30)