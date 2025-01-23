import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

// Create a root element for our React application
ReactDOM.createRoot(document.getElementById('root')!).render(
  // StrictMode helps catch common mistakes early
  <React.StrictMode>
    <App />
  </React.StrictMode>
)