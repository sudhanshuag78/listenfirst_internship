/**
 * SearchBar Component
 * Input field for filtering profiles by name, role, or bio
 * 
 * Props:
 * - searchTerm: current search value
 * - setSearchTerm: function to update search value
 */
import '../styles/SearchBar.css'

function SearchBar({ searchTerm, setSearchTerm }) {
  const handleChange = (e) => {
    setSearchTerm(e.target.value)
  }

  const handleClear = () => {
    setSearchTerm('')
  }

  return (
    <div className="search-container">
      <div className="search-wrapper">
        <div className="search-input-group">
          <span className="search-icon">🔍</span>
          <input
            type="text"
            className="search-input"
            placeholder="Search by name, role, or skills..."
            value={searchTerm}
            onChange={handleChange}
            aria-label="Search profiles"
          />
          {searchTerm && (
            <button 
              className="search-clear"
              onClick={handleClear}
              aria-label="Clear search"
            >
              ✕
            </button>
          )}
        </div>
        <p className="search-hint">
          Type to search for professionals by name, role, or expertise
        </p>
      </div>
    </div>
  )
}

export default SearchBar
