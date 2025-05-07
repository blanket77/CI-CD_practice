# test_app.py
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    
    print("!!GOOD!!")
    assert response.status_code == 200
    assert response.data == b"Hello, CI/CD! kimyouchan!!" # response.data는 bytes 타입이므로 b"Hello, CI/CD!"로 비교해야 함
