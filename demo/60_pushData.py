#!/usr/bin/env python
#!-*- coding:utf8 -*-

import requests
import time
import json

ts = int(time.time())
errorCount = 0.0
Count = 100.0
errorRate = errorCount/Count

payload = [
    {
        "endpoint": "prd-test-1.11.14-cnn1-a-000/cn/172.31.24.233",
        "metric": "test.123123:errorRate",
        "timestamp": ts,
        "step": 60,
        "value": errorRate,
        "counterType": "GAUGE",
        "tags": "idc=lg,loc=beijing",
    },

    {
        "endpoint": "prd-test-1.11.14-cnn1-a-000/cn/172.31.24.233",
        "metric": "test.123123:errorCount",
        "timestamp": ts,
        "step": 60,
        "value": errorCount,
        "counterType": "GAUGE",
        "tags": "idc=lg,loc=beijing",
    },
    {
        "endpoint": "prd-test-1.11.14-cnn1-a-000/cn/172.31.24.233",
        "metric": "test.123123:Count",
        "timestamp": ts,
        "step": 60,
        "value": Count,
        "counterType": "GAUGE",
        "tags": "idc=lg,loc=beijing",
    }
]


if __name__ == "__main__":
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
