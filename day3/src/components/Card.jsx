/**
 * Card Component
 * A reusable profile card that displays user information
 * 
 * Props:
 * - id: unique identifier for the profile
 * - name: user's full name
 * - role: user's job title/role
 * - bio: short biography or description
 * - image: profile image URL
 * - location: user's location
 */
import '../styles/Card.css'

function Card({ id, name, role, bio, image, location }) {
  const handleViewProfile = () => {
    alert(`Viewing profile of ${name} - ${role}`)
  }

  return (
    <div className="card">
      <div className="card-image-container">
        <img 
          src={image} 
          alt={`${name} profile`} 
          className="card-image"
        />
        <div className="card-overlay"></div>
      </div>
      
      <div className="card-content">
        <h2 className="card-name">{name}</h2>
        <p className="card-role">{role}</p>
        <p className="card-location">{location}</p>
        
        <p className="card-bio">{bio}</p>
        
        <button 
          className="card-button"
          onClick={handleViewProfile}
        >
          View Profile
        </button>
      </div>
    </div>
  )
}

export default Card
