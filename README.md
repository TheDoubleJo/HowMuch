[![Built with Devbox](https://jetpack.io/img/devbox/shield_galaxy.svg)](https://jetpack.io/devbox/docs/contributor-quickstart/)

# HowMuch
How much money I have on YNAB ?


## Add dependencies:
- poetry add requests

## Add dev dependencies:
- poetry add requests -G dev

## Local dev:
Add
dagger-io = {path = "cicd/dagger/sdk", develop = true}

in dev dependencies in pyproject.toml

## Start:
- devbox shell
- fastapi dev howmuch/main.py

## cicd:
dagger call test --src=..:howmuchview --secret_key=env:SECRET_KEY --ynab_access_token=env:YNAB_ACCESS_TOKEN --budget_id=env:BUDGET_ID --category_id=env:CATEGORY_ID

dagger call build-and-publish --src=..:howmuchview --registry_username=TheDoubleJo --registry_password=env:GH_TOKEN --secret_key=env:SECRET_KEY --ynab_access_token=env:YNAB_ACCESS_TOKEN --budget_id=env:BUDGET_ID --category_id=env:CATEGORY_ID