from app import demoapp

def test_home():
    with demoapp.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Hello, World!welcome to the Docker Demo App!" in response.data