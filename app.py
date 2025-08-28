from flask import Flask, render_template, request, redirect, url_for, flash
import pickle
import os
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
    # TODO: Implement feature extraction logic to match your model's expectations
    # Example: return [len(url), ...]
    return []

if __name__ == '__main__':
    app.run(debug=True)
