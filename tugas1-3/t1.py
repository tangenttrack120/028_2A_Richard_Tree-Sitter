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

"""
# ubah 'fungsi' dengan 'ifelse' atau 'kelas' untuk menguji kode
tree = parser.parse(fungsi)
print(tree.root_node)
"""

"""
# node bernama vs node anonim
tree_fungsi = parser.parse(fungsi)
func_node = tree_fungsi.root_node.children[0]

# Child langsung di dalam function_definition
for c in func_node.children:
    status = "bernama" if c.is_named else "anonim"
    print(f"  - tipe: {c.type!r:20} | teks: {c.text.decode()!r:15} | {status}")

# Child di dalam parameters
params_node = func_node.child_by_field_name("parameters")
for c in params_node.children:
    status = "bernama" if c.is_named else "anonim"
    print(f"  - tipe: {c.type!r:20} | teks: {c.text.decode()!r:15} | {status}")
"""

# Sengaja menghapus ':' setelah fungsi untuk menimbulkan error
fungsi_rusak = b"""def sapa(nama)
    return "Halo " + nama
"""
tree_rusak = parser.parse(fungsi_rusak)
print("Tree dengan sintaks rusak:")
print(tree_rusak.root_node)
print("has_error:", tree_rusak.root_node.has_error)