from app import app


def test_home_status_code():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_response_text():
    client = app.test_client()
    response = client.get("/")
    assert response.get_data(as_text=True) == "CI/CD is running"
