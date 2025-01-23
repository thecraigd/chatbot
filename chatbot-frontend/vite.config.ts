import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: '/chatbot/', // This tells Vite that your app will be served from /chatbot/
  build: {
    outDir: 'dist', // The directory where built files will go
    assetsDir: 'assets', // Where your static assets will go
  },
})