from flask import Flask, render_template, request, redirect, url_for, flash
import pickle
import os
import re
import ipaddress
from urllib.parse import urlparse
from firebase_config import db

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev_secret_key')  # Change for production

# Load the ML model (update the path to your pickle file after exporting from your notebook)
MODEL_PATH = os.getenv('MODEL_PATH', 'model.pkl')
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print('Model loaded successfully.')
except Exception as e:
    print(f'Could not load model: {e}')
    model = None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            flash('Please enter a URL.')
            return redirect(url_for('home'))
        # Placeholder: Extract features from URL here
        features = extract_features(url)  # You need to implement this
        # Predict
        if model:
            prediction = model.predict([features])[0]
        else:
            prediction = 'Model not loaded'
        # Store in Firestore
        if db:
            db.collection('url_predictions').add({
                'url': url,
                'prediction': str(prediction)
            })
        return render_template('result.html', url=url, prediction=prediction)
    return render_template('home.html')

@app.route('/result')
def result():
    # This route is only used for rendering result.html directly (not recommended)
    return render_template('result.html')

def extract_features(url):
    features = []
    
    # Basic URL features
    features.append(len(url))
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    features.append(len(domain))
    
    try:
        ipaddress.ip_address(domain)
        features.append(1)
    except:
        features.append(0)
        
    features.append(len(parsed_url.path))
    
    # TLD-related features
    tld = ".".join(domain.split('.')[-1:])
    features.append(len(tld))
    
    # Counts of special characters
    features.append(url.count('='))
    features.append(url.count('?'))
    features.append(url.count('&'))
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(url.count('_'))
    features.append(url.count('/'))
    features.append(url.count('//'))
    features.append(url.count('@'))
    features.append(url.count('!'))
    features.append(url.count("'"))
    features.append(url.count('"'))
    features.append(url.count('

if __name__ == '__main__':
    app.run(debug=True)
))
    features.append(url.count('%'))
    features.append(url.count(','))
    features.append(url.count(';'))
    features.append(url.count('+'))
    features.append(url.count('*'))
    
    # Character ratios
    letters = sum(c.isalpha() for c in url)
    digits = sum(c.isdigit() for c in url)
    special_chars = len(url) - letters - digits
    
    try:
        features.append(letters / len(url))
        features.append(digits / len(url))
        features.append(special_chars / len(url))
    except ZeroDivisionError:
        features.append(0)
        features.append(0)
        features.append(0)
        
    # HTTPS feature
    features.append(1 if parsed_url.scheme == 'https' else 0)
    
    # Subdomain count
    features.append(len(domain.split('.')) - 2)
    
    # Keyword features
    features.append(1 if 'login' in url.lower() else 0)
    features.append(1 if 'signin' in url.lower() else 0)
    features.append(1 if 'webscr' in url.lower() else 0)
    features.append(1 if 'ebay' in url.lower() else 0)
    features.append(1 if 'paypal' in url.lower() else 0)
    features.append(1 if 'account' in url.lower() else 0)
    features.append(1 if 'verify' in url.lower() else 0)
    features.append(1 if 'update' in url.lower() else 0)
    features.append(1 if 'secure' in url.lower() else 0)
    features.append(1 if 'banking' in url.lower() else 0)
    
    # The following features would require fetching the URL content.
    # For now, we will just append zeros as placeholders.
    
    # Placeholder for content-based features
    num_content_features = 55 - len(features)
    features.extend([0] * num_content_features)
    
    return features

if __name__ == '__main__':
    app.run(debug=True)
