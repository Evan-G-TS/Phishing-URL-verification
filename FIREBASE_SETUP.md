# Firebase Setup Guide for Flask Backend

This guide will walk you through setting up Firebase as the backend database for your Flask phishing URL detection app. You will use **Firebase Firestore** (NoSQL database) to store user-submitted URLs and their classification results.

---

## 1. Create a Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/).
2. Click **Add project**.
3. Enter a project name (e.g., `phishing-url-detection`).
4. (Optional) Disable Google Analytics for this project.
5. Click **Create Project** and wait for setup to complete.

---

## 2. Register Your App (Web App)

1. In your Firebase project dashboard, click the web icon (`</>`) to add a web app.
2. Enter an app nickname (e.g., `phishing-web`), then click **Register app**.
3. You will see your Firebase SDK config. **Copy the config object** (you'll need the API keys and project info for your Flask app).


---
Initiate your project
Run this command from your app's root directory:
**firebase init**

When you're ready, deploy your web app
Put your static files (e.g., HTML, CSS, JS) in your app's deploy directory (the default is "public"). Then, run this command from your app's root directory:
**firebase deploy**

After deploying, view your app at phishing-detector-2de7d.web.app
---


## 3. Enable Firestore Database

1. In the left sidebar, click **Build > Firestore Database**.
2. Click **Create database**.
3. Choose **Start in test mode** (for development/demo; restrict later for production).
4. Select a Cloud Firestore location (choose the closest region).
5. Click **Enable**.




## 4. Get Your API Keys and Project Info

- You will need the following from your Firebase config:
  - `apiKey`  "AIzaSyBjPu-D14FDLy2gtPfnyBRZYax33THhPO4",
  - `authDomain`  "phishing-detector-2de7d.firebaseapp.com",
  - `projectId` "phishing-detector-2de7d",
  - `storageBucket` "phishing-detector-2de7d.firebasestorage.app",
  - `messagingSenderId` "817409659920",
  - `appId`  "1:817409659920:web:dcd3b65afe105ea91c6695"

- Save these values for use in your Flask app (typically as environment variables or in a config file).
- 
-------------------FIREBASE SDK:
---

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBjPu-D14FDLy2gtPfnyBRZYax33THhPO4",
  authDomain: "phishing-detector-2de7d.firebaseapp.com",
  projectId: "phishing-detector-2de7d",
  storageBucket: "phishing-detector-2de7d.firebasestorage.app",
  messagingSenderId: "817409659920",
  appId: "1:817409659920:web:dcd3b65afe105ea91c6695",
  measurementId: "G-50LFR5BCL4"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

---

Example config:
```js
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "SENDER_ID",
  appId: "APP_ID",
  measurementId: "G-MEASUREMENT_ID"
};
```

---

## 5. Set Firestore Security Rules (Optional for Demo)

- For development, you can use test mode (open access). For production, update your rules to restrict access.
- Example (test mode):
```js
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true;
    }
  }
}
```
- For production, see [Firestore Security Rules Docs](https://firebase.google.com/docs/firestore/security/get-started).

---

## 6. (Optional) Enable Authentication

- If you want to restrict who can write/read data, enable **Authentication** (e.g., Email/Password, Google Sign-In) in the Firebase console.

---

## 7. Install Python Firebase Library

- In your Flask project, you will use [`firebase-admin`](https://pypi.org/project/firebase-admin/) for server-side access:

```bash
pip install firebase-admin
```

**Admin SDK configuration snippet:
**
---
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
---



## 8. Generate Service Account Key

1. In the Firebase console, go to **Project Settings** (gear icon > Project settings).
2. Click **Service accounts** tab.
3. Click **Generate new private key** under Firebase Admin SDK.
4. Download the JSON file and save it securely (e.g., as `serviceAccountKey.json` in your project, but **never commit it to GitHub**).

---

## 9. Next Steps

- You are now ready to connect your Flask app to Firebase Firestore using the `firebase-admin` SDK and your service account key.
- Store your API keys and service account JSON securely (use environment variables or a config file, not hardcoded in source code).

---

**References:**
- [Firebase Console](https://console.firebase.google.com/)
- [Firestore Python Admin SDK Docs](https://firebase.google.com/docs/admin/setup)
- [Firestore Security Rules](https://firebase.google.com/docs/firestore/security/get-started)
