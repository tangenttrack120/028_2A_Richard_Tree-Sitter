import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

# kode fungsi, if/else, kelas
fungsi = b"""def sapa(nama):
    return "Halo " + nama
"""

ifelse = b"""if nilai >= 75:
    status = "Lulus"
else:
    status = "Ulang"
"""

kelas = b"""class Mahasiswa:
    def belajar(self):
        return True
"""

# ubah 'fungsi' dengan 'ifelse' atau 'kelas' untuk menguji kode
tree = parser.parse(fungsi)
print(tree.root_node)

