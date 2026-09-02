---
name: straddle-api-python-sdk
description: "Python SDK for Straddle API. Use when writing Python code that calls Straddle API with the straddle package: installing it, constructing and authenticating the client, and calling API operations."
---

# Straddle API Python SDK

Generated Python client for Straddle API, published as `straddle`. Use the generated client instead of hand-writing HTTP requests.

## Install

```sh
pip install straddle
```

## Client setup and authentication

```python
import os

from straddle import StraddleAPI

client = StraddleAPI(
    bearer=os.environ.get("BEARER"),
)
```

Provide credentials using the options below. Environment variables are read automatically when the target runtime supports them:

- `bearer` (env: `BEARER`) — Send the API key as a bearer token in the `Authorization` header.

## Calling operations

```python
import os

from straddle import StraddleAPI

client = StraddleAPI(
    bearer=os.environ.get("BEARER"),
)

account = client.accounts.retrieve(
    account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)

print(account)
```

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](./api.md) before writing a call.

## Error handling

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from straddle import APIStatusError

try:
    account = client.accounts.retrieve(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

## Requirements

- Python 3.8 or newer

## Reference files

- [README.md](./README.md) — full feature tour: client options, retries and timeouts, logging.
- [api.md](./api.md) — complete catalogue of every operation with request and response types.
