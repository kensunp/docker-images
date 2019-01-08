#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers = '192.168.1.238:9092')

msg_dict = {
    "sleep_time":10,
    "db_config":{
        "database":"test_1",
        "host":"192.168.1.238",
        "user":"root",
        "password":"root"
    },
    "table":"msg",
    "msg":"Hello Workd"
}

msg = json.dumps(msg_dict).encode('utf-8')
producer.send("mykafka",msg,partition=0)
producer.close()
