module.exports = {
  runtimeCompiler: true,
  devServer: {
    proxy: {
      "/furet-ui": {
        target: 'http://localhost:5000',
        changeOrigin: true,
        secure: false
      }
    }
  }
}
