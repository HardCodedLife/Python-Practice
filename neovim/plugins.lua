-- ~/.config/nvim/lua/plugins.lua

return {
  -- Completion Engine
  {
    'saghen/blink.cmp',
    dependencies = 'rafamadriz/friendly-snippets',
    version = '*',
    opts = {
      keymap = { preset = 'default' },
      sources = {
        default = { 'lsp', 'path', 'snippets', 'buffer' },
      },
    },
  },

  -- LSP Support (The Modern 0.11+ Way)
  {
    'neovim/nvim-lspconfig',
    dependencies = { 'williamboman/mason.nvim', 'williamboman/mason-lspconfig.nvim' },
    config = function()
      require('mason').setup()
      require('mason-lspconfig').setup({
        ensure_installed = { 'basedpyright' }
      })
      local capabilities = require('blink.cmp').get_lsp_capabilities()

      -- NEW SYNTAX: Use vim.lsp.config instead of require('lspconfig')
      vim.lsp.config('basedpyright', {
	      capabilities = capabilities,
	      -- Can add additional python-specific settings here
      })

      -- This command actually triggers the LSP for the current/future buffers
      vim.lsp.enable('basedpyright')
    end,
  },
  
  -- Add your favorite theme here too!
  { "catppuccin/nvim", name = "catppuccin", priority = 1000 },
  {
    'windwp/nvim-autopairs',
    event = "InsertEnter",
    config = true -- This runs require('nvim-autopairs').setup({}) automatically
  },
}
