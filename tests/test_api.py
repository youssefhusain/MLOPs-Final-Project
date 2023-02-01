from fastapi.testclient import TestClient
from main import app

def test_predict():
    test_landmarks = [
        [117.29, 198.76], [124.63, 191.31], [126.44, 180.20], [121.04, 171.19],
        [114.39, 164.99], [128.71, 164.99], [129.61, 150.63], [129.22, 141.39],
        [128.27, 133.53], [121.72, 164.36], [123.99, 148.39], [124.48, 138.01],
        [124.50, 129.12], [114.75, 167.63], [111.69, 157.88], [113.22, 166.49],
        [115.14, 173.42], [108.09, 173.32], [105.69, 165.90], [107.82, 171.23],
        [109.83, 176.38]
    ]
    with TestClient(app) as client:  
        response = client.post("/predict", json={"landmarks": test_landmarks})
        assert response.status_code == 200, f"Error: {response.status_code} - {response.text}"
        assert response.json()["action"] in ["up", "down", "left", "right"]
