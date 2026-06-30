# 🩺 Med Buddy – AI-Powered Heart Disease Prediction System

## 🌟 Introduction

Med Buddy is a full-stack Machine Learning healthcare application designed to predict the likelihood of heart disease using patient medical parameters. The project demonstrates the complete journey of transforming a Machine Learning model into a production-ready application by integrating data science, backend engineering, frontend development, and cloud deployment.

The primary objective of Med Buddy is to provide users with a simple and interactive platform where they can enter health-related information and receive an AI-powered prediction in real time. This project showcases practical implementation of Machine Learning in healthcare while following modern software engineering and deployment practices.

---

## 🎯 Project Objectives

The main goals of this project were:

* Develop an accurate heart disease prediction model.
* Compare multiple Machine Learning algorithms and select the most suitable model.
* Optimize model performance through hyperparameter tuning.
* Build a scalable prediction service using FastAPI.
* Create a user-friendly interface for non-technical users.
* Deploy the complete application to the cloud for public accessibility.
* Gain hands-on experience with end-to-end Machine Learning deployment.

---

## 📊 Data Analysis & Model Development

The project started with comprehensive data exploration and preprocessing. The dataset was carefully analyzed to understand feature distributions, identify patterns, detect inconsistencies, and prepare the data for model training.

Several Machine Learning algorithms were trained and evaluated to determine the most effective approach for heart disease prediction. Different models were compared using performance metrics such as:

* Accuracy
* Precision
* Recall
* F1 Score
* Cross-Validation Performance

After extensive experimentation and evaluation, the **Random Forest Classifier** was selected as the final model due to its superior performance, robustness, and ability to generalize well on unseen data.

---

## ⚙️ Hyperparameter Optimization

To further improve predictive performance, hyperparameter tuning was performed on the Random Forest model.

Different parameter combinations were explored to identify the optimal configuration that maximized model performance while reducing overfitting. This process significantly enhanced the model's reliability and prediction accuracy.

The final optimized model achieved strong performance and served as the foundation of the Med Buddy prediction system.

---

## 🏗️ Building the Training Pipeline

To ensure maintainability and reproducibility, a dedicated training pipeline was developed.

The training pipeline automates:

✅ Data loading

✅ Data preprocessing

✅ Feature preparation

✅ Model training

✅ Hyperparameter tuning

✅ Model serialization

This modular architecture makes retraining and future model updates straightforward and scalable.

---

## 🧠 Prediction Engine

After training the final model, a separate prediction module was created to handle real-time inference.

The prediction engine is responsible for:

* Loading the trained model
* Accepting user inputs
* Validating incoming data
* Transforming inputs into the required format
* Generating predictions
* Calculating prediction probabilities
* Returning meaningful diagnostic results

This separation of concerns improves code organization and maintainability.

---

## 🚀 Backend Development with FastAPI

To transform the Machine Learning model into a production-ready service.

### Why FastAPI?

* High-performance asynchronous framework
* Automatic API documentation
* Easy integration with Machine Learning models
* Strong request validation
* Production-ready architecture

### Why Pydantic?

* Input validation
* Type safety
* Data serialization
* Error handling

The API acts as the bridge between the frontend and the Machine Learning model, enabling real-time communication and prediction generation.

---

## 🎨 Frontend Development with Streamlit

A clean and interactive user interface was developed using Streamlit.

The frontend allows users to:

❤️ Enter health-related parameters

📈 Submit information for analysis

🤖 Receive AI-powered predictions

📊 View prediction probabilities

⚕️ Understand diagnostic outcomes

The application was designed to be intuitive, responsive, and accessible to users without technical expertise.

---

## ☁️ Cloud Deployment on AWS EC2

To make the application accessible from anywhere, the complete system was deployed on an AWS EC2 instance.

During deployment, several cloud engineering concepts were implemented:

* Linux server management
* SSH authentication using key pairs
* Python virtual environments
* Dependency management
* FastAPI server deployment
* Streamlit deployment
* Network configuration and security group management

Deploying the project on AWS provided valuable hands-on experience with real-world production environments.

---

## 🏛️ System Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ▼
Prediction Engine
  │
  ▼
Random Forest Model
  │
  ▼
Prediction Result
```

---

## 🛠️ Technology Stack

### Machine Learning

* Python
* Scikit-learn
* Random Forest Classifier
* Hyperparameter Tuning
* Pandas
* NumPy

### Backend

* FastAPI
* Pydantic
* Joblib

### Frontend

* Streamlit
* Custom UI Components

### Cloud & Deployment

* AWS EC2
* Linux
* SSH

### Development Tools

* Git
* GitHub
* VS Code

---

## ✨ Key Features

🔹 Heart Disease Risk Prediction

🔹 Optimized Random Forest Model

🔹 Real-Time Predictions

🔹 Probability-Based Results

🔹 Interactive Streamlit Dashboard

🔹 Cloud Deployment on AWS EC2

🔹 Scalable and Modular Design

🔹 Production-Oriented Workflow

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

* Machine Learning model development
* Model optimization techniques
* Backend API development
* Data validation and serialization
* Frontend application development
* Cloud deployment using AWS
* Linux server management
* End-to-end ML system design

This project strengthened my understanding of how Machine Learning models move from experimentation to production and how different technologies work together to deliver real-world AI solutions.

---

## Author: Kaushal Kumar

