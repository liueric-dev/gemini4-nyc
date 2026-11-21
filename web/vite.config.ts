import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// The API runs on port 8000 (`make dev` starts both).
export default defineConfig({
  plugins: [react()],
  server: { proxy: { '/api': 'http://127.0.0.1:8000' } },
})
