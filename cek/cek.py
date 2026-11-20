import sys
from pathlib import Path
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

Q_TODO = Query(PY, '((comment) @c (#match? @c "TODO|FIXME"))')
Q_FUNGSI = Query(PY, "(function_definition name: (identifier) @nama) @fungsi")

FOLDER_ABAIKAN = {"venv", ".venv", ".git", "node_modules", "__pycache__"}


def cari_error_pertama(node):
    if node.is_error or node.is_missing:
        return node
    # Telusuri semua children (termasuk anonim) karena node MISSING bisa anonim
    for child in node.children:
        hasil = cari_error_pertama(child)
        if hasil is not None:
            return hasil
    return None


def cek_file(path):
    tree = parser.parse(path.read_bytes())

    # Fitur 1: komentar TODO / FIXME
    for node in QueryCursor(Q_TODO).captures(tree.root_node).get("c", []):
        teks = node.text.decode(errors="replace").strip()
        print(f"[TODO]   {path}:{node.start_point[0] + 1}: {teks}")

    # Fitur 2: fungsi yang panjangnya lebih dari 30 baris
    for _, cap in QueryCursor(Q_FUNGSI).matches(tree.root_node):
        nama_node = cap["nama"][0]
        fungsi_node = cap["fungsi"][0]
        jumlah_baris = fungsi_node.end_point[0] - fungsi_node.start_point[0] + 1
        if jumlah_baris > 30:
            nama = nama_node.text.decode(errors="replace")
            print(
                f"[PANJANG] {path}:{fungsi_node.start_point[0] + 1}: "
                f"fungsi '{nama}' ({jumlah_baris} baris)"
            )

    # Fitur 3: file yang pohonnya mengandung error sintaks
    if tree.root_node.has_error:
        err = cari_error_pertama(tree.root_node)
        baris_err = err.start_point[0] + 1 if err else 1
        jenis_err = "MISSING" if (err and err.is_missing) else "ERROR"
        print(f"[ERROR]  {path}:{baris_err}: sintaks tidak valid ({jenis_err})")


def main():
    if len(sys.argv) < 2:
        print("Pemakaian: python cek.py <folder>")
        sys.exit(1)

    target = Path(sys.argv[1])
    for path in target.rglob("*.py"):
        if any(bagian in FOLDER_ABAIKAN for bagian in path.parts):
            continue
        cek_file(path)


if __name__ == "__main__":
    main()