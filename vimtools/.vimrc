"set fileencodings=utf-8
"set fileencoding=utf-8
"set encoding=utf-8
set fileencodings=utf-8,gb2312,gbk,gb18030,cp936
set termencoding=utf-8,cp936

set t_Co=256
colorscheme wombat256mod
set tags=/home/peizhongyou/ECOM/mixer-TRUNK/tags
set ts=4
set expandtab
let Tlist_Auto_Open = 0 
let Tlist_Ctags_Cmd = '/usr/bin/ctags' 
let Tlist_Show_One_File = 1 
let Tlist_Exit_OnlyWindow =1
" set nobackup
set nocompatible
set backspace=indent,eol,start
set nu
set statusline=[%F]%y%r%m%*%=[Line:%l/%L,Column:%c][%p%%]
set laststatus=2
set hlsearch

" Uncomment the following to have Vim jump to the last position when
" " reopening a file
if has("autocmd")
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif

%retab! 
"set smartindent
set shiftwidth=4
if has("cscope")
	set csprg=~/.jumbo/bin/cscope
	" use both cscope and ctag for 'ctrl-]', ':ta', and 'vim -t'
	set cst
	" check cscope for definition of a symbol before checking ctags
	set csto=0
	set nocsverb
	" add any cscope database in current directory
	if filereadable("cscope.out")
	cs add cscope.out
	" else add database pointed to by environment
	elseif $CSCOPE_DB != ""
	cs add $CSCOPE_DB
	endif
	" show msg when any other cscope db added
	set csverb

	""" cscope/vim key mappings
	"
	"   's'   symbol: find all references to the token under cursor
	"   'g'   global: find global definition(s) of the token under cursor
	"   'c'   calls:  find all calls to the function name under cursor
	"   't'   text:   find all instances of the text under cursor
	"   'e'   egrep:  egrep search for the word under cursor
	"   'f'   file:   open the filename under cursor
	"   'i'   includes: find files that include the filename under cursor
	"   'd'   called: find functions that function under cursor calls
	"
	" NOTE: CTRL-\'s default use is as part of CTRL-\ CTRL-N typemap, which
	" basically just does the same thing as hitting 'escape';
	" CTRL-@ doesn't seem to have any default use).
	" You can change some or all of these maps to use other keys.  One
	" likely candidate is 'CTRL-_' (which also maps to CTRL-/, which is
	" easier to type).  By default it is used to switch between Hebrew and
	" English keyboard mode.
	" All of the maps involving the <cfile> macro use '^<cfile>$': this is
	" so that searches over '#include <time.h>' return only references to
	" 'time.h', and not 'sys/time.h', etc. (by default cscope will return
	" all files that contain 'time.h' as part of their name).

	" The first type of search, the result of your cscope search will be
	" displayed in the current window.  You can use CTRL-T to go back to
	" where you were before the search.
	nmap <C-\>s :cs find s <C-R>=expand("<cword>")<CR><CR>
	nmap <C-\>g :cs find g <C-R>=expand("<cword>")<CR><CR>
	nmap <C-\>c :cs find c <C-R>=expand("<cword>")<CR><CR>
	nmap <C-\>t :cs find t <C-R>=expand("<cword>")<CR><CR>
	nmap <C-\>e :cs find e <C-R>=expand("<cword>")<CR><CR>
	nmap <C-\>f :cs find f <C-R>=expand("<cfile>")<CR><CR>
	nmap <C-\>i :cs find i ^<C-R>=expand("<cfile>")<CR>$<CR>
	nmap <C-\>d :cs find d <C-R>=expand("<cword>")<CR><CR>

	" Using 'CTRL-spacebar' (intepreted as CTRL-@ by vim) then a search type
	" makes the vim window split horizontally, with search result displayed
	" in the new window.
	"nmap <C-_>s :scs find s <C-R>=expand("<cword>")<CR><CR>
	"nmap <C-_>g :scs find g <C-R>=expand("<cword>")<CR><CR>
	"nmap <C-_>c :scs find c <C-R>=expand("<cword>")<CR><CR>
	"nmap <C-_>t :scs find t <C-R>=expand("<cword>")<CR><CR>
	"nmap <C-_>e :scs find e <C-R>=expand("<cword>")<CR><CR>
	"nmap <C-_>f :scs find f <C-R>=expand("<cfile>")<CR><CR>
	"nmap <C-_>i :scs find i ^<C-R>=expand("<cfile>")<CR>$<CR>
	"nmap <C-_>d :scs find d <C-R>=expand("<cword>")<CR><CR>

	"" Hitting CTRL-space *twice* before the search type does a vertical
	"" split instead of a horizontal one
	"nmap <C-_><C-_>s :vert scs find s <C-R>=expand("<cword>")<CR><CR>
	"nmap <C-_><C-_>g :vert scs find g <C-R>=expand("<cword>")<CR><CR>
	"nmap <C-_><C-_>c :vert scs find c <C-R>=expand("<cword>")<CR><CR>
	"nmap <C-_><C-_>t :vert scs find t <C-R>=expand("<cword>")<CR><CR>
	"nmap <C-_><C-_>e :vert scs find e <C-R>=expand("<cword>")<CR><CR>
	"nmap <C-_><C-_>f :vert scs find f <C-R>=expand("<cfile>")<CR><CR>
	"nmap <C-_><C-_>i :vert scs find i ^<C-R>=expand("<cfile>")<CR>$<CR>
	"nmap <C-_><C-_>d :vert scs find d <C-R>=expand("<cword>")<CR><CR>

	nmap <F5> :!find . -iname '*.c' -o -iname '*.cpp' -o -iname '*.h' -o -iname '*.hpp' > cscope.files<CR> 
	                        \ :!cscope -b -i cscope.files -f cscope.out<CR> 
	                        \ :cs reset<CR>
endif

let g:winManagerWindowLayout='FileExplorer|TagList'
let g:winManagerWindowLayout='TagList'
nmap wm :WMToggle<cr>


syntax on
set number
set ruler
