""""Tests"""

from fastapi.testclient import TestClient
from howmuch.main import app

client = TestClient(app)


def test_route():
    """Test route left"""

    budget_id = "budget_id"
    category_id = "category_id"

    response = client.get(f"/left-in-budget/{budget_id}/{category_id}")
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data["balance"], int)
