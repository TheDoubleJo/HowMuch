"""Main"""

import os
import requests
from fastapi import FastAPI

app = FastAPI()

YNAB_BASE_URL = "https://api.ynab.com/v1"


@app.get("/left-in-budget/{budget_id}/{category_id}")
async def left_in_budget(budget_id: str, category_id: str):
    """left_in_budget"""

    ynab_access_token = os.environ.get("YNAB_ACCESS_TOKEN")

    headers = {"Authorization": f"Bearer {ynab_access_token}"}
    response = requests.get(
        f"{YNAB_BASE_URL}/budgets/{budget_id}/categories/{category_id}",
        headers=headers,
        timeout=10,
    )

    data = response.json()

    if response.status_code == 200:
        return {"balance": data["data"]["category"]["balance"]}

    return data
