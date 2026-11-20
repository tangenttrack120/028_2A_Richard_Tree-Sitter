# File uji 2: Memeriksa deteksi fungsi dengan panjang > 30 baris

def fungsi_pendek(x):
    return x * 2


def validasi_dan_ringkas_transaksi(transaksi_list):
    if not transaksi_list:
        return {
            "total_valid": 0,
            "total_batal": 0,
            "nominal_bersih": 0,
        }

    total_valid = 0
    total_batal = 0
    nominal_bersih = 0
    catatan_error = []

    for indeks, trx in enumerate(transaksi_list):
        status = trx.get("status", "unknown")
        nominal = trx.get("nominal", 0)

        if nominal < 0:
            catatan_error.append(f"Baris {indeks}: nominal negatif")
            continue

        if status == "paid":
            total_valid += 1
            nominal_bersih += nominal
        elif status == "cancelled":
            total_batal += 1
        else:
            catatan_error.append(f"Baris {indeks}: status '{status}' tidak dikenal")

    rata_rata = nominal_bersih / total_valid if total_valid > 0 else 0

    return {
        "total_valid": total_valid,
        "total_batal": total_batal,
        "nominal_bersih": nominal_bersih,
        "rata_rata": rata_rata,
        "error": catatan_error,
    }