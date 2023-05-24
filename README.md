# summer-api

Summarises the news!

Deployed here: <https://summer-api.fly.dev/>.

## Local setup

This app required either Python >= 3.11 or docker.

Install poetry if you don't have it already:

```shell
pip install poetry
```

Install dependencies:

```shell
poetry install
```

Start the app:

```shell
poetry run uvicorn app.main:app --reload
```

Test the app:

```shell
poetry run pytest
```
