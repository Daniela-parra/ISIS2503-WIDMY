#!/usr/bin/env python
import time
import pika
from random import uniform

rabbit_host = 'host'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'monitoring_measurements'
topic = 'Medery.Rafael.Glucosa'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

print('> Enviando glucosa. To exit press CTRL+C')

while True:
    value = round(uniform(10,250), 1)
    payload = "{'value':%r,'unit':'C'}" % (value)
    channel.basic_publish(exchange=exchange,
                          routing_key=topic, body=payload)
    print("Monitored glucosa: %r" % (value))
    time.sleep(1.5)

connection.close()
