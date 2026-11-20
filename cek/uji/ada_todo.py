# File uji 1: Memeriksa deteksi komentar TODO dan FIXME

def hitung_diskon(harga, persen):
    # TODO: tambahkan validasi jika persen negatif atau > 100
    potongan = harga * (persen / 100)
    return harga - potongan


def proses_pesanan(daftar_item):
    total = 0
    for item in daftar_item:
        # FIXME: tangani kasus jika kunci 'harga' tidak ada di dictionary
        total += item["harga"]
    return total