-- ~/.config/nvim/init.lua

vim.opt.clipboard="unnamedplus"
-- Use vim.opt for most settings (mimics :set in Vimscript)
vim.opt.number = true           -- Show line numbers
vim.opt.relativenumber = true   -- Relative line numbers (great for jumping)
--vim.opt.mouse = 'a'             -- Enable mouse support
vim.opt.ignorecase = true       -- Ignore case in search patterns
vim.opt.smartcase = true        -- ...unless \C or capital in search
vim.opt.cursorline = true       -- Highlight the current line
vim.opt.termguicolors = true    -- True color support (if your terminal supports it)

-- Tab / Indentation (General defaults)
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true        -- Convert tabs to spaces
vim.opt.smartindent = true

-- Set leader key (the prefix for custom shortcuts, e.g., <leader>w to save)
vim.g.mapleader = " "           -- Use space as leader
