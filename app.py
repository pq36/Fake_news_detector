import pickle
from flask import Flask, request, jsonify, render_template
import lime
import lime.lime_text
import requests
from bs4 import BeautifulSoup

def get_website_text(url):
    """Scrapes the main content text from the given website URL."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Extracting all paragraph and heading tags (common content locations)
        text = " ".join([p.get_text() for p in soup.find_all(["p", "h1", "h2", "h3"])])
        
        return text if text else None

    except Exception as e:
        return None


# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

# Initialize LIME Explainer
explainer = lime.lime_text.LimeTextExplainer(class_names=["true", "fake"])

# Home route (renders web form)
@app.route("/")
def home():
    return render_template("index.html")

# API for predicting Fake/True News
@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("text")  # For web form
    if not text:
        return jsonify({"error": "No text provided"}), 400

    prediction = model.predict([text])[0]
    
    return render_template("index.html", text=text, prediction=prediction)

@app.route("/predict-url", methods=["POST"])
def predict_fake_news():
    url = request.form.get("url")  
    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Scrape text from the website
    text = get_website_text(url)

    prediction = model.predict([text])[0]
    
    return render_template("index.html", text=text, prediction=prediction)


# API for explaining the prediction
@app.route("/explain", methods=["POST"])
def explain():
    text = request.json.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Explain prediction using LIME
    exp = explainer.explain_instance(text, model.predict_proba, num_features=5)

    return jsonify({"explanation": exp.as_list()})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
