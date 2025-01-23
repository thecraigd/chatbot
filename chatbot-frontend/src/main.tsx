import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        {/* Redirect root to /chatbot */}
        <Route path="/" element={<Navigate to="/chatbot" replace />} />
        {/* Main chatbot route */}
        <Route path="/chatbot" element={<App />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
)