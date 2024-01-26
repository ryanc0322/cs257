"================
"Vundle plugin
"================
set nocompatible               " be improved, required
filetype off                   " required
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()            " required
Plugin 'VundleVim/Vundle.vim'  " required
Plugin 'Valloric/YouCompleteMe'
Plugin 'davidhalter/jedi-vim'
Plugin 'vim-airline/vim-airline'
Plugin 'scrooloose/syntastic'
Plugin 'jiangmiao/auto-pairs'
Plugin 'tpope/vim-fugitive'
Plugin 'mattn/emmet-vim'
Plugin 'alvan/vim-closetag'
Plugin 'vyperlang/vim-vyper'
Plugin 'c.vim'
call vundle#end()               " required
filetype plugin indent on       " required

"================
"vim-plug plugin
"================
"Plugins (Have to be at the very beginnning of the file)
call plug#begin('~/.vim/plugged')

"Collection of color schemes
Plug 'rafi/awesome-vim-colorschemes'
Plug 'junegunn/vim-peekaboo'
Plug 'preservim/nerdtree'

call plug#end()
"To update plugins -> :PlugUpdate
"To remove plugins -> :PlugClean

"YCM config
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
"YCM config END

"Syntastic configuration
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
"Syntastic configuration END

"Use the colorscheme
colorscheme iceberg
set background=dark

noremap <Up> <NOP>
noremap <Down> <NOP>
noremap <Left> <NOP>
noremap <Right> <NOP>
nnoremap nt<CR> :NERDTree<CR> "toggle nerdtree

set cursorline
set number
set mouse=a
set showcmd
set clipboard^=unnamed " Use the system register
set hlsearch
set incsearch
set encoding=utf-8
"set relativenumber
set nowrap

"vim autocomplete for html
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags

" auto indent 2 spaces
set autoindent expandtab tabstop=2 shiftwidth=2
