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
- uvicorn howmuch.main:app --reload

## cicd:
dagger call test-and-publish --src=..:howmuchview