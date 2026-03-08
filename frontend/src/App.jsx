import { useState } from 'react'
import './App.css'
import placeholder from './assets/alan-placeholder.svg'
import BubbleMenu from './assets/BubbleMenu.jsx'

function makeItems(setPage) {
  return [
    {
      label: 'resources',
      href: '#',
      ariaLabel: 'Resources',
      rotation: -8,
      hoverStyles: { bgColor: '#3b82f6', textColor: '#ffffff' },
      onClick: () => setPage('resources')
    },
    {
      label: 'live coaching',
      href: '#',
      ariaLabel: 'Live Coaching',
      rotation: 8,
      hoverStyles: { bgColor: '#10b981', textColor: '#ffffff' },
      onClick: () => setPage('coaching')
    }
  ];
}

function App() {
  const [page, setPage] = useState('home') // 'home' or 'coaching'

  if (page === 'home') {
    return (
      <div className="home-page">
        <h1>Swing Sensei</h1>
        <p className="home-subtitle"><em>Your AI-powered badminton coach</em></p>
        <p className="home-subtitle">Ready to train? — click <em>yes</em> to get started.</p>
        {/* <button onClick={() => setPage('coaching')}>Resources</button>
        <button onClick={() => setPage('coaching')}>Start Coaching</button>
        <button onClick={() => setPage('coaching')}>See Summary</button> */}
        <div className="yes-no-wrapper">
          <BubbleMenu
            logo={<span style={{ fontWeight: 700 }}>RB</span>}
            items={makeItems(setPage)}
            menuAriaLabel="Toggle navigation"
            menuBg="#ffffff"
            menuContentColor="#111111"
            useFixedPosition={false}
            className="inline"
            animationEase="back.out(1.5)"
            animationDuration={0.5}
            staggerDelay={0.12}
          />
        </div>

        <img src={placeholder} alt="badminton" className='home-image'/>
      </div>
    )
  }

  if (page === 'resources') {
    return (<div className="resources-page">
        <button onClick={() => setPage('home')}>← Back to Home</button>
        <h1 className="resource">Videos</h1>
        <ul>
          <li><a href="https://www.youtube.com/watch?v=fBa08o5GEqw">Badminton Footwork Drills</a></li>
          <li><a href="https://www.youtube.com/watch?v=5VNL43j0-XI">Net Shots</a></li>
          <li><a href="https://www.youtube.com/watch?v=bJuiT6xzPuI">Common Mistakes</a></li>
        </ul>
        <h1 className="resource">Articles</h1>
        <ul>
          <li><a href="https://badminton-insight.com/footwork-articles/">Footwork</a></li>
          <li><a href="https://badminton-insight.com/training-articles/">Training Routines</a></li>
        </ul>
    </div>)
  }

  return (
    <div className='training-page'> 
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
