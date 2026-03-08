import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


function App() {
  const [page, setPage] = useState('home') // 'home' or 'coaching'

  if (page === 'home') {
    return (
      <div style={{ background: '#040c29', color: 'white', height: '100vh', textAlign: 'center' }}>
        <h1>🏸 Coach Alan Wu</h1>
        <p>Select a shot to practice</p>
        <button onClick={() => setPage('coaching')}>Start Coaching</button>
      </div>
    )
  }

  return (
    <div>
      <button onClick={() => setPage('home')}>← Back to Home</button>
      <iframe
        src="http://localhost:8501"
        width="100%"
        height="800px"
        style={{ border: 'none' }}
      />
    </div>
  )
}

export default App
