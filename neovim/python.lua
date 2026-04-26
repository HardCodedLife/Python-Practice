-- ~/.config/nvim/ftplugin/python.lua

-- Use vim.opt_local so settings don't leak into other file types
vim.opt_local.expandtab = true
vim.opt_local.shiftwidth = 4
vim.opt_local.tabstop = 4
vim.opt_local.softtabstop = 4

-- Example: Add a vertical line at 88 characters (standard for 'Black' formatter)
vim.opt_local.colorcolumn = "88"

-- Python-specific keymap: Run the current file with <leader>r
vim.keymap.set('n', '<leader>r', ':w<CR>:!python3 %<CR>', { buffer = true, desc = "Run Python script" })
