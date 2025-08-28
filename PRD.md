Product Requirements Document (PRD)

Project Name: Phishing URL Detection

Owner: Evan [Your Last Name]

Date: 26 August 2025

Purpose
The purpose of this project is to develop a machine learning-based phishing URL detection system that identifies malicious URLs and provides a simple web interface for demonstration. The project showcases data science, cybersecurity awareness, and web development skills.

Goals:

Demonstrate data preprocessing and feature engineering on URLs.

Apply machine learning classification models to detect phishing URLs.

Provide visualizations and insights into URL patterns.

Develop a Flask web application for interactive demonstration.

Scope
In Scope:

Data collection from a publicly available phishing URL dataset.

Feature extraction from URLs (length, character patterns, HTTPS presence, suspicious keywords, etc.).

Model training and evaluation using ML algorithms (Logistic Regression, Decision Tree, Random Forest).

Simple visualization of URL features and model performance.

Flask web application for user input and classification.

The backend will be based in Firebase, using Python Flask.

Do not store URLs—just process them in memory.
Use Python string methods and regex to parse the URL into features.
Ensure the feature vector matches the column order and data types used during training.

