import { resolve } from 'node:path'
import { defineConfig } from 'vite'

// The front end is plain HTML and one script (public/app.js); there is nothing to compile.
// The API runs on port 8000 (`make dev` starts both).
export default defineConfig({
  server: { proxy: { '/api': 'http://127.0.0.1:8000' } },
  build: { rollupOptions: { input: { main: resolve(import.meta.dirname, 'index.html'), proof: resolve(import.meta.dirname, 'proof.html') } } },
})
