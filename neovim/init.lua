-- ~/.config/nvim/init.lua
--
-- 1. Bootstrap lazy.nvim (Downloads the manager if it's missing)
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
    vim.fn.system({
        "git", "clone", "--filter=blob:none",
        "https://github.com/folke/lazy.nvim.git", "--branch=stable", lazypath,
    })
end
vim.opt.rtp:prepend(lazypath)

-- 2. General Settings
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

-- 3. Load Plugins
-- This looks for lua/plugins.lua and loads the table it returns
require("lazy").setup("plugins")

-- 4. Apply Theme
vim.cmd.colorscheme("catppuccin")
