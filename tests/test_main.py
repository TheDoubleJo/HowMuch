""""Tests"""

import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from howmuch.main import app
from howmuch.security import get_current_active_user, User

load_dotenv()


def get_current_active_user_override():
    """Test"""
    user = User(username="doublejo", email="doublejo@aol.com", disabled=False)
    return user


client = TestClient(app)
app.dependency_overrides[get_current_active_user] = get_current_active_user_override


def test_route():
    """Test route left"""

    budget_id = os.environ.get("BUDGET_ID")
    category_id = os.environ.get("CATEGORY_ID")

    response = client.get(f"/left-in-budget/{budget_id}/{category_id}")
    assert response.status_code == 200
    a = 1 / 0
    data = response.json()

    assert isinstance(data["balance"], int)
