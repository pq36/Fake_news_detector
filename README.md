# Fake News Detector

A web application that utilizes machine learning to detect fake news articles.

## Features

- **User Input**: Submit news articles for analysis.
- **Real-time Prediction**: Get instant results indicating whether the news is "Fake" or "True".
- **User-Friendly Interface**: Interactive and easy-to-use web design.
- **Docker Support**: Deploy the application seamlessly using Docker.
- **Machine Learning Model**: Uses a pre-trained model to detect fake news.

## Installation

### **1. Clone the Repository**

```bash
git clone https://github.com/pq36/Fake_news_detector.git
cd Fake_news_detector
```

### **2. Set Up a Virtual Environment** *(optional but recommended)*

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

## Usage

### **Run the Application Locally**

```bash
python app.py
```

### **Access the Web Interface**

Open your browser and navigate to:\
👉 **[http://127.0.0.1:8080/](http://127.0.0.1:8080/)**

### **Submit an Article for Analysis**

1. Paste the news article text into the provided text area.
2. Click the **"Check News"** button to analyze.

### **View Results**

- The application will display whether the submitted news is **"Fake"** or **"True"**.

## Docker Deployment

To deploy the application using Docker:

### **1. Build the Docker Image**

```bash
docker build -t fake_news_detector .
```

### **2. Run the Docker Container**

```bash
docker run -d -p 8080:80 --name flask-container fake_news_detector
```

## Project Structure

```
Fake_news_detector/
│-- app.py               # Main Flask application
│-- model.pkl            # Pre-trained ML model for fake news detection
│-- requirements.txt     # List of dependencies
│-- Dockerfile          # Docker build instructions
│-- templates/          # HTML templates for UI
│-- static/             # Static files (CSS, JS, images)
```

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and submit a pull request.

For any questions or suggestions, feel free to open an issue.

---

🚀 **Happy Coding!**

