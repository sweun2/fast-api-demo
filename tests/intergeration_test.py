import requests

BASE = "http://localhost:8000"

def test_create_and_read_user():
    payload = {
        "username": "alice",
        "email": "alice@example.com",
        "password": "secret"
    }
    res = requests.post(f"{BASE}/users/", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"
    user_id = data["id"]

    res2 = requests.get(f"{BASE}/users/{user_id}")
    assert res2.status_code == 200
    data2 = res2.json()
    assert data2["id"] == user_id
    assert data2["username"] == "alice"
    assert data2["email"] == "alice@example.com"

test_create_and_read_user()