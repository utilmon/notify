import requests
from datetime import datetime, timezone
import yaml
import os
import sys

sys.path.append(f"{os.path.dirname(__file__)}/../../api")
import gmail


def get_balance():
    """Returns BTC balance of the third whale

    :return: BTC balance of the third whale
    :rtype: float
    """
    return requests.get(
        "https://blockchain.info/q/addressbalance/1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ"
    ).json()/1e8


def record_bal(balance: int):
    entry = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "symbol": "BTC",
        "balance": balance,
    }

    path = f"{os.path.dirname(__file__)}/history.yaml"
    history = yaml.safe_load(open(path, "r"))
    history.insert(0, entry)
    yaml.dump(history, open(path, "w"))


def read_bal():
    history = yaml.safe_load(open(os.path.dirname(__file__) + "/history.yaml", "r"))
    return history[0]["balance"]


if __name__ == "__main__":

    current_balance = get_balance()
    diff = int(current_balance - read_bal())
    title = "Python: 3rd Whale alert"
    if diff > 1:
        msg = f"3rd BTC whale just bought {diff} BTC ({diff/current_balance * 100:.3g} % of portfolio)"
        record_bal(current_balance)
        gmail.send_strmsg(title=title, msg=msg)
    elif diff < -1:
        msg = f"3rd BTC whale just sold {-diff} BTC ({diff/current_balance * 100:.3g} % of portfolio)"
        record_bal(current_balance)
        gmail.send_strmsg(title=title, msg=msg)
