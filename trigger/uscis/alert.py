import requests
from datetime import datetime, timezone
import yaml
import os
import sys

sys.path.append(f"{os.path.dirname(__file__)}/../../api")
import gmail
import checkUSCIS as uscis
import json
import copy

receipt_numbers = ["MSC2290390290", "MSC2290390292", "MSC2290390291"]


def record_status(new_status: dict):

    path = f"{os.path.dirname(__file__)}/history.yaml"
    history = yaml.safe_load(open(path, "r"))
    history.insert(0, new_status)
    yaml.dump(history, open(path, "w"))


def check_msg(input:dict, case_num:str):

    output = input

    status = uscis.requestStatus(case_num)

    output[case_num] = status
    
    return output

def update_status(input:dict, case_numbers: list):

    output = copy.deepcopy(input)

    for case_num in case_numbers:
        output = check_msg(output, case_num)

    return output

def read_msg():
    history = yaml.safe_load(open(os.path.dirname(__file__) + "/history.yaml", "r"))
    return history[0]


if __name__ == "__main__":

    old_status = read_msg()
    new_status = update_status(old_status, receipt_numbers)

    if new_status != old_status:

        new_status["date"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        msg = json.dumps(new_status, indent=4)
        gmail.send_strmsg(title="Python: USCIS update", msg=msg)

        record_status(new_status)
    
