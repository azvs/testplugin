#!-*- coding:utf8 -*-

import requests
import time
import json

ts = int(time.time())
payload = [
    {
        "endpoint": "172.31.0.66",
        "metric": "test-metric",
        "timestamp": ts,
        "step": 60,
        "value": 5,
        "counterType": "GAUGE",
        "tags": "",
    },

]


print json.dumps(payload)