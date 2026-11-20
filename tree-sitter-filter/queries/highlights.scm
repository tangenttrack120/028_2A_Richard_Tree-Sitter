; Kata kunci logika dan operator berbasis kata (Tugas 4)
["and" "or" "not" "in" "contains"] @keyword

; Operator perbandingan simbolik
["=" "!=" ">" "<" ">=" "<="] @operator

; Tipe nilai literal
(string) @string
(number) @number
(boolean) @constant.builtin

; Nama field pada comparison maupun in_expression
(comparison field: (identifier) @property)
(in_expression field: (identifier) @property)