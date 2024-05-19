"""Main"""

import os
from typing import Annotated
import requests
import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from howmuch.security import User, get_current_active_user, router


YNAB_BASE_URL = "https://api.ynab.com/v1"


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


@app.get("/left-in-budget/{budget_id}/{category_id}")
async def left_in_budget(
    budget_id: str,
    category_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """left_in_budget"""

    ynab_access_token = os.environ.get("YNAB_ACCESS_TOKEN")

    print(current_user)

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
