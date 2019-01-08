#!/usr/local/bin/python

from kafka import KafkaConsumer

consumer = KafkaConsumer("mykafka",bootstrap_servers=["192.168.1.238:9092"])

for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)
