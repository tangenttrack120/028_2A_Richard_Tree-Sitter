import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

kode = open(sys.argv[1], "rb").read()
pola = open(sys.argv[2]).read()
tree = parser.parse(kode)

cursor = QueryCursor(Query(PY, pola))

# Khusus query fungsi & jumlah parameter: gunakan matches() agar berpasangan
if "@params" in pola:
    for _, cap in cursor.matches(tree.root_node):
        nama = cap["nama"][0].text.decode()
        jumlah = cap["params"][0].named_child_count
        baris = cap["nama"][0].start_point[0] + 1
        print(f"Fungsi '{nama}' (baris {baris}) -> {jumlah} parameter")
else:
    hasil = cursor.captures(tree.root_node)
    for nama, nodes in hasil.items():
        for n in nodes:
            print(f"@{nama}  baris {n.start_point[0] + 1}: {n.text.decode()}")