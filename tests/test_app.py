import pytest
from app import app, get_website_text
import requests_mock

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test if the home route loads correctly."""
    response = client.get("/")
    assert response.status_code == 200

def test_predict_valid_text(client, mocker):
    """Test prediction endpoint with valid text input."""
    mock_model = mocker.patch("app.model")
    mock_model.predict.return_value = ["fake"]  # Mock the model's output
    
    response = client.post("/predict", data={"text": "This is a fake news article."})
    assert response.status_code == 200
    assert b"fake" in response.data  # Check if "fake" is in the rendered template

def test_predict_missing_text(client):
    """Test prediction endpoint when no text is provided."""
    response = client.post("/predict", data={})
    assert response.status_code == 400  # Expecting a bad request

def test_predict_url_valid(client, requests_mock, mocker):
    """Test prediction via URL scraping."""
    mock_model = mocker.patch("app.model")
    mock_model.predict.return_value = ["true"]  # Mock the model's output
    
    # Mock website response
    requests_mock.get("https://edition.cnn.com/2025/03/18/europe/analysis-putin-trump-phone-call-ukraine-intl-latam/index.html", text="<h1>Fake News</h1>")

    response = client.post("/predict-url", data={"url": "https://edition.cnn.com/2025/03/18/europe/analysis-putin-trump-phone-call-ukraine-intl-latam/index.html"})
    assert response.status_code == 200
    assert b"true" in response.data  # Ensure prediction is in the response

def test_explain_valid_text(client, mocker):
    """Test LIME explanation API with valid input."""
    mock_explainer = mocker.patch("app.explainer")
    mock_explainer.explain_instance.return_value.as_list.return_value = [("word1", 0.5), ("word2", -0.3)]
    
    response = client.post("/explain", json={"text": "Breaking news headline"})
    assert response.status_code == 200
    assert b"word1" in response.data  # Ensure explanation is in the response

def test_explain_missing_text(client):
    """Test LIME explanation API when no text is provided."""
    response = client.post("/explain", json={})
    assert response.status_code == 400  # Expecting a bad request

def test_get_website_text(requests_mock):
    """Test website text extraction function."""
    requests_mock.get("https://edition.cnn.com/2025/03/18/europe/analysis-putin-trump-phone-call-ukraine-intl-latam/index.html", text="<h1>Breaking News</h1><p>News content here</p>")
    text = get_website_text("https://edition.cnn.com/2025/03/18/europe/analysis-putin-trump-phone-call-ukraine-intl-latam/index.html")
    assert text == "Breaking News News content here"

