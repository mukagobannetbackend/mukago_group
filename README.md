# Mukago Group Website

A professional, advanced website for Mukago Group - a diversified business conglomerate with five subsidiaries.

## Features

- **Advanced Dark Theme**: Sleek, modern dark interface with cyan and gold accents
- **Responsive Design**: Fully responsive across all devices
- **Secure Authentication**: User login and registration system
- **Multiple Subsidiaries**: Dedicated pages for all five subsidiaries
- **Advanced Backend**: Flask-based Python backend with API endpoints
- **Search Functionality**: Real-time search across all content
- **Dashboard**: User dashboard with profile and subsidiary information
- **Media Gallery**: Professional media and news section
- **Contact System**: Contact form for inquiries

## Subsidiaries

1. **Mukago Capital** - Investment & Financial Services
2. **Mukago Properties** - Real Estate & Property Management
3. **Mukago Wallstreet Schools** - Education (Primary, Secondary, Institution)
4. **Mutoto Manufacturers** - Advanced Manufacturing Solutions
5. **Mukago Technologies** - Digital Innovation & Solutions

## Project Structure

```
mukago_group/
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── static/
│   ├── css/
│   │   ├── style.css              # Main stylesheet
│   │   └── auth.css               # Authentication pages stylesheet
│   ├── js/
│   │   └── main.js                # Main JavaScript file
│   └── images/
│       ├── hero_bg.png            # Hero background
│       ├── capital_office.png      # Mukago Capital office
│       ├── properties_office.png   # Mukago Properties office
│       ├── schools_campus.png      # School campus
│       ├── manufacturers_factory.png # Manufacturing facility
│       ├── tech_hub.png            # Technology hub
│       └── login_bg.png            # Login page background
└── templates/
    ├── base.html                  # Base template
    ├── index.html                 # Home page
    ├── about.html                 # About page
    ├── subsidiaries.html          # Subsidiaries overview
    ├── subsidiary_detail.html     # Individual subsidiary page
    ├── media.html                 # Media & news page
    ├── contact.html               # Contact page
    ├── login.html                 # Login page
    ├── register.html              # Registration page
    ├── dashboard.html             # User dashboard
    ├── 404.html                   # 404 error page
    └── 500.html                   # 500 error page
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Extract the project folder**
   ```bash
   cd mukago_group
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the website**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Demo Credentials

For testing the login functionality, use these credentials:

**Admin Account:**
- Email: `admin@mukago.com`
- Password: `Admin@123`

**User Account:**
- Email: `user@mukago.com`
- Password: `User@123`

## Features Overview

### Home Page
- Hero section with call-to-action buttons
- Subsidiaries overview grid
- Key features section
- Statistics display
- Latest news section

### Subsidiaries
- Individual pages for each subsidiary
- Detailed information and services
- Professional imagery
- Call-to-action buttons

### Authentication
- Dark-themed login page with advanced UI
- Registration system for new users
- Secure password handling
- Session management

### Dashboard
- User profile management
- Quick access to subsidiaries
- Recent news feed
- Account settings
- Document downloads

### Media & News
- News articles with filtering
- Press releases
- Media gallery
- Social media links
- Newsletter subscription

### Contact
- Contact form
- Department contact information
- Business hours
- Map integration
- Direct contact methods

## API Endpoints

The application provides several API endpoints:

- `GET /api/subsidiaries` - Get all subsidiaries
- `GET /api/subsidiary/<id>` - Get specific subsidiary
- `GET /api/news` - Get all news articles
- `GET /api/user/profile` - Get user profile (requires login)
- `GET /api/search?q=<query>` - Search functionality

## Customization

### Colors
Edit the CSS variables in `static/css/style.css` and `static/css/auth.css`:
```css
:root {
    --primary-color: #00d4ff;
    --secondary-color: #ffd700;
    --dark-bg: #0a0e27;
    /* ... more colors ... */
}
```

### Content
Edit the `subsidiaries_data` dictionary in `app.py` to modify subsidiary information.

### Images
Replace images in `static/images/` with your own while maintaining the same filenames.

## Security Notes

- This is a demo application. For production use:
  - Use a proper database instead of in-memory storage
  - Implement HTTPS
  - Use environment variables for sensitive data
  - Add CSRF protection
  - Implement rate limiting
  - Use secure session management

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance

- Lazy loading for images
- CSS animations and transitions
- Optimized asset delivery
- Responsive design for all screen sizes

## Support

For issues or questions, contact:
- Email: info@mukagogroup.com
- Phone: +1 (555) 123-4567

## License

© 2024 Mukago Group. All rights reserved.

## Version

Version 1.0.0 - Initial Release
