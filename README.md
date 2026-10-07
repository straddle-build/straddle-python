# Straddle Python SDK

Use Straddle's Pay by Bank and Embed APIs from Python. The SDK provides synchronous and asynchronous clients, typed responses, authentication, and retries.

## Install

Use Python 3.9 or later. Install the package in your project's virtual environment:

```sh
python -m pip install straddle
```

The PyPI package is [`straddle`](https://pypi.org/project/straddle/). Its source lives in `straddle-build/straddle-python`.

## Make your first request

Create a sandbox API key in the [Straddle Dashboard](https://dashboard.straddle.com), then set it in your environment. See [API authentication](https://docs.straddle.com/api-reference/authentication) for the setup steps.

```sh
export STRADDLE_API_KEY="YOUR_SANDBOX_API_KEY"
```

Save the following example as `quickstart.py`. It requests the first page of customers from the sandbox and closes the client when the request finishes:

```python
import os

from straddle import StraddleAPI

with StraddleAPI(
    bearer=os.environ["STRADDLE_API_KEY"],
    base_url="https://sandbox.straddle.com",
) as client:
    page = client.customers.list(page_number=1, page_size=10)
    print(f"Customers on this page: {len(page.data)}")
```

For a SaaS platform key, add `straddle_account_id="YOUR_EMBEDDED_ACCOUNT_ID"` to the `list` arguments before running the example. This selects the embedded account whose customers you want to read. Direct accounts and marketplaces list customers without that header. See [platform account scoping](https://docs.straddle.com/guides/embed/api-headers).

Run the example:

```sh
python quickstart.py
```

A successful request prints the number of customers on the page. `Customers on this page: 0` is valid for an empty account. Customer records are in `page.data`; pagination and request metadata are in `page.meta`.

## Use the async client

`AsyncStraddleAPI` exposes the same resources and methods with `await`. Use an async context manager to close its connections:

```python
import asyncio
import os

from straddle import AsyncStraddleAPI


async def main() -> None:
    async with AsyncStraddleAPI(
        bearer=os.environ["STRADDLE_API_KEY"],
        base_url="https://sandbox.straddle.com",
    ) as client:
        page = await client.customers.list(page_number=1, page_size=10)
        print(f"Customers on this page: {len(page.data)}")


asyncio.run(main())
```

Apply the same account-scoping rule to the async request.

## Configure authentication and environments

The examples pass `STRADDLE_API_KEY` explicitly as `bearer`. If you omit `bearer`, the client reads `BEARER`.

Set `base_url` explicitly to select an environment. If you omit it, the client reads `STRADDLE_BASE_URL`, then defaults to `https://sandbox.straddle.com`. Production uses `https://production.straddle.com` and a production API key. See [environments](https://docs.straddle.com/api-reference/environments).

## Read additional pages

List methods return one response page. Choose the next `page_number` using `page.meta.total_pages`, and keep your filters and account scope the same between requests:

```python
page = client.customers.list(page_number=2, page_size=10)
```

This and the following snippets assume an open `client`, such as one inside the context manager in the first example. See the [method reference](./api.md) for each resource's filters and response types.

## Handle errors

Catch `APIStatusError` for an HTTP error response. Its `status_code`, `response`, and `body` describe the response. Connection errors raise `APIConnectionError`; timeouts raise `APITimeoutError`.

```python
from straddle import APIConnectionError, APIStatusError

try:
    page = client.customers.list(page_size=10)
except APIConnectionError:
    print("The request could not connect to Straddle.")
    raise
except APIStatusError as error:
    print(error.status_code, error.message)
    raise
```

For a `401`, check that the key matches the selected environment. For a `403`, check the key's permissions and account scope. See [API errors](https://docs.straddle.com/api-reference/errors) for response details.

## Set retries and timeouts

The client retries connection errors, `408`, `409`, `429`, and `5xx` responses twice by default. It uses exponential backoff and honors supported `Retry-After` values. Its default HTTPX timeout is 60 seconds, with a 5-second connection timeout. Retries can extend the total request duration.

Set `max_retries` and `timeout` in the constructor, or use `with_options` for a request:

```python
page = client.with_options(max_retries=0, timeout=30.0).customers.list(page_size=10)
```

For write operations that accept an idempotency key, pass the operation's `idempotency_key` argument. Reuse that value when retrying the same operation. See [idempotency](https://docs.straddle.com/api-reference/idempotency).

## Inspect raw and streaming responses

Use `with_raw_response` to inspect HTTP metadata before parsing the result:

```python
response = client.with_raw_response.customers.list(page_size=10)
print(response.status_code)
page = response.parse()
```

Use `with_streaming_response` in a context manager to read the body as a stream:

```python
with client.with_streaming_response.customers.list(page_size=10) as response:
    for line in response.iter_lines():
        print(line)
```

The async client provides the corresponding async response methods.

## Client options and logging

Set these options in the client constructor.

| Option | Purpose | Default |
| --- | --- | --- |
| `bearer` | API key | `BEARER` |
| `base_url` | API base URL | `STRADDLE_BASE_URL`, then sandbox |
| `timeout` | HTTPX timeout in seconds or an `httpx.Timeout` | 60 seconds; connection timeout 5 seconds |
| `max_retries` | Retry count | `2` |
| `default_headers` | Headers sent with each request | None |
| `default_query` | Query parameters sent with each request | None |
| `http_client` | Custom HTTPX client | SDK-managed client |

Methods also accept `extra_headers`, `extra_query`, `extra_body`, and `timeout` for individual requests.

Set `STRADDLE_LOG` to `info` or `debug` to enable HTTP logging. The SDK uses Python's standard `logging` module under the `straddle` logger.

## Reference and support

Use the following resources as you build your integration:

- [SDK method reference](./api.md): operations, parameters, and response types.
- [Straddle guides](https://docs.straddle.com): payment flows, sandbox testing, and API concepts.
- [GitHub issues](https://github.com/straddle-build/straddle-python/issues): SDK bugs and feature requests.
- [Versioning and contributions](./VERSIONING.md): submit customizations against `scalar-next` so Scalar carries them through regeneration.
- [Security policy](./SECURITY.md) and [Apache 2.0 license](./LICENSE).

Straddle generates this SDK with Scalar and maintains repository customizations through the workflow in `VERSIONING.md`.
