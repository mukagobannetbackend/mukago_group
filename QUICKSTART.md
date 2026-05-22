# Mukago Group Website - Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Extract the Project
```bash
unzip mukago_group.zip
cd mukago_group
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Open in Browser
Navigate to: **http://localhost:5000**

---

## 🔐 Demo Login Credentials

**Admin Account:**
- Email: `admin@mukago.com`
- Password: `Admin@123`

**User Account:**
- Email: `user@mukago.com`
- Password: `User@123`

---

## 📱 What You Get

✅ **5 Subsidiary Pages** - Mukago Capital, Properties, Schools, Manufacturers, Technologies
✅ **Advanced Dark Theme** - Professional cyan and gold design
✅ **User Authentication** - Secure login and registration
✅ **Responsive Design** - Works on desktop, tablet, and mobile
✅ **Media Gallery** - Professional images and news section
✅ **Search Functionality** - Real-time search across all content
✅ **User Dashboard** - Personalized dashboard for logged-in users
✅ **Contact System** - Contact form for inquiries
✅ **API Endpoints** - RESTful API for integration

---

## 🎨 Key Features

### Home Page
- Hero section with company overview
- Subsidiaries grid with quick access
- Key features and statistics
- Latest news feed

### Subsidiaries
- Individual pages for each subsidiary
- Detailed service descriptions
- Professional office imagery
- Call-to-action buttons

### Authentication
- Dark-themed login page
- User registration system
- Secure password handling
- Session management

### Dashboard
- User profile management
- Quick access to all subsidiaries
- Recent news and updates
- Account settings and preferences

### Media & News
- News articles with filtering
- Press releases section
- Professional media gallery
- Social media integration

---

## 🛠️ Customization

### Change Colors
Edit `/static/css/style.css` and `/static/css/auth.css`:
```css
:root {
    --primary-color: #00d4ff;      /* Cyan */
    --secondary-color: #ffd700;    /* Gold */
    --dark-bg: #0a0e27;            /* Dark background */
}
```

### Update Company Information
Edit `/app.py` and modify the `subsidiaries_data` dictionary with your company details.

### Replace Images
Place your images in `/static/images/` with the same filenames:
- `hero_bg.png` - Hero section background
- `capital_office.png` - Mukago Capital office
- `properties_office.png` - Mukago Properties office
- `schools_campus.png` - School campus
- `manufacturers_factory.png` - Manufacturing facility
- `tech_hub.png` - Technology hub
- `login_bg.png` - Login page background

---

## 📁 Project Structure

```
mukago_group/
├── app.py                    # Flask backend
├── requirements.txt          # Python dependencies
├── README.md                 # Full documentation
├── QUICKSTART.md             # This file
├── static/
│   ├── css/                  # Stylesheets
│   ├── js/                   # JavaScript files
│   └── images/               # Images and assets
└── templates/                # HTML templates
```

---

## 🌐 Pages Available

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Homepage with overview |
| About | `/about` | Company information |
| Subsidiaries | `/subsidiaries` | All subsidiaries overview |
| Subsidiary Detail | `/subsidiary/<id>` | Individual subsidiary page |
| Media | `/media` | News and media gallery |
| Contact | `/contact` | Contact form |
| Login | `/login` | User login |
| Register | `/register` | New user registration |
| Dashboard | `/dashboard` | User dashboard (requires login) |

---

## 🔌 API Endpoints

```
GET  /api/subsidiaries              - Get all subsidiaries
GET  /api/subsidiary/<id>           - Get specific subsidiary
GET  /api/news                      - Get all news articles
GET  /api/user/profile              - Get user profile (requires login)
GET  /api/search?q=<query>          - Search functionality
POST /login                         - User login
POST /register                      - User registration
POST /contact                       - Submit contact form
```

---

## ⚙️ Configuration

### Change Port
Edit `app.py` and modify:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to your port
```

### Enable/Disable Debug Mode
```python
app.run(debug=False)  # Set to False for production
```

---

## 🔒 Security Notes

This is a demo application. For production use:

1. **Use a Database** - Replace in-memory user storage with a real database
2. **Enable HTTPS** - Use SSL/TLS certificates
3. **Environment Variables** - Store secrets in environment variables
4. **CSRF Protection** - Implement Flask-WTF for CSRF protection
5. **Rate Limiting** - Add rate limiting to prevent abuse
6. **Input Validation** - Validate all user inputs
7. **Secure Headers** - Add security headers to responses

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change the port in app.py or use:
python app.py --port 8000
```

### Module Not Found Error
```bash
# Make sure you're in the project directory and virtual environment is activated
pip install -r requirements.txt
```

### Images Not Loading
```bash
# Ensure images are in: mukago_group/static/images/
# Check file names match those referenced in templates
```

---

## 📞 Support

For issues or questions:
- Email: info@mukagogroup.com
- Phone: +1 (555) 123-4567
- Website: mukagogroup.com

---

## 📄 License

© 2024 Mukago Group. All rights reserved.

---

**Enjoy your Mukago Group website! 🎉**
