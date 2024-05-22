""""Tests"""

from fastapi.testclient import TestClient
from howmuch.main import app
from howmuch.security import get_current_active_user, User


def get_current_active_user_override():
    """Test"""
    user = User(
        username="doublejo",
        email="doublejo@aol.com",
        disabled=False,
        budget_id="670e499b-c323-41c5-a428-7c3eeddd5a9c",
        category_id="39e18d9b-9a91-4d6d-a85e-be656976205d",
    )
    return user


client = TestClient(app)
app.dependency_overrides[get_current_active_user] = get_current_active_user_override


def test_route():
    """Test route left"""

    response = client.get("/left-in-budget")
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data["balance"], int)
