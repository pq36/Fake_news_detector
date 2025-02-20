# Fake News Detector

A web application that utilizes machine learning to detect fake news articles.

## Features

- **User Input**: Submit news articles for analysis.
- **Prediction Display**: View results indicating whether the news is "Fake" or "True".
- **Interactive Interface**: User-friendly design for seamless interaction.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/pq36/Fake_news_detector.git
   cd Fake_news_detector
   ```

2. **Set Up a Virtual Environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:

   ```bash
   python app.py
   ```

2. **Access the Web Interface**:

   Open your browser and navigate to `http://127.0.0.1:5000/`.

3. **Submit an Article**:

   - Paste the news article text into the provided text area.
   - Click the "Check News" button to analyze.

4. **View Results**:

   The application will display whether the submitted news is "Fake" or "True".

## Docker Deployment

To deploy the application using Docker:

1. **Build the Docker Image**:

   ```bash
   docker build -t fake_news_detector .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run -p 5000:5000 fake_news_detector
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## Project Structure

- `app.py`: Main Flask application.
- `model.pkl`: Pre-trained machine learning model for fake news detection.
- `requirements.txt`: List of Python dependencies.
- `Dockerfile`: Instructions to build the Docker image.
- `templates/`: HTML templates for the web interface.
- `static/`: Static files (CSS, JavaScript, images).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---
