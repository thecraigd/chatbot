import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// This configuration tells Vite how to build and serve our application
export default defineConfig({
  // Enable React integration
  plugins: [react()],
  // Configure the development server
  server: {
    port: 3000,
    // Allow our React app to make requests to our Flask backend
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true
      }
    }
  }
})