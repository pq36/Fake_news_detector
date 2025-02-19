import pickle
from flask import Flask, request, jsonify, render_template
import lime
import lime.lime_text

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
    app.run(debug=True)
