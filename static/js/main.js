// ==================== Global Variables ====================
const searchInput = document.getElementById('search-input');
const searchResults = document.getElementById('search-results');
let searchTimeout;

// ==================== Search Functionality ====================
if (searchInput) {
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        const query = this.value.trim();
        
        if (query.length < 2) {
            searchResults.classList.remove('active');
            searchResults.innerHTML = '';
            return;
        }
        
        searchTimeout = setTimeout(() => {
            performSearch(query);
        }, 300);
    });
    
    document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.classList.remove('active');
        }
    });
}

async function performSearch(query) {
    try {
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const results = await response.json();
        
        if (results.length === 0) {
            searchResults.innerHTML = '<div style="padding: 20px; text-align: center; color: #a0a0a0;">No results found</div>';
        } else {
            searchResults.innerHTML = results.map(result => `
                <a href="${result.url || '#'}" style="display: block; padding: 15px 20px; border-bottom: 1px solid #2a3050; color: #e0e0e0; text-decoration: none; transition: all 0.3s ease;">
                    <div style="font-weight: 600; color: #00d4ff;">${result.name}</div>
                    <div style="font-size: 12px; color: #a0a0a0; margin-top: 5px;">${result.description}</div>
                </a>
            `).join('');
        }
        
        searchResults.classList.add('active');
    } catch (error) {
        console.error('Search error:', error);
        searchResults.innerHTML = '<div style="padding: 20px; text-align: center; color: #ff6b6b;">Error performing search</div>';
    }
}

// ==================== Mobile Menu ====================
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger) {
    hamburger.addEventListener('click', function() {
        navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
    });
}

// ==================== Smooth Scroll ====================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href !== '#' && document.querySelector(href)) {
            e.preventDefault();
            document.querySelector(href).scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// ==================== Navbar Scroll Effect ====================
const navbar = document.querySelector('.navbar');
let lastScrollTop = 0;

window.addEventListener('scroll', function() {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (scrollTop > 100) {
        navbar.style.boxShadow = '0 8px 30px rgba(0, 0, 0, 0.5)';
    } else {
        navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
    }
    
    lastScrollTop = scrollTop;
});

// ==================== Lazy Loading Images ====================
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                }
                observer.unobserve(img);
            }
        });
    });
    
    document.querySelectorAll('img[data-src]').forEach(img => imageObserver.observe(img));
}

// ==================== Scroll Animations ====================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.subsidiary-card, .feature-card, .news-card, .stat-box').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
});

// ==================== Form Validation ====================
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePassword(password) {
    return password.length >= 8;
}

// ==================== Newsletter Subscription ====================
const newsletterForm = document.querySelector('.newsletter-form');
if (newsletterForm) {
    newsletterForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const email = this.querySelector('input[type="email"]').value;
        
        if (!validateEmail(email)) {
            alert('Please enter a valid email address');
            return;
        }
        
        // Simulate subscription
        alert('Thank you for subscribing to our newsletter!');
        this.reset();
    });
}

// ==================== Filter Functionality ====================
const filterButtons = document.querySelectorAll('.filter-btn');
const filterableItems = document.querySelectorAll('[data-category]');

filterButtons.forEach(btn => {
    btn.addEventListener('click', function() {
        const filter = this.dataset.filter;
        
        filterButtons.forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        
        filterableItems.forEach(item => {
            if (filter === 'all' || item.dataset.category === filter) {
                item.style.display = 'block';
                setTimeout(() => {
                    item.style.opacity = '1';
                }, 10);
            } else {
                item.style.opacity = '0';
                setTimeout(() => {
                    item.style.display = 'none';
                }, 300);
            }
        });
    });
});

// ==================== Utility Functions ====================
function formatDate(date) {
    return new Date(date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

function truncateText(text, length) {
    return text.length > length ? text.substring(0, length) + '...' : text;
}

// ==================== Console Message ====================
console.log('%cMukago Group', 'font-size: 24px; font-weight: bold; color: #00d4ff;');
console.log('%cInnovation | Integration | Elevation', 'font-size: 14px; color: #d4af37;');
console.log('%cWelcome to our platform!', 'font-size: 12px; color: #a0a0a0;');
