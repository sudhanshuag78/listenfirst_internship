import { useState } from 'react'
import Navbar from './components/Navbar'
import SearchBar from './components/SearchBar'
import Gallery from './components/Gallery'
import './styles/App.css'

function App() {
  const [searchTerm, setSearchTerm] = useState('')

  return (
    <div className="app-container">
      <Navbar />
      <main className="main-content">
        <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
        <Gallery searchTerm={searchTerm} />
      </main>
    </div>
  )
}

export default App
