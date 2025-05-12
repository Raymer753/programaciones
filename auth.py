
import pandas as pd
import requests

ZABBIX_URL = "http://172.16.1.43:8080/api_jsonrpc.php"
ZABBIX_TOKEN = "d347ca7066749e094f29b7b8e4d8ced3c534dffee8341789a92b44d1ec9299fc"

headers = {
    "Content-Type": "application/json-rpc",
    "Authorization": f"Bearer {ZABBIX_TOKEN}"
}

def metricas(hostid1, hostid2, hostid3): 
    payload = {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "hostids": [hostid1, hostid2, hostid3],
            "output": ["itemid"],
            "search": {"name": "SNMP agent availability"},
            "sortfield": "name"
        },
        "id": 1
    }
    response = requests.post(ZABBIX_URL, json=payload, headers=headers)
    data = response.json()

    items = data.get("result", [])

    def get_id(idx):
        try:
            return int(items[idx]["itemid"])
        except (IndexError, KeyError, ValueError):
            return None

    return get_id(0), get_id(1), get_id(2)

id1, id2, id3 = metricas(10660, 10661, 10662)