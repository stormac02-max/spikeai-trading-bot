"""Read-only connection test for an Alpaca trading account.

Reads credentials from .env (or the environment), calls GET /v2/account and
GET /v2/clock, and prints a summary. It never places, changes or cancels orders.
"""

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

PAPER_URL = "https://paper-api.alpaca.markets"
LIVE_URL = "https://api.alpaca.markets"


def load_env(path):
    """Load KEY=VALUE lines from a .env file without overriding real env vars."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        value = value.strip().strip('"').strip("'")
        if value and not os.environ.get(key.strip()):
            os.environ[key.strip()] = value


def get(base_url, path, key_id, secret):
    request = urllib.request.Request(
        base_url + path,
        headers={
            "APCA-API-KEY-ID": key_id,
            "APCA-API-SECRET-KEY": secret,
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def money(value, currency):
    try:
        return f"{float(value):,.2f} {currency}"
    except (TypeError, ValueError):
        return str(value)


def main():
    load_env(Path(__file__).with_name(".env"))

    key_id = os.environ.get("APCA_API_KEY_ID", "").strip()
    secret = os.environ.get("APCA_API_SECRET_KEY", "").strip()
    base_url = os.environ.get("APCA_API_BASE_URL", "").strip().rstrip("/")
    if base_url.endswith("/v2"):
        base_url = base_url[: -len("/v2")]

    if not key_id or not secret:
        print("FAILED: APCA_API_KEY_ID and/or APCA_API_SECRET_KEY are not set.")
        print("Fill them in the .env file next to this script, then run it again.")
        return 2

    candidates = [base_url] if base_url else [PAPER_URL, LIVE_URL]
    account = None
    connected_url = None

    for url in candidates:
        try:
            account = get(url, "/v2/account", key_id, secret)
            connected_url = url
            break
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="replace")[:300]
            print(f"  {url} -> HTTP {error.code} {error.reason} {body}")
        except urllib.error.URLError as error:
            print(f"  {url} -> network error: {error.reason}")
        except TimeoutError:
            print(f"  {url} -> timed out")

    if account is None:
        print("FAILED: could not authenticate with Alpaca.")
        print("Check that the key and secret are correct, belong together, and")
        print("match the endpoint (paper keys only work on the paper URL).")
        return 1

    currency = account.get("currency", "USD")
    number = str(account.get("account_number", ""))
    masked = "*" * max(len(number) - 4, 0) + number[-4:]
    environment = "PAPER" if "paper" in connected_url else "LIVE"

    print(f"CONNECTED ({environment}) via {connected_url}")
    print(f"  Account number    : {masked}")
    print(f"  Status            : {account.get('status')}")
    print(f"  Cash              : {money(account.get('cash'), currency)}")
    print(f"  Buying power      : {money(account.get('buying_power'), currency)}")
    print(f"  Portfolio value   : {money(account.get('portfolio_value'), currency)}")
    print(f"  Trading blocked   : {account.get('trading_blocked')}")
    print(f"  Account blocked   : {account.get('account_blocked')}")
    print(f"  Pattern day trader: {account.get('pattern_day_trader')}")

    try:
        clock = get(connected_url, "/v2/clock", key_id, secret)
        state = "open" if clock.get("is_open") else "closed"
        print(f"  Market            : {state} (next open {clock.get('next_open')})")
    except (urllib.error.URLError, TimeoutError) as error:
        print(f"  Market clock      : unavailable ({error})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
