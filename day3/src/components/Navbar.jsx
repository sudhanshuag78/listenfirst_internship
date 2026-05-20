/**
 * Navbar Component
 * Header navigation bar for the application
 */
import '../styles/Navbar.css'

function Navbar() {
  return (
    <header className="navbar">
      <nav className="navbar-content">
        <div className="navbar-logo">
          <h1>ProfileHub</h1>
          <span className="navbar-tagline">Discover Talent</span>
        </div>
        
        <ul className="navbar-links">
          <li><a href="#home">Home</a></li>
          <li><a href="#gallery">Gallery</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>
  )
}

export default Navbar
