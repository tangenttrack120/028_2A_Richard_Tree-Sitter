; Menangkap semua pemanggilan fungsi print(...)
(call
  function: (identifier) @fn
  arguments: (argument_list) @args
  (#eq? @fn "print"))
