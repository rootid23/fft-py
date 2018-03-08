
function! AppendModeline()
  let l:modeline = "vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=indent fdl=1"
  let l:modeline = substitute(&commentstring, "%s", l:modeline, "")
  call append(line("$"), l:modeline)
endfunction
nnoremap <silent> ,aml :call AppendModeline()<CR>
"
"Replace comment
nmap ,rmc :%s/\/\//#/g<CR>

"Go to end of file and add python main
nnoremap ,mn <ESC>GA<CR><ESC>:.-1read tmpl/.main.tmpl<CR>I<BS><ESC>j0i<BS><ESC>l

nnoremap ,hdr <ESC>gg<ESC>:.-1read tmpl/.header.tmpl<CR>I<BS><ESC>j0i<BS><ESC>l
