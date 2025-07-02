import pandas as pd

with open("../logs/error.log", "r") as f:
    lines = f.read().splitlines()

with open("../logs/success.log", "r") as s:
    baris = s.read().splitlines()
    

df = pd.DataFrame(lines, columns=["alamat"])
df2 = pd.DataFrame(baris, columns=["alamat"])

error = len(df)
success = len(df2)


def compute(error, success):
    print(f"[❌] Jumlah data error: {error}")
    print(f"[✅] Jumlah data ditemukan: {success}")
    print(f"[⏩] Jumlah data total: ",error + success)

if __name__ == "__main__":
    compute(error,success)