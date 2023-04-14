#!/usr/bin/env python
import time
import pika
from random import uniform

rabbit_host = '10.128.0.5'
rabbit_user = 'perzi'
rabbit_password = 'r'
exchange = 'monitoring_measurements'
topic_glucosa = 'Medery.Rafael.Glucosa'
topic_peso = 'Medery.Rafael.Peso'
topic_temperatura = 'Medery.Rafael.Temperatura'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

print('> Enviando glucosa, peso y temperatura. Para salir, presiona CTRL+C')

while True:
    value_glucosa = round(uniform(10, 250), 1)
    payload_glucosa = "{'measurement':'glucosa','value':%r,'unit':'C'}" % (value_glucosa)
    channel.basic_publish(exchange=exchange,
                          routing_key=topic_glucosa, body=payload_glucosa)
    print("Monitoreo de glucosa: %r" % (value_glucosa))

    value_peso = round(uniform(40, 150), 1)
    payload_peso = "{'measurement':'peso','value':%r,'unit':'kg'}" % (value_peso)
    channel.basic_publish(exchange=exchange,
                          routing_key=topic_peso, body=payload_peso)
    print("Monitoreo de peso: %r kg" % (value_peso))

    value_temperatura = round(uniform(20, 40), 1)
    payload_temperatura = "{'measurement':'temperatura','value':%r,'unit':'C'}" % (value_temperatura)
    channel.basic_publish(exchange=exchange,
                          routing_key=topic_temperatura, body=payload_temperatura)
    print("Monitoreo de temperatura: %r" % (value_temperatura))

    time.sleep(1.5)

connection.close()