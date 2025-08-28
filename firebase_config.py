import firebase_admin
from firebase_admin import credentials, firestore
import os

# Path to your service account key JSON file
SERVICE_ACCOUNT_PATH = os.getenv('FIREBASE_SERVICE_ACCOUNT', 'phishing-detector-2de7d-firebase-adminsdk-fbsvc-ce0a95e8da.json')

# Initialize the Firebase Admin SDK
try:
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
        firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("Firebase Admin SDK initialized and Firestore client created.")
except Exception as e:
    print(f"Error initializing Firebase Admin SDK: {e}")
    db = None

# Usage:
# from firebase_config import db
# db.collection('your_collection').add({'field': 'value'})
