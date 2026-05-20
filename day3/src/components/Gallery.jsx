/**
 * Gallery Component
 * Renders a responsive grid of profile cards
 * Demonstrates the .map() function for rendering dynamic data
 * 
 * Props:
 * - searchTerm: the search query to filter profiles
 */
import { useMemo } from 'react'
import Card from './Card'
import profiles from '../data/profiles'
import '../styles/Gallery.css'

function Gallery({ searchTerm }) {
  // Filter profiles based on search term
  const filteredProfiles = useMemo(() => {
    if (!searchTerm.trim()) {
      return profiles
    }
    
    const lowerSearch = searchTerm.toLowerCase()
    return profiles.filter(profile => 
      profile.name.toLowerCase().includes(lowerSearch) ||
      profile.role.toLowerCase().includes(lowerSearch) ||
      profile.bio.toLowerCase().includes(lowerSearch)
    )
  }, [searchTerm])

  return (
    <section className="gallery">
      <div className="gallery-header">
        <h1 className="gallery-title">Our Team Members</h1>
        <p className="gallery-subtitle">
          Meet our talented professionals
        </p>
      </div>

      {filteredProfiles.length > 0 ? (
        <div className="gallery-grid">
          {/* Using .map() to render each profile as a Card component */}
          {filteredProfiles.map((profile) => (
            <Card
              key={profile.id}
              id={profile.id}
              name={profile.name}
              role={profile.role}
              bio={profile.bio}
              image={profile.image}
              location={profile.location}
            />
          ))}
        </div>
      ) : (
        <div className="gallery-empty">
          <p>No profiles found matching "{searchTerm}"</p>
        </div>
      )}

      <div className="gallery-footer">
        <p className="gallery-count">
          Showing {filteredProfiles.length} of {profiles.length} profiles
        </p>
      </div>
    </section>
  )
}

export default Gallery
