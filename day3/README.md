# Profile Card Gallery

A beginner-friendly React + Vite application that demonstrates core React concepts through an interactive profile card gallery. Perfect for learning about components, props, state management, and responsive design.

## Features

- **Responsive Grid Layout** - Automatically adjusts from 1 column (mobile) to 3 columns (desktop)
- **Interactive Search** - Filter profiles by name, role, or skills in real-time
- **Reusable Components** - Demonstrates component composition and prop passing
- **Modern UI Design** - Features soft shadows, rounded corners, and smooth hover animations
- **Professional Structure** - Organized with separate folders for components, data, and styles
- **Accessible** - Built with semantic HTML and ARIA labels

## Learning Outcomes

This project teaches fundamental React concepts:

### 1. **JSX** 
   - Learn how to write HTML-like syntax in JavaScript
   - See examples in all component files

### 2. **Components**
   - `Card.jsx` - Reusable component that displays a single profile
   - `Gallery.jsx` - Container component that renders multiple cards
   - `Navbar.jsx` - Navigation header component
   - `SearchBar.jsx` - Search input component with state management

### 3. **Props**
   - See how data flows from parent to child components
   - `Gallery` passes profile data to `Card` via props
   - Example: `<Card name={profile.name} role={profile.role} />`

### 4. **Dynamic Rendering with .map()**
   - In `Gallery.jsx`, the `.map()` function renders an array of profiles
   - Learn how to loop through data and create components for each item
   ```jsx
   {filteredProfiles.map((profile) => (
     <Card key={profile.id} {...profile} />
   ))}
   ```

### 5. **State Management**
   - `useState` hook for managing search input
   - See how state changes trigger component re-renders

### 6. **CSS & Responsive Design**
   - Mobile-first approach with media queries
   - CSS Grid for flexible layouts
   - CSS Variables for consistent theming
   - Hover animations and transitions

## Project Structure

```
profile-card-gallery/
├── src/
│   ├── components/
│   │   ├── Card.jsx           # Individual profile card component
│   │   ├── Gallery.jsx        # Gallery container with .map() rendering
│   │   ├── Navbar.jsx         # Navigation header
│   │   └── SearchBar.jsx      # Search input component
│   ├── data/
│   │   └── profiles.js        # Sample profile data array
│   ├── styles/
│   │   ├── index.css          # Global styles and CSS variables
│   │   ├── App.css            # App component styles
│   │   ├── Navbar.css         # Navbar styles
│   │   ├── SearchBar.css      # SearchBar styles
│   │   ├── Gallery.css        # Gallery grid layout
│   │   └── Card.css           # Card component styles
│   ├── App.jsx                # Main app component
│   └── main.jsx               # Entry point
├── index.html                 # HTML template
├── vite.config.js             # Vite configuration
├── package.json               # Project dependencies
└── README.md                  # This file
```

## Getting Started

### Prerequisites
- Node.js (v16 or higher)
- npm or pnpm

### Installation

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd profile-card-gallery
   ```

3. Install dependencies:
   ```bash
   pnpm install
   # or
   npm install
   ```

### Development

Start the development server:

```bash
pnpm dev
# or
npm run dev
```

The application will open at `http://localhost:3000` with hot module replacement (HMR) enabled. Changes to your files will automatically refresh the browser.

### Building for Production

Create an optimized production build:

```bash
pnpm build
# or
npm run build
```

The built files will be in the `dist/` folder, ready for deployment.

### Preview Production Build

To test the production build locally:

```bash
pnpm preview
# or
npm run preview
```

## Key Concepts Explained

### Understanding Props in Card.jsx

```jsx
function Card({ id, name, role, bio, image, location }) {
  // Each prop is like a function parameter
  // The parent (Gallery) passes these values
  return <h2>{name}</h2>  // Use prop just like a variable
}
```

### Using .map() in Gallery.jsx

```jsx
// This converts an array of profiles into an array of Card components
{filteredProfiles.map((profile) => (
  <Card 
    key={profile.id}  // Always provide a unique key for lists
    name={profile.name}
    role={profile.role}
    // ... other props
  />
))}
```

### Managing State with useState

```jsx
const [searchTerm, setSearchTerm] = useState('')

const handleChange = (e) => {
  setSearchTerm(e.target.value)  // Update state
  // This causes App to re-render, filtering profiles
}
```

## Customization

### Adding New Profiles

Edit `src/data/profiles.js`:

```javascript
const profiles = [
  {
    id: 11,
    name: 'Your Name',
    role: 'Your Role',
    bio: 'Your bio here',
    image: 'https://image-url.com/photo.jpg',
    location: 'Your City'
  },
  // ... more profiles
]
```

### Changing Colors

Edit `src/styles/index.css` CSS variables:

```css
:root {
  --primary-color: #6366f1;      /* Change this to your brand color */
  --secondary-color: #ec4899;    /* Change accent color */
  --neutral-900: #111827;        /* Change text color */
}
```

### Modifying Layouts

CSS Grid in `src/styles/Gallery.css`:

```css
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--spacing-lg);
}
```

Change `minmax(300px, 1fr)` to adjust card sizing.

## Responsive Breakpoints

The design includes responsive styles for:
- **Mobile**: Less than 480px
- **Tablet**: 480px - 768px
- **Desktop**: 768px - 1024px
- **Large Desktop**: 1024px and above

Each breakpoint adjusts font sizes, spacing, and grid columns for optimal viewing.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Common Learning Questions

### Q: Why use a `key` prop when rendering lists?
**A:** React uses keys to identify which items have changed. Without keys, React re-renders all items when the list changes, which is inefficient.

### Q: How do I add more functionality?
**A:** Add event handlers to buttons (`onClick`), create new components, and manage state with `useState`. Start small and build from there!

### Q: Can I deploy this?
**A:** Yes! Build the project and upload the `dist/` folder to services like Vercel, Netlify, or GitHub Pages.

## Next Steps

To expand your learning:

1. **Add filtering by role** - Modify SearchBar to have multiple filter options
2. **Add a detail page** - Click "View Profile" to navigate to individual profile pages
3. **Add favorites** - Let users favorite profiles and persist to localStorage
4. **Add sorting** - Sort profiles by name or role
5. **Connect to a real API** - Fetch profiles from a backend instead of static data
6. **Add authentication** - Implement user accounts and profiles

## Resources

- [React Documentation](https://react.dev)
- [Vite Documentation](https://vitejs.dev)
- [MDN Web Docs - CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [CSS Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)

## Troubleshooting

### Port 3000 already in use
```bash
# Use a different port
pnpm dev -- --port 3001
```

### Images not loading
- Check that image URLs are accessible
- Ensure the image is a valid URL format
- Try using different Unsplash image URLs

### Styles not applying
- Clear your browser cache (Ctrl+Shift+Delete)
- Restart the dev server
- Check the CSS file paths are correct

## License

This project is open source and available for educational purposes.

---

Happy learning! 🚀
