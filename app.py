from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'mukago_group_secret_key_2024'

# In-memory user database (for demo purposes)
users_db = {
    'admin@mukago.com': {
        'password': generate_password_hash('Admin@123'),
        'name': 'Admin User',
        'role': 'admin'
    },
    'user@mukago.com': {
        'password': generate_password_hash('User@123'),
        'name': 'Demo User',
        'role': 'user'
    }
}

# Subsidiaries data
subsidiaries_data = {
    'capital': {
        'name': 'Mukago Capital',
        'tagline': 'Investment & Financial Services',
        'description': 'Mukago Capital is a leading investment firm providing comprehensive financial solutions, portfolio management, and strategic investment opportunities.',
        'services': ['Portfolio Management', 'Investment Advisory', 'Wealth Management', 'Trading Services'],
        'image': '/static/images/capital_office.png'
    },
    'properties': {
        'name': 'Mukago Properties',
        'tagline': 'Real Estate & Property Management',
        'description': 'Mukago Properties specializes in premium real estate development, property management, and creating exceptional living and working spaces.',
        'services': ['Residential Development', 'Commercial Properties', 'Property Management', 'Investment Properties'],
        'image': '/static/images/properties_office.png'
    },
    'schools': {
        'name': 'Mukago Wallstreet Schools',
        'tagline': 'Education Excellence',
        'description': 'Mukago Wallstreet Schools offers world-class education from primary through higher institution levels, nurturing future leaders.',
        'divisions': {
            'primary': 'Primary School - Foundation for Excellence',
            'secondary': 'Secondary School - Building Leaders',
            'institution': 'Higher Institution - Advancing Knowledge'
        },
        'image': '/static/images/schools_campus.png'
    },
    'manufacturers': {
        'name': 'Mutoto Manufacturers',
        'tagline': 'Advanced Manufacturing Solutions',
        'description': 'Mutoto Manufacturers delivers cutting-edge manufacturing solutions with precision engineering and innovative production processes.',
        'services': ['Precision Engineering', 'Advanced Automation', 'Quality Assurance', 'Global Delivery'],
        'image': '/static/images/manufacturers_factory.png'
    },
    'technologies': {
        'name': 'Mukago Technologies',
        'tagline': 'Digital Innovation & Solutions',
        'description': 'Mukago Technologies drives digital transformation through innovative software solutions, cloud services, and emerging technology integration.',
        'services': ['Software Development', 'Cloud Solutions', 'AI & Machine Learning', 'Cybersecurity'],
        'image': '/static/images/tech_hub.png'
    }
}

# News/Media data
news_data = [
    {
        'id': 1,
        'title': 'Mukago Group Expands Global Operations',
        'date': '2024-05-15',
        'category': 'Business',
        'excerpt': 'Mukago Group announces expansion into 5 new markets across Africa and Asia.'
    },
    {
        'id': 2,
        'title': 'Mukago Technologies Launches AI Platform',
        'date': '2024-05-10',
        'category': 'Technology',
        'excerpt': 'Revolutionary AI platform designed for enterprise solutions and digital transformation.'
    },
    {
        'id': 3,
        'title': 'Mukago Wallstreet Schools Achieves 98% Pass Rate',
        'date': '2024-05-05',
        'category': 'Education',
        'excerpt': 'Students excel in national examinations with outstanding academic performance.'
    },
    {
        'id': 4,
        'title': 'Mutoto Manufacturers Wins Industry Award',
        'date': '2024-04-28',
        'category': 'Manufacturing',
        'excerpt': 'Recognition for innovation and excellence in manufacturing processes.'
    }
]

# Decorator for login requirement
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ==================== Authentication Routes ====================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if email in users_db and check_password_hash(users_db[email]['password'], password):
            session['user_id'] = email
            session['user_name'] = users_db[email]['name']
            session['user_role'] = users_db[email]['role']
            return jsonify({'success': True, 'message': 'Login successful', 'redirect': '/dashboard'})
        else:
            return jsonify({'success': False, 'message': 'Invalid email or password'}), 401
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        
        if email in users_db:
            return jsonify({'success': False, 'message': 'Email already registered'}), 400
        
        users_db[email] = {
            'password': generate_password_hash(password),
            'name': name,
            'role': 'user'
        }
        
        session['user_id'] = email
        session['user_name'] = name
        session['user_role'] = 'user'
        
        return jsonify({'success': True, 'message': 'Registration successful', 'redirect': '/dashboard'})
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# ==================== Main Routes ====================

@app.route('/')
def home():
    return render_template('index.html', subsidiaries=subsidiaries_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/subsidiaries')
def subsidiaries():
    return render_template('subsidiaries.html', subsidiaries=subsidiaries_data)

@app.route('/subsidiary/<subsidiary_id>')
def subsidiary_detail(subsidiary_id):
    if subsidiary_id not in subsidiaries_data:
        return render_template('404.html'), 404
    
    subsidiary = subsidiaries_data[subsidiary_id]
    return render_template('subsidiary_detail.html', subsidiary_id=subsidiary_id, subsidiary=subsidiary)

@app.route('/media')
def media():
    return render_template('media.html', news=news_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.get_json()
        # In a real application, you would save this to a database or send an email
        return jsonify({'success': True, 'message': 'Message sent successfully'})
    
    return render_template('contact.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user_name=session.get('user_name'))

# ==================== API Routes ====================

@app.route('/api/subsidiaries')
def api_subsidiaries():
    return jsonify(subsidiaries_data)

@app.route('/api/subsidiary/<subsidiary_id>')
def api_subsidiary(subsidiary_id):
    if subsidiary_id not in subsidiaries_data:
        return jsonify({'error': 'Subsidiary not found'}), 404
    return jsonify(subsidiaries_data[subsidiary_id])

@app.route('/api/news')
def api_news():
    return jsonify(news_data)

@app.route('/api/user/profile')
@login_required
def api_user_profile():
    return jsonify({
        'email': session.get('user_id'),
        'name': session.get('user_name'),
        'role': session.get('user_role')
    })

@app.route('/api/search')
def api_search():
    query = request.args.get('q', '').lower()
    results = []
    
    # Search in subsidiaries
    for key, subsidiary in subsidiaries_data.items():
        if query in subsidiary['name'].lower() or query in subsidiary['tagline'].lower():
            results.append({
                'type': 'subsidiary',
                'name': subsidiary['name'],
                'description': subsidiary['tagline'],
                'url': f'/subsidiary/{key}'
            })
    
    # Search in news
    for article in news_data:
        if query in article['title'].lower() or query in article['excerpt'].lower():
            results.append({
                'type': 'news',
                'name': article['title'],
                'description': article['excerpt'],
                'date': article['date']
            })
    
    return jsonify(results)

# ==================== Error Handlers ====================

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
