import pytest
from fastapi.testclient import TestClient
from  fastapi import status

from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.headers["content-type"] == 'application/json'
    assert response.json() == {"detail": "Not found"}

class TestHealthEndpoint:
    def test_health_test_status_code(self):
        response = client.get("/health")
        assert response.status_code == status.HTTP_200_OK
    
    def test_health_test_response_body(self):
        response = client.get("/health")
        assert response.json() == {"status": "healthy"}

class TestHelloEndpoint:
    @pytest.mark.parametrize("test_input, expected", [("world","Hello world"), ("","Hello "), ("1234", "Hello 1234"), ("  wo rld ", "Hello   wo rld "), ("@#$%", "Hello @#$%")])

    def test_hello_valid_name(self, test_input, expected): #correct input
        response = client.get(f"/hello?VALUE={test_input}")
        assert response.status_code == status.HTTP_200_OK
        assert response.headers["content-type"] == "application/json"
        assert response.json() == {"detail": expected} 
    
    def test_hello_missing_name(): #incorrect input
        response = client.get("/hello")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.headers["content-type"] == "application/json"
        assert response.json() == {"detail": "VALUE IS REQUIRED"}

    def test_hello_case_sensitivity(): #checking for case sensitivity
        response_lowercase = client.get(f"/hello?value=test")
        assert response_lowercase.status_code == status.HTTP_400_BAD_REQUEST
        assert response_lowercase.json() == {"detail": "VALUE is required"}

        response_uppercase = client.get(f"/hello?VALUE=test")
        assert response_uppercase.status_code == status.HTTP_200_OK
        assert response_uppercase.json() == {"detail": "Hello test"}