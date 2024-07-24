import React from 'react'
import ReactDOM from 'react-dom/client'
// import App from './App.jsx'
// import './index.css'

import './color_changer/index.css'

// import NewApp from './increNo/NewApp.jsx'
import NewApp from './color_changer/NewApp.jsx'


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* <App /> */}
    
    <NewApp />

  </React.StrictMode>,
)
