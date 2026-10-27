"""
Model Data Mining Decision Tree
Dataset diambil dari Data_Mining_KKN.xlsx.
Catatan: contoh edukasi klasifikasi, bukan diagnosis medis.
"""
from pathlib import Path
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data_pasien.csv"
FEATURES = ["Usia", "BMI", "Glukosa", "Tekanan_Darah", "Riwayat_Keluarga"]

def main():
    df = pd.read_csv(DATA_FILE)
    X = df[FEATURES]
    y = df["Kelas"]

    # Model alternatif dari KNN: Decision Tree (pohon keputusan).
    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )
    model.fit(X, y)

    print("=" * 54)
    print("   KLASIFIKASI DATA PASIEN - DECISION TREE")
    print("=" * 54)
    print(f"Jumlah data latih : {len(df)}")
    print("Fitur             : " + ", ".join(FEATURES))
    print(f"Akurasi pada data latih: {model.score(X, y) * 100:.2f}%")
    print("\nAturan pohon keputusan:")
    print(export_text(model, feature_names=FEATURES))

    # Data pasien baru mengikuti contoh di file Excel.
    pasien_baru = pd.DataFrame([{
        "Usia": 42,
        "BMI": 28.5,
        "Glukosa": 130,
        "Tekanan_Darah": 128,
        "Riwayat_Keluarga": 1
    }])
    prediksi = model.predict(pasien_baru)[0]
    print("\nData pasien baru:")
    print(pasien_baru.to_string(index=False))
    print(f"\nHasil prediksi Decision Tree: {prediksi}")
    print("Catatan: hasil ini hanya untuk latihan data mining, bukan diagnosis medis.")

    # Simpan visualisasi pohon keputusan.
    plt.figure(figsize=(14, 8))
    plot_tree(
        model,
        feature_names=FEATURES,
        class_names=[str(c) for c in model.classes_],
        filled=True,
        rounded=True,
        impurity=False,
        proportion=False,
        fontsize=9
    )
    plt.title("Pohon Keputusan - Decision Tree")
    plt.tight_layout()
    output_image = BASE_DIR / "pohon_keputusan.png"
    plt.savefig(output_image, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"\nGambar pohon keputusan disimpan di: {output_image.name}")

if __name__ == "__main__":
    main()
